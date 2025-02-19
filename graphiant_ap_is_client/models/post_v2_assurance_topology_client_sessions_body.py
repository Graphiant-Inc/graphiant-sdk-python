from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_client_sessions_body_filter import (
        PostV2AssuranceTopologyClientSessionsBodyFilter,
    )
    from ..models.post_v2_assurance_topology_client_sessions_body_time_window import (
        PostV2AssuranceTopologyClientSessionsBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionsBody")


@_attrs_define
class PostV2AssuranceTopologyClientSessionsBody:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        app_server_key (Union[Unset, str]):  Example: TYPE_STRING.
        bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        filter_ (Union[Unset, PostV2AssuranceTopologyClientSessionsBodyFilter]):
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        time_window (Union[Unset, PostV2AssuranceTopologyClientSessionsBodyTimeWindow]):
    """

    app_name: Union[Unset, str] = UNSET
    app_server_key: Union[Unset, str] = UNSET
    bucket_id: Union[Unset, str] = UNSET
    client_ip: Union[Unset, str] = UNSET
    filter_: Union[Unset, "PostV2AssuranceTopologyClientSessionsBodyFilter"] = UNSET
    site_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2AssuranceTopologyClientSessionsBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        app_server_key = self.app_server_key

        bucket_id = self.bucket_id

        client_ip = self.client_ip

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        site_id = self.site_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if app_server_key is not UNSET:
            field_dict["appServerKey"] = app_server_key
        if bucket_id is not UNSET:
            field_dict["bucketId"] = bucket_id
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_client_sessions_body_filter import (
            PostV2AssuranceTopologyClientSessionsBodyFilter,
        )
        from ..models.post_v2_assurance_topology_client_sessions_body_time_window import (
            PostV2AssuranceTopologyClientSessionsBodyTimeWindow,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        app_server_key = d.pop("appServerKey", UNSET)

        bucket_id = d.pop("bucketId", UNSET)

        client_ip = d.pop("clientIp", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV2AssuranceTopologyClientSessionsBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV2AssuranceTopologyClientSessionsBodyFilter.from_dict(_filter_)

        site_id = d.pop("siteId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceTopologyClientSessionsBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceTopologyClientSessionsBodyTimeWindow.from_dict(_time_window)

        post_v2_assurance_topology_client_sessions_body = cls(
            app_name=app_name,
            app_server_key=app_server_key,
            bucket_id=bucket_id,
            client_ip=client_ip,
            filter_=filter_,
            site_id=site_id,
            time_window=time_window,
        )

        post_v2_assurance_topology_client_sessions_body.additional_properties = d
        return post_v2_assurance_topology_client_sessions_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
