from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200 import (
    GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    address: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    interface: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["address"] = address

    params["deviceId"] = device_id

    params["interface"] = interface

    params["vrfName"] = vrf_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/device/routing/bgp/nbrs/per-afi-prefix",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    if response.status_code == 200:
        response_200 = GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    interface: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    """**API Description:**<br/> - Get BGP Neighbor Per Afi Prefix Counter

    Args:
        address (Union[Unset, str]):
        device_id (Union[Unset, str]):
        interface (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]
    """

    kwargs = _get_kwargs(
        address=address,
        device_id=device_id,
        interface=interface,
        vrf_name=vrf_name,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    interface: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    """**API Description:**<br/> - Get BGP Neighbor Per Afi Prefix Counter

    Args:
        address (Union[Unset, str]):
        device_id (Union[Unset, str]):
        interface (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]
    """

    return sync_detailed(
        client=client,
        address=address,
        device_id=device_id,
        interface=interface,
        vrf_name=vrf_name,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    interface: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    """**API Description:**<br/> - Get BGP Neighbor Per Afi Prefix Counter

    Args:
        address (Union[Unset, str]):
        device_id (Union[Unset, str]):
        interface (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]
    """

    kwargs = _get_kwargs(
        address=address,
        device_id=device_id,
        interface=interface,
        vrf_name=vrf_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    interface: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]]:
    """**API Description:**<br/> - Get BGP Neighbor Per Afi Prefix Counter

    Args:
        address (Union[Unset, str]):
        device_id (Union[Unset, str]):
        interface (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            address=address,
            device_id=device_id,
            interface=interface,
            vrf_name=vrf_name,
            authorization=authorization,
        )
    ).parsed
