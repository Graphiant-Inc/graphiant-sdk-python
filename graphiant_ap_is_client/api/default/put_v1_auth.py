from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_v1_auth_body import PutV1AuthBody
from ...models.put_v1_auth_response_204 import PutV1AuthResponse204
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PutV1AuthBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/auth",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PutV1AuthResponse204]]:
    if response.status_code == 204:
        response_204 = PutV1AuthResponse204.from_dict(response.json())

        return response_204
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
) -> Response[Union[Any, PutV1AuthResponse204]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutV1AuthBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PutV1AuthResponse204]]:
    """
    Args:
        authorization (Union[Unset, str]):
        body (PutV1AuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutV1AuthResponse204]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PutV1AuthBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PutV1AuthResponse204]]:
    """
    Args:
        authorization (Union[Unset, str]):
        body (PutV1AuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutV1AuthResponse204]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutV1AuthBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PutV1AuthResponse204]]:
    """
    Args:
        authorization (Union[Unset, str]):
        body (PutV1AuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutV1AuthResponse204]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PutV1AuthBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PutV1AuthResponse204]]:
    """
    Args:
        authorization (Union[Unset, str]):
        body (PutV1AuthBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutV1AuthResponse204]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
