from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_logs_response_200_logs_item_ts import PostV1LogsResponse200LogsItemTs


T = TypeVar("T", bound="PostV1LogsResponse200LogsItem")


@_attrs_define
class PostV1LogsResponse200LogsItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        facility (Union[Unset, str]):  Example: TYPE_STRING.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        level (Union[Unset, str]):  Example: TYPE_ENUM.
        message (Union[Unset, str]):  Example: TYPE_STRING.
        ts (Union[Unset, PostV1LogsResponse200LogsItemTs]):
    """

    device_id: Union[Unset, str] = UNSET
    facility: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1LogsResponse200LogsItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        facility = self.facility

        hostname = self.hostname

        level = self.level

        message = self.message

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if facility is not UNSET:
            field_dict["facility"] = facility
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_logs_response_200_logs_item_ts import PostV1LogsResponse200LogsItemTs

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        facility = d.pop("facility", UNSET)

        hostname = d.pop("hostname", UNSET)

        level = d.pop("level", UNSET)

        message = d.pop("message", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1LogsResponse200LogsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1LogsResponse200LogsItemTs.from_dict(_ts)

        post_v1_logs_response_200_logs_item = cls(
            device_id=device_id,
            facility=facility,
            hostname=hostname,
            level=level,
            message=message,
            ts=ts,
        )

        post_v1_logs_response_200_logs_item.additional_properties = d
        return post_v1_logs_response_200_logs_item

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
