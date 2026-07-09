"""Parse bearer tokens from paste text, JSON, HTTP headers, and Graphiant API URLs."""

from __future__ import annotations

import json
import re
from urllib.parse import parse_qs, urlparse, urlunparse

from graphiant_cli.cli_logging import get_logger, safe_api_url_for_log

logger = get_logger("token_parsing")

# Minimum length for opaque/JWT-like session tokens (rejects "null", "Bearer null", etc.)
MIN_ACCESS_TOKEN_LEN = 12

_PLACEHOLDER_TOKENS = frozenset(
    {"null", "undefined", "none", "true", "false"},
)


def portal_root_url(portal_url: str) -> str:
    """Root landing URL (``https://host/``) used to load the home SPA after sign-in."""
    raw = portal_url.strip()
    p = urlparse(raw if "://" in raw else f"https://{raw.lstrip('/')}")
    if not p.netloc:
        p = urlparse(f"https://{raw}")
    scheme = p.scheme or "https"
    return urlunparse((scheme, p.netloc, "/", "", "", ""))


def extract_token_from_paste(text: str) -> str:
    """Accept ``Bearer …``, Authorization-style value, portal URL with ssotoken, or raw JWT."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    if text.startswith("Bearer "):
        return text[7:].strip()
    if "ssotoken=" in text.lower():
        if not text.startswith(("http://", "https://")):
            text = "https://dummy?" + text.split("?", 1)[-1] if "?" in text else text
        parsed = urlparse(text)
        qs = parse_qs(parsed.query)
        for key in ("ssotoken", "ssoToken", "SSOTOKEN"):
            if key in qs and qs[key][0]:
                return qs[key][0].strip()
    if re.match(r"^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$", text):
        return text
    raise ValueError(
        "Could not parse token. From DevTools → Network, copy the full Authorization header value "
        "(including the word Bearer) and paste it here, or paste a raw JWT."
    )


def extract_token_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    for key in ("ssotoken", "ssoToken", "SSOTOKEN"):
        if key in qs and qs[key][0]:
            return qs[key][0].strip()
    return None


def extract_token_from_refresh_json(data: object) -> str | None:
    """Parse ``…/auth/refresh`` JSON: ``authorization`` / ``token`` / ``accessToken``."""
    if not isinstance(data, dict):
        return None
    auth = data.get("authorization") or data.get("Authorization")
    if isinstance(auth, str) and auth.strip():
        v = auth.strip()
        if v.lower().startswith("bearer "):
            return v[7:].strip()
        return v
    for key in ("token", "accessToken", "access_token"):
        tok = data.get(key)
        if isinstance(tok, str) and tok.strip():
            return tok.strip()
    return None


def normalize_bearer_value(value: str | None) -> str | None:
    if not value or not isinstance(value, str):
        return None
    v = value.strip()
    if v.lower().startswith("bearer "):
        return v[7:].strip()
    return v


def bearer_from_header_map(headers: object) -> str | None:
    if not isinstance(headers, dict):
        return None
    for k, v in headers.items():
        if str(k).lower() == "authorization" and isinstance(v, str):
            return normalize_bearer_value(v)
    return None


def is_plausible_access_token(tok: str) -> bool:
    """Reject placeholders (e.g. ``Bearer null`` on ``/auth/login/pre``)."""
    if not isinstance(tok, str):
        return False
    s = tok.strip()
    if len(s) < MIN_ACCESS_TOKEN_LEN:
        return False
    if s.lower() in _PLACEHOLDER_TOKENS:
        return False
    return True


def url_ignored_for_bearer_capture(url: str) -> bool:
    """Pre-login URLs that may carry non-session Authorization values."""
    try:
        path = urlparse(url).path.lower()
        if "/auth/login/pre" in path:
            return True
    except Exception:
        pass
    return False


def eligible_capture(tok: str | None, url: str) -> bool:
    """Whether ``tok`` should be stored as a session bearer for this ``url``."""
    if not tok or not is_plausible_access_token(tok):
        return False
    if url_ignored_for_bearer_capture(url):
        logger.debug("Ignoring bearer from pre-login URL %s", safe_api_url_for_log(url))
        return False
    return True


def extract_token_from_refresh_response(response: object) -> str | None:
    """Bearer from refresh: JSON body, then response/request ``Authorization`` headers."""
    try:
        status = getattr(response, "status", None)
        if status is not None and (status < 200 or status >= 300):
            return None
    except Exception:
        pass

    try:
        json_fn = getattr(response, "json", None)
        if callable(json_fn):
            data = json_fn()
            if isinstance(data, dict):
                tok = extract_token_from_refresh_json(data)
                if tok:
                    return tok
    except Exception:
        try:
            body_fn = getattr(response, "body", None)
            if callable(body_fn):
                raw = body_fn()
                if raw:
                    data = json.loads(raw.decode("utf-8", errors="replace"))
                    if isinstance(data, dict):
                        tok = extract_token_from_refresh_json(data)
                        if tok:
                            return tok
        except Exception:
            pass

    try:
        tok = bearer_from_header_map(getattr(response, "headers", None))
        if tok:
            return tok
    except Exception:
        pass

    try:
        req = getattr(response, "request", None)
        if req is not None:
            tok = bearer_from_header_map(getattr(req, "headers", None))
            if tok:
                return tok
    except Exception:
        pass

    return None


def token_from_authorization_headers_only(message: object) -> str | None:
    try:
        return bearer_from_header_map(getattr(message, "headers", None))
    except Exception:
        return None


def extract_token_from_graphiant_api_response(response: object) -> str | None:
    """Non-refresh API response: ``Authorization`` on response or linked request only."""
    try:
        status = getattr(response, "status", None)
        if status is not None and (status < 200 or status >= 300):
            return None
    except Exception:
        pass
    tok = token_from_authorization_headers_only(response)
    if tok:
        return tok
    try:
        req = getattr(response, "request", None)
        if req is not None:
            return token_from_authorization_headers_only(req)
    except Exception:
        pass
    return None


def is_graphiant_api_url(url: str) -> bool:
    """REST-like path: ``/v1/``, ``/v2/``, or ``…/auth/refresh``."""
    try:
        path = urlparse(url).path or ""
        if "/v1/" in path or "/v2/" in path:
            return True
        p = path.rstrip("/")
        if p.endswith("/auth/refresh"):
            return True
    except Exception:
        pass
    u = url.lower()
    return "/v1/" in u or "/v2/" in u


def is_auth_refresh_url(url: str) -> bool:
    try:
        path = urlparse(url).path.rstrip("/")
        if path.endswith("/auth/refresh"):
            return True
    except Exception:
        pass
    return "/v1/auth/refresh" in url
