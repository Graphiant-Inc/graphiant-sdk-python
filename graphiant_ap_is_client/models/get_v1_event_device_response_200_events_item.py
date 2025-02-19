from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_event_device_response_200_events_item_event_time import (
        GetV1EventDeviceResponse200EventsItemEventTime,
    )


T = TypeVar("T", bound="GetV1EventDeviceResponse200EventsItem")


@_attrs_define
class GetV1EventDeviceResponse200EventsItem:
    """
    Attributes:
        actions (Union[Unset, list[str]]):  Example: ['UIUpdate'].
        device_id (Union[Unset, str]):  Example: 30000000001.
        enterprise_id (Union[Unset, str]):  Example: 30000000001.
        event_data (Union[Unset, str]):  Example: InterfaceOperStateChange.
        event_id (Union[Unset, str]):  Example: 30000000001.
        event_time (Union[Unset, GetV1EventDeviceResponse200EventsItemEventTime]):
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        severity (Union[Unset, str]):  Example: major.
        type_ (Union[Unset, str]):  Example: InterfaceOperStateChange.
    """

    actions: Union[Unset, list[str]] = UNSET
    device_id: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    event_data: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    event_time: Union[Unset, "GetV1EventDeviceResponse200EventsItemEventTime"] = UNSET
    hostname: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        device_id = self.device_id

        enterprise_id = self.enterprise_id

        event_data = self.event_data

        event_id = self.event_id

        event_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_time, Unset):
            event_time = self.event_time.to_dict()

        hostname = self.hostname

        severity = self.severity

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if event_data is not UNSET:
            field_dict["eventData"] = event_data
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_time is not UNSET:
            field_dict["eventTime"] = event_time
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_event_device_response_200_events_item_event_time import (
            GetV1EventDeviceResponse200EventsItemEventTime,
        )

        d = src_dict.copy()
        actions = cast(list[str], d.pop("actions", UNSET))

        device_id = d.pop("deviceId", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        event_data = d.pop("eventData", UNSET)

        event_id = d.pop("eventId", UNSET)

        _event_time = d.pop("eventTime", UNSET)
        event_time: Union[Unset, GetV1EventDeviceResponse200EventsItemEventTime]
        if isinstance(_event_time, Unset):
            event_time = UNSET
        else:
            event_time = GetV1EventDeviceResponse200EventsItemEventTime.from_dict(_event_time)

        hostname = d.pop("hostname", UNSET)

        severity = d.pop("severity", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_event_device_response_200_events_item = cls(
            actions=actions,
            device_id=device_id,
            enterprise_id=enterprise_id,
            event_data=event_data,
            event_id=event_id,
            event_time=event_time,
            hostname=hostname,
            severity=severity,
            type_=type_,
        )

        get_v1_event_device_response_200_events_item.additional_properties = d
        return get_v1_event_device_response_200_events_item

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
