"""Tests for portal URL resolution and token extraction."""

import pytest

from graphiant_cli.config_store import DEFAULT_PORTAL_URL
from graphiant_cli.portal_login import (
    effective_portal_url,
    extract_token_from_graphiant_api_response,
    extract_token_from_paste,
    extract_token_from_refresh_json,
    extract_token_from_refresh_response,
    extract_token_from_url,
    portal_root_url,
    _eligible_capture,
    _is_auth_refresh_url,
    _is_graphiant_api_url,
    _is_plausible_access_token,
    _url_ignored_for_bearer_capture,
)


def test_default_portal_constant() -> None:
    assert DEFAULT_PORTAL_URL == "https://portal.graphiant.com/"


def test_portal_root_url() -> None:
    assert portal_root_url(
        "https://portal.graphiant.com/foo/bar") == "https://portal.graphiant.com/"
    assert portal_root_url("https://portal.example.com") == "https://portal.example.com/"


def test_effective_portal_url_override() -> None:
    assert effective_portal_url("https://example.com/path").startswith("https://example.com/path/")


def test_effective_portal_url_none_uses_config_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "graphiant_cli.portal_login.load_config",
        lambda: {},
    )
    assert effective_portal_url(None) == "https://portal.graphiant.com/"


def test_extract_ssotoken_from_url() -> None:
    u = "https://portal.graphiant.com/?ssotoken=eyJhbGciOiJIUzI1NiJ9.abc"
    assert extract_token_from_url(u) == "eyJhbGciOiJIUzI1NiJ9.abc"


def test_extract_token_from_paste_url() -> None:
    url = "https://portal.graphiant.com/?ssotoken=eyJ.a.b"
    assert extract_token_from_paste(url) == "eyJ.a.b"


def test_extract_bearer() -> None:
    assert extract_token_from_paste("Bearer eyJ.x.y") == "eyJ.x.y"


def test_extract_raw_jwt() -> None:
    t = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.sig"
    assert extract_token_from_paste(t) == t


def test_extract_token_from_refresh_json_authorization() -> None:
    assert (
        extract_token_from_refresh_json({"authorization": "Bearer eyJ.tok.en"})
        == "eyJ.tok.en"
    )
    assert extract_token_from_refresh_json({"Authorization": "Bearer eyJ.alt"}) == "eyJ.alt"
    assert extract_token_from_refresh_json({"authorization": "gr-auth-abc"}) == "gr-auth-abc"


def test_extract_token_from_refresh_json_token_field() -> None:
    assert extract_token_from_refresh_json({"token": "gr-auth-xyz", "auth": True}) == "gr-auth-xyz"


def test_extract_token_from_refresh_json_access_token_aliases() -> None:
    assert extract_token_from_refresh_json({"accessToken": "tok-a"}) == "tok-a"
    assert extract_token_from_refresh_json({"access_token": "tok-b"}) == "tok-b"


def test_extract_token_from_refresh_response_entry_point_uses_request_header() -> None:
    """OpenAPI oneOf: refresh may return only entryPoint; bearer on the request."""

    class _Req:
        headers = {"authorization": "Bearer gr-auth-from-req"}

    class _Resp:
        url = "https://api.example.com/v1/auth/refresh"
        status = 200
        headers: dict[str, str] = {}
        request = _Req()

        def json(self) -> dict:
            return {"entryPoint": "/dashboard"}

    assert extract_token_from_refresh_response(_Resp()) == "gr-auth-from-req"


def test_extract_token_from_refresh_response_response_header() -> None:
    class _Resp:
        url = "https://api.example.com/v1/auth/refresh"
        status = 200
        headers = {"authorization": "Bearer gr-auth-from-resp"}
        request = None

        def json(self) -> dict:
            return {"entryPoint": "/dashboard"}

    assert extract_token_from_refresh_response(_Resp()) == "gr-auth-from-resp"


def test_is_auth_refresh_url_any_host() -> None:
    assert _is_auth_refresh_url("https://api.graphiant.com/v1/auth/refresh?currentPath=%2F")
    assert _is_auth_refresh_url("https://other-region.example/v1/auth/refresh?x=1")
    assert _is_auth_refresh_url("https://api.example.com/api/v1/auth/refresh?currentPath=%2F")
    assert not _is_auth_refresh_url("https://api.graphiant.com/v1/auth/session")


def test_is_plausible_access_token_rejects_placeholders() -> None:
    assert not _is_plausible_access_token("null")
    assert not _is_plausible_access_token("undefined")
    assert not _is_plausible_access_token("Bearer null"[7:])
    long_tok = "gr-auth-" + "a" * 40
    assert _is_plausible_access_token(long_tok)


def test_url_ignored_for_bearer_capture_login_pre() -> None:
    assert _url_ignored_for_bearer_capture("https://api.graphiant.com/v1/auth/login/pre")
    assert not _url_ignored_for_bearer_capture("https://api.graphiant.com/v1/auth/refresh")


def test_eligible_capture_combines_plausible_and_url() -> None:
    assert not _eligible_capture("null", "https://api.graphiant.com/v1/auth/login/pre")
    assert not _eligible_capture("null", "https://api.graphiant.com/v1/edges-summary")
    tok = "gr-auth-" + "x" * 40
    assert _eligible_capture(tok, "https://api.graphiant.com/v1/edges-summary")
    assert not _eligible_capture(tok, "https://api.graphiant.com/v1/auth/login/pre")


def test_is_graphiant_api_url() -> None:
    assert _is_graphiant_api_url("https://api.graphiant.com/v1/edges-summary")
    assert _is_graphiant_api_url("https://api.graphiant.com/v2/edges/summary")
    assert _is_graphiant_api_url("https://api.graphiant.com/v1/auth/refresh?x=1")
    assert _is_graphiant_api_url("https://reg.example.com/api/v1/auth/refresh")
    assert not _is_graphiant_api_url("https://portal.graphiant.com/assets/main.js")
    assert _is_graphiant_api_url("https://api.graphiant.com/v2/edges")


def test_extract_token_from_graphiant_api_response_headers_only() -> None:
    class _Req:
        headers = {"authorization": "Bearer tok-from-req"}

    class _Resp:
        url = "https://api.graphiant.com/v1/edges-summary"
        status = 200
        headers: dict[str, str] = {}
        request = _Req()

        def json(self) -> dict:
            return {"token": "wrong-not-used"}

    assert extract_token_from_graphiant_api_response(_Resp()) == "tok-from-req"


def test_extract_token_from_graphiant_api_response_ignores_non_2xx() -> None:
    class _Resp:
        url = "https://api.graphiant.com/v1/foo"
        status = 401
        headers: dict[str, str] = {}
        request = None

    assert extract_token_from_graphiant_api_response(_Resp()) is None
