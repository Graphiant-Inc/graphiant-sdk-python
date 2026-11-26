"""Tests for ApiClient array query-param serialization (QA-13519).

openapi-generator's Python templates don't support ``style: deepObject`` for
array query params: they type them as ``List[List[...]]`` and mark them
``csv``. The backend only accepts indexed-bracket keys (``k[0]=a&k[1]=b``),
the same format the Go SDK sends.
"""

from unittest import mock

from graphiant_sdk import ApiClient, Configuration, DefaultApi


def _client() -> ApiClient:
    return ApiClient(Configuration(host="http://localhost"))


def test_csv_list_of_list_single_value_is_indexed() -> None:
    query = _client().parameters_to_url_query(
        [("enterpriseIds", [[10000000335]])], {"enterpriseIds": "csv"}
    )
    assert query == "enterpriseIds[0]=10000000335"


def test_csv_list_of_list_multiple_values_are_indexed_in_order() -> None:
    query = _client().parameters_to_url_query(
        [("deviceIds", [[30000058487, 30000058486]])], {"deviceIds": "csv"}
    )
    assert query == "deviceIds[0]=30000058487&deviceIds[1]=30000058486"


def test_csv_list_of_list_string_values_are_quoted() -> None:
    query = _client().parameters_to_url_query(
        [("vrfNames", [["default", "vrf a/b"]])], {"vrfNames": "csv"}
    )
    assert query == "vrfNames[0]=default&vrfNames[1]=vrf%20a/b"


def test_multiple_array_params_in_one_request() -> None:
    query = _client().parameters_to_url_query(
        [("lanSegmentIds", [[1, 2]]), ("siteIds", [[7]])],
        {"lanSegmentIds": "csv", "siteIds": "csv"},
    )
    assert query == "lanSegmentIds[0]=1&lanSegmentIds[1]=2&siteIds[0]=7"


def test_tuple_inner_sequence_is_indexed() -> None:
    query = _client().parameters_to_url_query(
        [("protocols", [("static", "bgp")])], {"protocols": "csv"}
    )
    assert query == "protocols[0]=static&protocols[1]=bgp"


def test_flat_csv_list_is_unchanged() -> None:
    query = _client().parameters_to_url_query(
        [("ids", [1, 2, 3])], {"ids": "csv"}
    )
    assert query == "ids=1,2,3"


def test_multi_and_other_formats_are_unchanged() -> None:
    client = _client()
    assert client.parameters_to_url_query(
        [("ids", [1, 2])], {"ids": "multi"}
    ) == "ids=1&ids=2"
    assert client.parameters_to_url_query(
        [("ids", [1, 2])], {"ids": "pipes"}
    ) == "ids=1|2"


def test_scalar_and_unformatted_params_are_unchanged() -> None:
    query = _client().parameters_to_url_query(
        [("enterpriseId", 5), ("showExcluded", True), ("lanSegmentIds[0]", 9)],
        {},
    )
    assert query == "enterpriseId=5&showExcluded=true&lanSegmentIds[0]=9"


def test_generated_method_sends_indexed_query_string() -> None:
    """End-to-end through the generated v1_enterprises_get serializer."""
    api = DefaultApi(_client())
    _method, url, _headers, _body, _post = api._v1_enterprises_get_serialize(
        authorization="Bearer t",
        enterprise_ids=[[10000000335, 10000000336]],
        _request_auth=None,
        _content_type=None,
        _headers=None,
        _host_index=0,
    )
    assert url.endswith(
        "/v1/enterprises?enterpriseIds[0]=10000000335&enterpriseIds[1]=10000000336"
    )


def test_generated_method_sends_request_with_indexed_query() -> None:
    client = _client()
    api = DefaultApi(client)
    response = mock.Mock(
        status=200,
        data=b'{"enterprises": []}',
        reason="OK",
        headers={"content-type": "application/json"},
    )
    response.getheader.return_value = "application/json"
    with mock.patch.object(client.rest_client, "request", return_value=response) as req:
        api.v1_enterprises_get(authorization="Bearer t", enterprise_ids=[[42]])
    assert req.call_args.args[1].endswith("/v1/enterprises?enterpriseIds[0]=42")
