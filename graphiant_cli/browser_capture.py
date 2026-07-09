"""Playwright Chromium session: capture bearer from Graphiant API network traffic."""

from __future__ import annotations

import subprocess
import sys
import time
from typing import TYPE_CHECKING, Callable

from graphiant_cli.cli_logging import ensure_cli_logging, get_logger, safe_api_url_for_log
from graphiant_cli.token_parsing import (
    eligible_capture,
    extract_token_from_graphiant_api_response,
    extract_token_from_refresh_response,
    is_auth_refresh_url,
    is_graphiant_api_url,
    portal_root_url,
    token_from_authorization_headers_only,
)

if TYPE_CHECKING:
    from playwright.sync_api import Page, PlaywrightContextManager, Request, Response

logger = get_logger("browser_capture")

PLAYWRIGHT_AVAILABLE = False
sync_playwright: Callable[[], PlaywrightContextManager] | None = None
try:
    from playwright.sync_api import sync_playwright as _sync_playwright

    sync_playwright = _sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    pass


def playwright_yield_ms(page: Page, ms: int) -> None:
    """
    Yield so Playwright's sync driver can process network events.

    Avoid bare ``time.sleep`` in capture loops: it can block delivery of
    ``request`` / ``response`` handlers until the next Playwright call.
    """
    try:
        page.wait_for_timeout(ms)
    except Exception:
        time.sleep(ms / 1000.0)


def _install_chromium() -> bool:
    try:
        r = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            capture_output=True,
            text=True,
            timeout=600,
        )
        if r.returncode != 0:
            logger.warning(
                "playwright install chromium failed (exit %s): %s",
                r.returncode,
                (r.stderr or r.stdout or "").strip()[:500],
            )
            return False
        logger.info("playwright install chromium completed successfully")
        return True
    except subprocess.TimeoutExpired:
        logger.warning("playwright install chromium timed out")
        return False
    except OSError as e:
        logger.warning("playwright install chromium could not run: %s", e)
        return False


def _launch_failure_suggests_missing_browser(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return (
        "executable doesn't exist" in msg
        or "could not find browser" in msg
        or "browserType.launch" in msg
        or "chromium" in msg and "install" in msg
    )


def capture_token_via_browser(
    portal_url: str,
    timeout_seconds: int = 120,
    *,
    verbose: bool = False,
) -> str | None:
    """
    Open Chromium, listen for Graphiant ``/v1/`` / ``/v2/`` / ``…/auth/refresh`` traffic,
    return the last plausible bearer captured after optional home navigation + reload.
    """
    ensure_cli_logging()

    if not PLAYWRIGHT_AVAILABLE or sync_playwright is None:
        logger.warning("Playwright not installed; browser capture unavailable")
        return None

    def _attempt() -> str | None:
        logger.info(
            "Browser capture starting: portal=%s timeout=%ss",
            safe_api_url_for_log(portal_url),
            timeout_seconds,
        )
        with sync_playwright() as p:
            browser = None
            try:
                browser = p.chromium.launch(headless=False)
            except Exception as e:
                logger.warning("Chromium launch failed: %s", e)
                raise
            try:
                context = browser.new_context(ignore_https_errors=True)
                page = context.new_page()
                captured: list[str] = []

                def on_request(request: Request) -> None:
                    try:
                        if not is_graphiant_api_url(request.url):
                            return
                        tok = token_from_authorization_headers_only(request)
                        if tok is not None and eligible_capture(tok, request.url):
                            captured.append(tok)
                            logger.debug(
                                "Captured bearer from request %s",
                                safe_api_url_for_log(request.url),
                            )
                    except Exception:
                        logger.debug("on_request handler failed", exc_info=True)

                def on_response(response: Response) -> None:
                    try:
                        url = response.url
                        if not is_graphiant_api_url(url):
                            return
                        if is_auth_refresh_url(url):
                            tok = extract_token_from_refresh_response(response)
                        else:
                            tok = extract_token_from_graphiant_api_response(response)
                        if tok is not None and eligible_capture(tok, url):
                            captured.append(tok)
                            logger.debug(
                                "Captured bearer from response %s status=%s",
                                safe_api_url_for_log(url),
                                getattr(response, "status", "?"),
                            )
                    except Exception:
                        logger.debug("on_response handler failed", exc_info=True)

                context.on("request", on_request)
                context.on("response", on_response)

                try:
                    page.goto(portal_url, wait_until="domcontentloaded", timeout=60000)
                except Exception as e:
                    logger.warning("Initial page.goto failed: %s", e)
                    return None
                try:
                    page.wait_for_load_state("load", timeout=45000)
                except Exception as e:
                    logger.warning("wait_for_load_state(load) timed out or failed: %s", e)

                deadline = time.time() + timeout_seconds
                next_progress = time.time() + 25.0
                while time.time() < deadline:
                    if captured:
                        break
                    if time.time() >= next_progress:
                        if verbose:
                            print(
                                "Still waiting for a Graphiant API bearer token "
                                "(…/v1/…, …/v2/…, or …/auth/refresh) … "
                                "(sign in in Chromium; after login, refresh the portal "
                                "home page if needed — e.g. F5 or the reload button. "
                                "Press Ctrl+C to paste a token.)",
                                file=sys.stderr,
                            )
                        else:
                            print(
                                "Waiting for sign-in… (Ctrl+C to paste a token)",
                                file=sys.stderr,
                            )
                        next_progress = time.time() + 25.0
                    playwright_yield_ms(page, 250)

                if not captured:
                    for _ in range(20):
                        if captured:
                            break
                        playwright_yield_ms(page, 100)

                if not captured:
                    logger.debug(
                        "No bearer token captured within %ss (portal %s)",
                        timeout_seconds,
                        safe_api_url_for_log(portal_url),
                    )
                    return None

                logger.info(
                    "Bearer token observed from network (%d capture event(s)); navigating home",
                    len(captured),
                )
                if verbose:
                    print(
                        "Signed in. The CLI will open the home URL and reload once. "
                        "If no further API traffic appears, refresh the portal home page "
                        "yourself (F5 or reload).",
                        file=sys.stderr,
                    )
                else:
                    print("Signed in.", file=sys.stderr)

                root = portal_root_url(portal_url)
                try:
                    page.goto(root, wait_until="load", timeout=60000)
                except Exception as e:
                    logger.warning("page.goto(home) failed: %s", e)
                try:
                    page.reload(wait_until="load", timeout=60000)
                except Exception as e:
                    logger.warning("page.reload failed: %s", e)
                playwright_yield_ms(page, 500)
                out = captured[-1] if captured else None
                if out:
                    logger.info(
                        "Browser capture finished (%d capture event(s), token length=%d)",
                        len(captured),
                        len(out),
                    )
                return out
            finally:
                if browser is not None:
                    try:
                        browser.close()
                    except Exception as e:
                        logger.warning("browser.close() failed: %s", e)

    try:
        return _attempt()
    except Exception as e:
        if _launch_failure_suggests_missing_browser(e):
            logger.warning(
                "Browser missing or failed to start; attempting playwright install chromium")
            if _install_chromium():
                try:
                    return _attempt()
                except Exception as e2:
                    logger.exception("Retry after browser install failed: %s", e2)
                    return None
            logger.warning("Browser install did not help or install failed; giving up")
            return None
        logger.exception("Browser capture failed: %s", e)
        return None
