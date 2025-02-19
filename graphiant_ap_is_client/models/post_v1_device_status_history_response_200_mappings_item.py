from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_device_status_history_response_200_mappings_item_event_time import (
        PostV1DeviceStatusHistoryResponse200MappingsItemEventTime,
    )


T = TypeVar("T", bound="PostV1DeviceStatusHistoryResponse200MappingsItem")


@_attrs_define
class PostV1DeviceStatusHistoryResponse200MappingsItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        enterprise_id (Union[Unset, str]):  Example: TYPE_UINT64.
        event (Union[Unset, str]):  Example: TYPE_ENUM.
        event_time (Union[Unset, PostV1DeviceStatusHistoryResponse200MappingsItemEventTime]):
        ipaddress (Union[Unset, str]):  Example: TYPE_STRING.
        tt_identity (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_id: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    event_time: Union[Unset, "PostV1DeviceStatusHistoryResponse200MappingsItemEventTime"] = UNSET
    ipaddress: Union[Unset, str] = UNSET
    tt_identity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        enterprise_id = self.enterprise_id

        event = self.event

        event_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_time, Unset):
            event_time = self.event_time.to_dict()

        ipaddress = self.ipaddress

        tt_identity = self.tt_identity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if event is not UNSET:
            field_dict["event"] = event
        if event_time is not UNSET:
            field_dict["eventTime"] = event_time
        if ipaddress is not UNSET:
            field_dict["ipaddress"] = ipaddress
        if tt_identity is not UNSET:
            field_dict["ttIdentity"] = tt_identity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_device_status_history_response_200_mappings_item_event_time import (
            PostV1DeviceStatusHistoryResponse200MappingsItemEventTime,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        event = d.pop("event", UNSET)

        _event_time = d.pop("eventTime", UNSET)
        event_time: Union[Unset, PostV1DeviceStatusHistoryResponse200MappingsItemEventTime]
        if isinstance(_event_time, Unset):
            event_time = UNSET
        else:
            event_time = PostV1DeviceStatusHistoryResponse200MappingsItemEventTime.from_dict(_event_time)

        ipaddress = d.pop("ipaddress", UNSET)

        tt_identity = d.pop("ttIdentity", UNSET)

        post_v1_device_status_history_response_200_mappings_item = cls(
            device_id=device_id,
            enterprise_id=enterprise_id,
            event=event,
            event_time=event_time,
            ipaddress=ipaddress,
            tt_identity=tt_identity,
        )

        post_v1_device_status_history_response_200_mappings_item.additional_properties = d
        return post_v1_device_status_history_response_200_mappings_item

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
