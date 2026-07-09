"""Tests for SDK method listing (no live API calls)."""

from typing import Optional

from graphiant_cli.sdk_invoke import _coerce_value, list_api_method_rows, list_api_methods
from graphiant_sdk.models.v1_global_content_filters_post_request import (
    V1GlobalContentFiltersPostRequest,
)


def test_list_api_methods_includes_auth_get() -> None:
    names = list_api_methods("v1_auth_")
    assert "v1_auth_get" in names
    assert "v1_auth_get_with_http_info" not in names


def test_list_api_methods_prefix_filter() -> None:
    edges = list_api_methods("v1_edges_summary")
    assert "v1_edges_summary_get" in edges


def test_list_api_method_rows_includes_raw_http() -> None:
    rows = {name: (verb, path) for name, verb, path in list_api_method_rows("v1_edges_summary")}
    assert rows["v1_edges_summary_get"] == ("GET", "/v1/edges-summary")
    assert rows["v1_edges_summary_post"][0] == "POST"


def test_list_api_methods_includes_global_content_filters() -> None:
    names = list_api_methods("v1_global_content_filters")
    assert "v1_global_content_filters_get" in names
    assert "v1_global_content_filters_post" in names


def test_list_api_method_rows_global_content_filters_and_rollouts() -> None:
    rows = {n: (v, p) for n, v, p in list_api_method_rows("v1_global_content_filters")}
    assert rows["v1_global_content_filters_get"] == ("GET", "/v1/global/content-filters")
    assert rows["v1_global_content_filters_post"][0] == "POST"
    roll = {n: (v, p) for n, v, p in list_api_method_rows("v1_software_rollouts")}
    assert roll["v1_software_rollouts_get"] == ("GET", "/v1/software/rollouts")
    macsec = {n: (v, p) for n, v, p in list_api_method_rows(
        "v2_monitoring_macsec_device_id_status")}
    assert macsec["v2_monitoring_macsec_device_id_status_get"] == (
        "GET",
        "/v2/monitoring/macsec/{deviceId}/status",
    )


def test_coerce_optional_request_model_from_dict() -> None:
    """CLI --kwargs JSON dicts become Pydantic bodies (incl. Optional[Model] params)."""
    ann = Optional[V1GlobalContentFiltersPostRequest]
    out = _coerce_value({}, ann)
    assert isinstance(out, V1GlobalContentFiltersPostRequest)
    out2 = _coerce_value(None, ann)
    assert out2 is None


def test_coerce_request_model_non_optional() -> None:
    out = _coerce_value({}, V1GlobalContentFiltersPostRequest)
    assert isinstance(out, V1GlobalContentFiltersPostRequest)
