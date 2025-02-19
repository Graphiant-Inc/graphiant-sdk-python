from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_extranet_log_details_response_200_logs_item_ts import (
        PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs,
    )


T = TypeVar("T", bound="PostV2MonitoringExtranetLogDetailsResponse200LogsItem")


@_attrs_define
class PostV2MonitoringExtranetLogDetailsResponse200LogsItem:
    """
    Attributes:
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        reason (Union[Unset, str]):  Example: TYPE_STRING.
        server_address (Union[Unset, str]):  Example: TYPE_STRING.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        ts (Union[Unset, PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs]):
    """

    hostname: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    server_address: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        reason = self.reason

        server_address = self.server_address

        site_name = self.site_name

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if reason is not UNSET:
            field_dict["reason"] = reason
        if server_address is not UNSET:
            field_dict["serverAddress"] = server_address
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_extranet_log_details_response_200_logs_item_ts import (
            PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs,
        )

        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        reason = d.pop("reason", UNSET)

        server_address = d.pop("serverAddress", UNSET)

        site_name = d.pop("siteName", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2MonitoringExtranetLogDetailsResponse200LogsItemTs.from_dict(_ts)

        post_v2_monitoring_extranet_log_details_response_200_logs_item = cls(
            hostname=hostname,
            reason=reason,
            server_address=server_address,
            site_name=site_name,
            ts=ts,
        )

        post_v2_monitoring_extranet_log_details_response_200_logs_item.additional_properties = d
        return post_v2_monitoring_extranet_log_details_response_200_logs_item

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
