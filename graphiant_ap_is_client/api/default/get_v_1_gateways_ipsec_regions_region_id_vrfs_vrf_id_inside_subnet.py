from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_gateways_ipsec_regions_region_id_vrfs_vrf_id_inside_subnet_response_200 import (
    GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region_id: str,
    vrf_id: str,
    *,
    address_family: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["addressFamily"] = address_family

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/gateways/ipsec/regions/{region_id}/vrfs/{vrf_id}/inside-subnet",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    if response.status_code == 200:
        response_200 = GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    address_family: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    """**API Description:**<br/> - Get the IPv4/Ipv6 Overlay Subnet for an ipsec gateway

    Args:
        region_id (str):
        vrf_id (str):
        address_family (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        vrf_id=vrf_id,
        address_family=address_family,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    address_family: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    """**API Description:**<br/> - Get the IPv4/Ipv6 Overlay Subnet for an ipsec gateway

    Args:
        region_id (str):
        vrf_id (str):
        address_family (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]
    """

    return sync_detailed(
        region_id=region_id,
        vrf_id=vrf_id,
        client=client,
        address_family=address_family,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    region_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    address_family: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    """**API Description:**<br/> - Get the IPv4/Ipv6 Overlay Subnet for an ipsec gateway

    Args:
        region_id (str):
        vrf_id (str):
        address_family (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        vrf_id=vrf_id,
        address_family=address_family,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    address_family: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]]:
    """**API Description:**<br/> - Get the IPv4/Ipv6 Overlay Subnet for an ipsec gateway

    Args:
        region_id (str):
        vrf_id (str):
        address_family (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            vrf_id=vrf_id,
            client=client,
            address_family=address_family,
            authorization=authorization,
        )
    ).parsed
