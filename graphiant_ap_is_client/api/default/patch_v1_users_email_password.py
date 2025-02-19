from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_v1_users_email_password_body import PatchV1UsersEmailPasswordBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    email: str,
    *,
    body: PatchV1UsersEmailPasswordBody,
    token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/users/{email}/password",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
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
    email: str,
    *,
    client: AuthenticatedClient,
    body: PatchV1UsersEmailPasswordBody,
    token: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        email (str):
        token (Union[Unset, str]):
        body (PatchV1UsersEmailPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        body=body,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    body: PatchV1UsersEmailPasswordBody,
    token: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        email (str):
        token (Union[Unset, str]):
        body (PatchV1UsersEmailPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        body=body,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
