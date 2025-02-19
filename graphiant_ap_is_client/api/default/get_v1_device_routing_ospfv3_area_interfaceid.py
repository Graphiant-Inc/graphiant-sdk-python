from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_device_routing_ospfv_3_area_interfaceid_response_200 import (
    GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    area_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    instance_name: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["areaId"] = area_id

    params["deviceId"] = device_id

    params["instanceName"] = instance_name

    params["last"] = last

    params["vrfName"] = vrf_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/device/routing/ospfv3/area/interfaceid",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    if response.status_code == 200:
        response_200 = GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    area_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    instance_name: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    """**API Description:**<br/> - Get OSPFv3 Area

    Args:
        area_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        instance_name (Union[Unset, str]):
        last (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]
    """

    kwargs = _get_kwargs(
        area_id=area_id,
        device_id=device_id,
        instance_name=instance_name,
        last=last,
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
    area_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    instance_name: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    """**API Description:**<br/> - Get OSPFv3 Area

    Args:
        area_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        instance_name (Union[Unset, str]):
        last (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]
    """

    return sync_detailed(
        client=client,
        area_id=area_id,
        device_id=device_id,
        instance_name=instance_name,
        last=last,
        vrf_name=vrf_name,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    area_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    instance_name: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    """**API Description:**<br/> - Get OSPFv3 Area

    Args:
        area_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        instance_name (Union[Unset, str]):
        last (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]
    """

    kwargs = _get_kwargs(
        area_id=area_id,
        device_id=device_id,
        instance_name=instance_name,
        last=last,
        vrf_name=vrf_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    area_id: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    instance_name: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    vrf_name: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]]:
    """**API Description:**<br/> - Get OSPFv3 Area

    Args:
        area_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        instance_name (Union[Unset, str]):
        last (Union[Unset, str]):
        vrf_name (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            area_id=area_id,
            device_id=device_id,
            instance_name=instance_name,
            last=last,
            vrf_name=vrf_name,
            authorization=authorization,
        )
    ).parsed
