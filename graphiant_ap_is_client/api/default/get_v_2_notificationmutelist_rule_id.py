from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_notificationmutelist_rule_id_response_200 import GetV2NotificationmutelistRuleIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rule_id: str,
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/notificationmutelist/{rule_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetV2NotificationmutelistRuleIdResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    """
    Args:
        rule_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    """
    Args:
        rule_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV2NotificationmutelistRuleIdResponse200]
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    """
    Args:
        rule_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetV2NotificationmutelistRuleIdResponse200]]:
    """
    Args:
        rule_id (str):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetV2NotificationmutelistRuleIdResponse200]
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
