from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_lldp_interface_id_neighbors_response_200 import GetV1LldpInterfaceIdNeighborsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    interface_id: str,
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/lldp/{interface_id}/neighbors",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    if response.status_code == 200:
        response_200 = GetV1LldpInterfaceIdNeighborsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    interface_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    """**API Description:**<br/> - Get the LLDP neighbors for an interface and optionally for a specific
    vendor

    Args:
        interface_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]
    """

    kwargs = _get_kwargs(
        interface_id=interface_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interface_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    """**API Description:**<br/> - Get the LLDP neighbors for an interface and optionally for a specific
    vendor

    Args:
        interface_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]
    """

    return sync_detailed(
        interface_id=interface_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    interface_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    """**API Description:**<br/> - Get the LLDP neighbors for an interface and optionally for a specific
    vendor

    Args:
        interface_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]
    """

    kwargs = _get_kwargs(
        interface_id=interface_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interface_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]]:
    """**API Description:**<br/> - Get the LLDP neighbors for an interface and optionally for a specific
    vendor

    Args:
        interface_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1LldpInterfaceIdNeighborsResponse200]
    """

    return (
        await asyncio_detailed(
            interface_id=interface_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
