"""graphiant CLI — portal login, bearer token → GRAPHIANT_ACCESS_TOKEN."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from typing import Any, Optional

import click
import typer
from rich.console import Console
from rich.json import JSON
from rich.table import Table

from graphiant_cli import __version__
from graphiant_cli.cli_logging import configure_logging, get_logger
from graphiant_cli.config_store import (
    DEFAULT_PORTAL_URL,
    DEFAULT_PROFILE,
    clear_profile,
    format_env_export_line,
    get_profile,
    load_config,
    save_config,
)
from graphiant_cli.login_common import (
    print_login_success,
    try_persist_login,
    write_export_line_to_stdout,
)
from graphiant_cli.portal_login import (
    PLAYWRIGHT_AVAILABLE,
    capture_token_via_browser,
    effective_portal_url,
    extract_token_from_paste,
    open_portal,
    portal_url_from_config,
)
from graphiant_cli.rest_client import QueryDict, request as rest_request
from graphiant_cli.sdk_invoke import invoke_method, list_api_method_rows, list_api_methods
from graphiant_sdk.exceptions import ApiException

login_logger = get_logger("login")

app = typer.Typer(
    name="graphiant",
    help="Graphiant CLI — portal login, SDK API calls, and raw REST.",
    no_args_is_help=True,
    add_completion=True,
)
configure_app = typer.Typer(help="Default API host and portal URL.")
login_app = typer.Typer(
    help=(
        "Open the portal; auto-captures bearer from Graphiant API traffic "
        "(/v1/… or auth/refresh) after login."
    ),
    invoke_without_command=True,
)
api_app = typer.Typer(help="Call DefaultApi methods or list operation names.")
app.add_typer(configure_app, name="configure")
app.add_typer(login_app, name="login")
app.add_typer(api_app, name="api")

console = Console(stderr=True)


def _is_token_expired_api_response(status: int, text: str) -> bool:
    """True when the API returns the portal-style JSON (e.g. displayError: Token Expired)."""
    if status != 403:
        return False
    try:
        obj = json.loads((text or "").strip() or "{}")
    except json.JSONDecodeError:
        return False
    if not isinstance(obj, dict):
        return False
    if obj.get("displayError") == "Token Expired":
        return True
    if obj.get("message") == "Token Expired":
        return True
    return False


def _print_token_expired_relogin_hint() -> None:
    console.print("[red]Your session token has expired.[/red]")
    console.print(
        "Run [bold]graphiant login[/bold], then load the new token into this shell, for example:\n"
        "  [cyan]source ~/.graphiant/env.sh[/cyan]\n"
        "Then retry your command."
    )


def _handle_cli_http_error(status: int, text: str) -> None:
    """Print a friendly message for token expiry, else raw HTTP error."""
    if _is_token_expired_api_response(status, text):
        _print_token_expired_relogin_hint()
    else:
        console.print(f"[red]HTTP {status}[/red]\n{text}")


def _default_host() -> str:
    cfg = load_config()
    return cfg.get("host") or os.environ.get("GRAPHIANT_API_HOST", "https://api.graphiant.com")


def _token_for_profile(profile: Optional[str]) -> tuple[str, str]:
    name = profile or os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE)
    host = _default_host()
    prof = get_profile(name)
    if prof and prof.get("host"):
        host = prof["host"]
    tok = os.environ.get("GRAPHIANT_ACCESS_TOKEN", "").strip()
    if not tok and prof:
        tok = (prof.get("access_token") or "").strip()
    return tok, host


@configure_app.command("set-host")
def configure_set_host(
    host: str = typer.Argument(..., help="API base URL, e.g. https://api.graphiant.com"),
) -> None:
    cfg = load_config()
    cfg["host"] = host.rstrip("/")
    save_config(cfg)
    console.print(f"[green]API host set to[/green] {cfg['host']}")


@configure_app.command("set-portal-url")
def configure_set_portal_url(
    url: str = typer.Argument(
        ...,
        help=f"Portal opened on login (default {DEFAULT_PORTAL_URL})",
    ),
) -> None:
    """Persist portal URL (used when you run graphiant login without --portal-url)."""
    cfg = load_config()
    cfg["portal_url"] = url.rstrip("/") + "/"
    save_config(cfg)
    console.print(f"[green]Portal URL set to[/green] {cfg['portal_url']}")


@configure_app.command("show")
def configure_show() -> None:
    """Show API host, portal URL, and profile summary."""
    cfg = load_config()
    prof = get_profile()
    console.print("[bold]API host:[/bold]", cfg.get("host") or _default_host())
    console.print("[bold]Portal URL:[/bold]", cfg.get("portal_url")
                  or portal_url_from_config().rstrip("/"))
    console.print("[bold]Profile:[/bold]", os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE))
    if prof:
        console.print("[bold]Token:[/bold]", "present" if prof.get("access_token") else "none")
    else:
        console.print("[bold]Credentials:[/bold]", "[yellow]not logged in[/yellow]")


@login_app.callback()
def login_callback(
    ctx: typer.Context,
    profile: str = typer.Option(DEFAULT_PROFILE, "--profile", "-p"),
    portal_url: Optional[str] = typer.Option(
        None,
        "--portal-url",
        help=(
            f"Graphiant portal base URL (default: {DEFAULT_PORTAL_URL} "
            "or configure set-portal-url)"
        ),
    ),
    no_browser: bool = typer.Option(False, "--no-browser", help="Do not open a browser"),
    no_capture: bool = typer.Option(
        False,
        "--no-capture",
        help="Disable automatic token capture; paste token from DevTools or enter manually",
    ),
    capture_timeout: int = typer.Option(
        90,
        "--timeout",
        "-t",
        help=(
            "Seconds to wait for API bearer capture after opening the browser "
            "(default 90; then paste prompt)"
        ),
    ),
    export_shell: bool = typer.Option(
        False,
        "--export/--no-export",
        help=(
            "After success, also print 'export GRAPHIANT_ACCESS_TOKEN=…' to stdout "
            "(for scripts/eval). Default off so the token is not echoed to the "
            "terminal; ~/.graphiant/env.sh is always written."
        ),
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help=(
            "Verbose login diagnostics on stderr (debug). "
            "Or set GRAPHIANT_LOG=debug|info|warning."
        ),
    ),
) -> None:
    if ctx.invoked_subcommand is not None:
        return

    configure_logging(verbose=verbose)
    host = _default_host()
    purl = effective_portal_url(portal_url)
    tok: Optional[str] = None

    login_logger.info(
        "Login: profile=%s api_host=%s portal=%s no_capture=%s no_browser=%s timeout=%ss",
        profile,
        host,
        purl.rstrip("/"),
        no_capture,
        no_browser,
        capture_timeout,
    )

    if not no_capture and PLAYWRIGHT_AVAILABLE and not no_browser:
        if verbose:
            console.print(
                "[dim]Complete sign-in in the [bold]Chromium[/bold] window. "
                "The CLI captures [bold]Bearer[/bold] from Graphiant "
                "[bold]…/v1/…[/bold] or [bold]…/v2/…[/bold] API calls or "
                "[bold]…/auth/refresh[/bold]. "
                "After login, refresh the home page [bold]if needed[/bold] (F5); "
                "the CLI also opens [cyan]/[/cyan] and reloads once. "
                "[bold]Ctrl+C[/bold] skips wait and prompts for a token.[/dim]"
            )
        else:
            console.print(
                "[dim]Sign in in the browser window. [bold]Ctrl+C[/bold] to paste a token.[/dim]")
        capture_interrupted = False
        try:
            tok = capture_token_via_browser(
                purl,
                timeout_seconds=capture_timeout,
                verbose=verbose,
            )
        except KeyboardInterrupt:
            capture_interrupted = True
            console.print(
                "\n[yellow]Auto-capture interrupted. Paste your token below "
                "(DevTools → Network: copy the full [cyan]Authorization[/cyan] value, "
                "including the word [cyan]Bearer[/cyan]).[/yellow]\n"
            )
            tok = None
        except Exception as e:
            login_logger.exception("Browser capture raised unexpectedly: %s", e)
            console.print(
                "[red]Browser capture failed unexpectedly.[/red] "
                "Try [cyan]graphiant login -v[/cyan] or set [cyan]GRAPHIANT_LOG=debug[/cyan].\n"
            )
            tok = None
        if tok:
            if not try_persist_login(host, tok, profile, console=console, logger=login_logger):
                raise typer.Exit(1)
            if export_shell:
                write_export_line_to_stdout(tok)
            print_login_success(console, export_shell=export_shell, verbose=verbose)
            login_logger.info("Login succeeded (browser capture)")
            return
        if not capture_interrupted:
            console.print(
                "[yellow]Auto-capture did not see a bearer token from Graphiant API "
                "traffic in time.[/yellow] "
                "Try a longer wait: [cyan]graphiant login -t 180[/cyan], complete sign-in "
                "sooner, refresh the portal home (F5), "
                "or use [cyan]graphiant login --no-capture[/cyan]. "
                "Diagnostics: [cyan]graphiant login -v[/cyan] or "
                "[cyan]GRAPHIANT_LOG=debug[/cyan].\n"
            )

    if not no_browser:
        open_portal(purl)
        console.print(f"[green]Opened portal:[/green] {purl}")
    else:
        console.print(f"[bold]Open this URL in your browser:[/bold]\n  {purl}")

    if not PLAYWRIGHT_AVAILABLE and not no_capture:
        console.print(
            "[dim]Playwright is not installed; cannot auto-capture. "
            "Install dependencies: pip install graphiant-sdk[/dim]\n"
        )

    console.print(
        "After the portal home page loads, open [bold]Developer tools[/bold] → "
        "[bold]Network[/bold], select a request to the Graphiant API "
        "([cyan]api.graphiant.com[/cyan] or your configured host), "
        "and copy the entire [bold]Authorization[/bold] request header value, "
        "including the word [cyan]Bearer[/cyan] and the token "
        "(you can also paste a raw JWT only).\n"
    )
    line = click.prompt("Authorization / token", err=True).strip()
    if not line:
        raise typer.Exit(1)
    try:
        tok = extract_token_from_paste(line)
    except ValueError as e:
        login_logger.warning("Token parse failed: %s", e)
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    if not try_persist_login(host, tok, profile, console=console, logger=login_logger):
        raise typer.Exit(1)
    if export_shell:
        write_export_line_to_stdout(tok)
    print_login_success(console, export_shell=export_shell, verbose=verbose)
    login_logger.info("Login succeeded (manual token)")


@login_app.command("env-export")
def login_env_export(profile: Optional[str] = typer.Option(None, "--profile", "-p")) -> None:
    """Print export GRAPHIANT_ACCESS_TOKEN=… for eval."""
    name = profile or os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE)
    tok = os.environ.get("GRAPHIANT_ACCESS_TOKEN", "").strip()
    prof = get_profile(name)
    if not tok and prof:
        tok = (prof.get("access_token") or "").strip()
    if not tok:
        print("graphiant: not logged in", file=sys.stderr)
        raise typer.Exit(1)
    print(format_env_export_line(tok), file=sys.stdout)


@app.command("logout")
def logout_cmd(profile: Optional[str] = typer.Option(None, "--profile", "-p")) -> None:
    name = profile or os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE)
    clear_profile(name)
    login_logger.info(
        "Logged out profile %s (clear shell with unset GRAPHIANT_ACCESS_TOKEN if needed)", name)
    console.print(f"[green]Logged out[/green] profile [bold]{name}[/bold]")
    console.print(
        "[dim]If this terminal still has a token exported, run:[/dim] "
        "[cyan]unset GRAPHIANT_ACCESS_TOKEN[/cyan]"
    )


def _print_sdk_result(result: object) -> None:
    if hasattr(result, "to_dict"):
        console.print(JSON(json.dumps(result.to_dict(), default=str)))
    elif hasattr(result, "model_dump"):
        console.print(JSON(json.dumps(result.model_dump(mode="json"), default=str)))
    else:
        console.print(JSON(json.dumps(result, default=str)))


def _run_api_invoke(
    method_name: str,
    args_json: Optional[str],
    kwargs_json: Optional[str],
    profile: Optional[str],
) -> None:
    token, host = _token_for_profile(profile)
    if not token:
        console.print("[red]Not logged in. Run [bold]graphiant login[/bold][/red]")
        raise typer.Exit(1)
    try:
        out = invoke_method(host, token, method_name, args_json, kwargs_json)
        _print_sdk_result(out)
    except ApiException as e:
        body = getattr(e, "body", None) or ""
        st = getattr(e, "status", None)
        if st is not None and _is_token_expired_api_response(int(st), str(body)):
            _print_token_expired_relogin_hint()
        else:
            console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e
    except Exception as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e


@api_app.command("invoke")
def api_invoke_cmd(
    method_name: str = typer.Argument(
        ...,
        help="DefaultApi method name, e.g. v1_auth_get, v1_edges_summary_get",
    ),
    args_json: Optional[str] = typer.Option(
        None,
        "--args",
        "-a",
        help='JSON array of positional args in parameter order, e.g. \'["Bearer …"]\'',
    ),
    kwargs_json: Optional[str] = typer.Option(
        None,
        "--kwargs",
        "-k",
        help=(
            'JSON object of keyword args (request bodies as nested objects), '
            'e.g. \'{"v1_foo_post_request": {...}}\''
        ),
    ),
    profile: Optional[str] = typer.Option(None, "--profile", "-p"),
) -> None:
    """Call a generated SDK method on DefaultApi (authorization is injected automatically)."""
    _run_api_invoke(method_name, args_json, kwargs_json, profile)


@app.command("invoke")
def invoke_alias_cmd(
    method_name: str = typer.Argument(..., help="DefaultApi method name"),
    args_json: Optional[str] = typer.Option(None, "--args", "-a"),
    kwargs_json: Optional[str] = typer.Option(None, "--kwargs", "-k"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p"),
) -> None:
    """Shorthand for [cyan]graphiant api invoke[/cyan]."""
    _run_api_invoke(method_name, args_json, kwargs_json, profile)


def _print_api_list(prefix: str, plain: bool) -> None:
    if plain:
        for m in list_api_methods(prefix):
            console.print(m)
        return
    t = Table(title="DefaultApi operations", show_header=True, header_style="bold")
    t.add_column("SDK method", style="cyan", overflow="fold")
    t.add_column("HTTP", style="green", no_wrap=True)
    t.add_column("Path", overflow="fold")
    for name, verb, path in list_api_method_rows(prefix):
        t.add_row(name, verb, path)
    console.print(t)


@api_app.command("list")
def api_list_cmd(
    prefix: str = typer.Option(
        "", "--prefix", help="Only methods starting with this prefix (e.g. v1_edges)"),
    plain: bool = typer.Option(
        False,
        "--plain",
        "-1",
        help="Print one SDK method name per line (no HTTP/path table)",
    ),
) -> None:
    """List DefaultApi method names and raw HTTP path (for graphiant api invoke)."""
    _print_api_list(prefix, plain)


@app.command("apis")
def apis_alias_cmd(
    prefix: str = typer.Option("", "--prefix"),
    plain: bool = typer.Option(False, "--plain", "-1", help="SDK method names only, one per line"),
) -> None:
    """Shorthand for [cyan]graphiant api list[/cyan]."""
    _print_api_list(prefix, plain)


@app.command("rest")
def rest_cmd(
    method: str = typer.Argument(..., help="HTTP method: GET, POST, PATCH, PUT, DELETE"),
    path: str = typer.Argument(..., help="Path starting with /v1/..."),
    body: Optional[str] = typer.Option(
        None, "--body", "-b", help="JSON body string or @file.json"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p"),
    query: Optional[str] = typer.Option(None, "--query", "-q", help="Query string a=b&c=d"),
) -> None:
    """Raw REST call with Bearer auth (path relative to API host)."""
    token, host = _token_for_profile(profile)
    if not token:
        console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)
    payload: dict[str, Any] | str | None = None
    if body:
        if body.startswith("@"):
            with open(body[1:], encoding="utf-8") as f:
                payload = json.load(f)
        else:
            try:
                payload = json.loads(body)
            except json.JSONDecodeError:
                payload = body
    qdict: QueryDict | None = None
    if query:
        qdict = {}
        for pair in query.split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                qdict[k.strip()] = v.strip()
    status, text, _ = rest_request(host, method, path, token, body=payload, query=qdict)
    if 200 <= status < 300:
        try:
            console.print(JSON(json.dumps(json.loads(text), default=str)))
        except json.JSONDecodeError:
            console.print(text)
    else:
        _handle_cli_http_error(status, text)
        raise typer.Exit(1)


def _whoami_key_is_last_active(key: str) -> bool:
    return str(key).replace("-", "_").lower() in ("lastactiveat", "last_active_at")


def _whoami_row_keys(data: dict[str, Any]) -> list[str]:
    """Alphabetical property order, with lastActiveAt (any casing) as the final row(s)."""
    last_active = sorted(k for k in data if _whoami_key_is_last_active(k))
    rest = sorted(k for k in data if k not in set(last_active))
    return rest + last_active


def _parse_unix_timestamp_value(val: Any) -> float | None:
    """Coerce protobuf JSON, JSON string, epoch int/float/str → Unix seconds (fractional)."""
    if isinstance(val, str):
        s = val.strip()
        if s.startswith("{") and "seconds" in s:
            try:
                val = json.loads(s)
            except json.JSONDecodeError:
                return None
    if isinstance(val, dict):
        raw_s = val.get("seconds")
        if raw_s is None:
            return None
        try:
            ts = float(raw_s)
        except (TypeError, ValueError):
            return None
        nanos = val.get("nanos", 0)
        try:
            ts += float(nanos) / 1e9
        except (TypeError, ValueError):
            pass
        return ts
    if isinstance(val, (int, float)):
        ts = float(val)
        if ts > 1e12:
            ts /= 1000.0
        return ts
    if isinstance(val, str):
        s = val.strip()
        if not s:
            return None
        try:
            ts = float(s)
        except ValueError:
            return None
        if ts > 1e12:
            ts /= 1000.0
        return ts
    return None


def _format_utc_time_human(val: Any) -> str | None:
    """Readable instant in UTC (Unix / protobuf timestamps are UTC-based)."""
    ts = _parse_unix_timestamp_value(val)
    if ts is None:
        return None
    try:
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    except (OSError, ValueError, OverflowError):
        return None
    base = dt.strftime("%B %d, %Y at %I:%M:%S %p")
    return f"{base} (UTC)"


def _user_display_name(user: dict[str, Any]) -> str:
    fn = (user.get("firstName") or "").strip()
    ln = (user.get("lastName") or "").strip()
    full = f"{fn} {ln}".strip()
    if full:
        return full
    email = (user.get("email") or "").strip()
    return email or "—"


def _whoami_value_cell(key: str, val: Any) -> str:
    if _whoami_key_is_last_active(key):
        human = _format_utc_time_human(val)
        if human is not None:
            return human
    if isinstance(val, dict) and "seconds" in val and set(val.keys()) <= {"seconds", "nanos"}:
        human = _format_utc_time_human(val)
        if human is not None:
            return human
    if isinstance(val, (dict, list)):
        return json.dumps(val, default=str)
    return str(val)


def _whoami_table_from_dict(title: str, caption: str, data: dict[str, Any]) -> Table:
    t = Table(title=title, caption=caption, show_header=True, header_style="bold")
    t.add_column("Property", style="cyan", overflow="fold")
    t.add_column("Value", overflow="fold")
    for key in _whoami_row_keys(data):
        t.add_row(str(key), _whoami_value_cell(key, data[key]))
    return t


def _print_whoami_tables(
    host: str,
    raw_token: str,
    auth: dict[str, Any],
) -> None:
    """Tabular output: session, permissions, and user profile (no raw JSON dump)."""
    user_id = auth.get("userId")
    ent_id = auth.get("enterpriseId")

    user_note = "—"
    user_obj: dict[str, Any] | None = None
    if user_id is not None and str(user_id).strip():
        st_u, body_u, _ = rest_request(
            host,
            "GET",
            "/v1/users",
            raw_token,
            body=None,
            query={"id": str(user_id)},
        )
        if 200 <= st_u < 300:
            try:
                uj = json.loads(body_u)
                users = uj.get("users") if isinstance(uj, dict) else None
                if isinstance(users, list) and users and isinstance(users[0], dict):
                    user_obj = users[0]
                    user_note = _user_display_name(user_obj)
                else:
                    user_note = f"(no users in response, HTTP {st_u})"
            except (json.JSONDecodeError, TypeError):
                user_note = f"(invalid JSON, HTTP {st_u})"
        else:
            user_note = f"(lookup failed HTTP {st_u})"

    extra_auth = {k: v for k, v in auth.items() if k not in ("permissions",)}
    slim = {k: v for k, v in extra_auth.items() if k not in ("userId", "enterpriseId", "timeZone")}

    session = Table(
        title="[bold]Session[/bold]",
        caption="[dim]GET /v1/auth/user (+ /v1/users for your display name)[/dim]",
        show_header=True,
        header_style="bold",
    )
    session.add_column("Property", style="cyan", no_wrap=True)
    session.add_column("Value", overflow="fold")
    session.add_row("userId", str(user_id) if user_id is not None else "—")
    session.add_row("User name", user_note)
    session.add_row("enterpriseId", str(ent_id) if ent_id is not None else "—")
    session.add_row("timeZone", str(auth.get("timeZone", "—")))
    for key in _whoami_row_keys(slim):
        session.add_row(str(key), _whoami_value_cell(key, slim[key]))
    console.print()
    console.print(session)

    perms = auth.get("permissions")
    if isinstance(perms, dict) and perms:
        pt = Table(
            title="[bold]Permissions[/bold]",
            caption="[dim]From GET /v1/auth/user[/dim]",
            show_header=True,
            header_style="bold",
        )
        pt.add_column("Permission", style="cyan")
        pt.add_column("Level")
        for pk in sorted(perms.keys()):
            pv = perms[pk]
            pt.add_row(str(pk), "—" if pv is None or pv == "" else str(pv))
        console.print()
        console.print(pt)

    if user_obj is not None:
        console.print()
        console.print(
            _whoami_table_from_dict(
                "[bold]Profile[/bold]",
                f"[dim]GET /v1/users?id={user_id}[/dim]",
                user_obj,
            )
        )


@app.command("whoami")
def whoami_cmd(profile: Optional[str] = typer.Option(None, "--profile", "-p")) -> None:
    """Show who you are: session, permissions, and profile (GET /v1/auth/user + /v1/users).

    Uses the raw REST client with a single Authorization header. The OpenAPI client
    would also apply jwtAuth (duplicate authorization header keys), which some
    gateways (e.g. Azure Application Gateway) reject with 400.
    """
    token, host = _token_for_profile(profile)
    if not token:
        console.print("[red]Not logged in. Run [bold]graphiant login[/bold][/red]")
        raise typer.Exit(1)
    raw_tok = token[7:].strip() if token.lower().startswith("bearer ") else token
    try:
        status, text, _ = rest_request(host, "GET", "/v1/auth/user",
                                       raw_tok, body=None, query=None)
        if 200 <= status < 300:
            try:
                payload = json.loads(text)
            except json.JSONDecodeError:
                console.print(text)
                return
            if isinstance(payload, dict):
                _print_whoami_tables(host, raw_tok, payload)
            else:
                console.print(JSON(json.dumps(payload, indent=2, default=str)))
        else:
            _handle_cli_http_error(status, text)
            raise typer.Exit(1)
    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e


@app.command("version")
def version_cmd() -> None:
    console.print(f"graphiant {__version__}")


def main() -> None:
    # Stable prog name for Click/Typer shell completion
    # (_GRAPHIANT_COMPLETE, --install-completion).
    app(prog_name="graphiant")


if __name__ == "__main__":
    main()
