from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v2_monitoring_circuitsummary_circuit_name_body import PostV2MonitoringCircuitsummaryCircuitNameBody
from ...models.post_v2_monitoring_circuitsummary_circuit_name_response_200 import (
    PostV2MonitoringCircuitsummaryCircuitNameResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    circuit_name: str,
    *,
    body: PostV2MonitoringCircuitsummaryCircuitNameBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v2/monitoring/circuitsummary/{circuit_name}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    if response.status_code == 200:
        response_200 = PostV2MonitoringCircuitsummaryCircuitNameResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    circuit_name: str,
    *,
    client: AuthenticatedClient,
    body: PostV2MonitoringCircuitsummaryCircuitNameBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    """
    Args:
        circuit_name (str):
        authorization (Union[Unset, str]):
        body (PostV2MonitoringCircuitsummaryCircuitNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]
    """

    kwargs = _get_kwargs(
        circuit_name=circuit_name,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    circuit_name: str,
    *,
    client: AuthenticatedClient,
    body: PostV2MonitoringCircuitsummaryCircuitNameBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    """
    Args:
        circuit_name (str):
        authorization (Union[Unset, str]):
        body (PostV2MonitoringCircuitsummaryCircuitNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]
    """

    return sync_detailed(
        circuit_name=circuit_name,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    circuit_name: str,
    *,
    client: AuthenticatedClient,
    body: PostV2MonitoringCircuitsummaryCircuitNameBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    """
    Args:
        circuit_name (str):
        authorization (Union[Unset, str]):
        body (PostV2MonitoringCircuitsummaryCircuitNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]
    """

    kwargs = _get_kwargs(
        circuit_name=circuit_name,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    circuit_name: str,
    *,
    client: AuthenticatedClient,
    body: PostV2MonitoringCircuitsummaryCircuitNameBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]]:
    """
    Args:
        circuit_name (str):
        authorization (Union[Unset, str]):
        body (PostV2MonitoringCircuitsummaryCircuitNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostV2MonitoringCircuitsummaryCircuitNameResponse200]
    """

    return (
        await asyncio_detailed(
            circuit_name=circuit_name,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
