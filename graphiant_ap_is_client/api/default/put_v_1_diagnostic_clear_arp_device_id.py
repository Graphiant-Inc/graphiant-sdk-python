from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_v1_diagnostic_clear_arp_device_id_body import PutV1DiagnosticClearArpDeviceIdBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    device_id: str,
    *,
    body: PutV1DiagnosticClearArpDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/diagnostic/clear-arp/{device_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 500:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: PutV1DiagnosticClearArpDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """**API Description:**<br/> - Clear arp entries

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PutV1DiagnosticClearArpDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: PutV1DiagnosticClearArpDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """**API Description:**<br/> - Clear arp entries

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PutV1DiagnosticClearArpDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
