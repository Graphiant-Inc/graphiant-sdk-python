from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_alarms_response_200 import GetV1AlarmsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    first: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["after"] = after

    params["before"] = before

    params["first"] = first

    params["last"] = last

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alarms",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV1AlarmsResponse200]]:
    if response.status_code == 200:
        response_200 = GetV1AlarmsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV1AlarmsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    first: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1AlarmsResponse200]]:
    """
    Args:
        after (Union[Unset, str]):
        before (Union[Unset, str]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1AlarmsResponse200]]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        first=first,
        last=last,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    first: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1AlarmsResponse200]]:
    """
    Args:
        after (Union[Unset, str]):
        before (Union[Unset, str]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1AlarmsResponse200]
    """

    return sync_detailed(
        client=client,
        after=after,
        before=before,
        first=first,
        last=last,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    first: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV1AlarmsResponse200]]:
    """
    Args:
        after (Union[Unset, str]):
        before (Union[Unset, str]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV1AlarmsResponse200]]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        first=first,
        last=last,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    first: Union[Unset, str] = UNSET,
    last: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV1AlarmsResponse200]]:
    """
    Args:
        after (Union[Unset, str]):
        before (Union[Unset, str]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV1AlarmsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            before=before,
            first=first,
            last=last,
            authorization=authorization,
        )
    ).parsed
