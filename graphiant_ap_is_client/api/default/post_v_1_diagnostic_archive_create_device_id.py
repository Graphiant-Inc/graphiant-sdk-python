from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v1_diagnostic_archive_create_device_id_body import PostV1DiagnosticArchiveCreateDeviceIdBody
from ...models.post_v1_diagnostic_archive_create_device_id_response_201 import (
    PostV1DiagnosticArchiveCreateDeviceIdResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    device_id: str,
    *,
    body: PostV1DiagnosticArchiveCreateDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/diagnostic/archive-create/{device_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
    if response.status_code == 201:
        response_201 = PostV1DiagnosticArchiveCreateDeviceIdResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
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
    body: PostV1DiagnosticArchiveCreateDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
    """**API Description:**<br/> - Create a device debug archive

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PostV1DiagnosticArchiveCreateDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]
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


def sync(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1DiagnosticArchiveCreateDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
    """**API Description:**<br/> - Create a device debug archive

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PostV1DiagnosticArchiveCreateDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]
    """

    return sync_detailed(
        device_id=device_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1DiagnosticArchiveCreateDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
    """**API Description:**<br/> - Create a device debug archive

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PostV1DiagnosticArchiveCreateDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1DiagnosticArchiveCreateDeviceIdBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]]:
    """**API Description:**<br/> - Create a device debug archive

    Args:
        device_id (str):
        authorization (Union[Unset, str]):
        body (PostV1DiagnosticArchiveCreateDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostV1DiagnosticArchiveCreateDeviceIdResponse201]
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
