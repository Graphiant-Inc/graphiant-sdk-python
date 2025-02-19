from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_event_device_response_200_events_item import GetV1EventDeviceResponse200EventsItem


T = TypeVar("T", bound="GetV1EventDeviceResponse200")


@_attrs_define
class GetV1EventDeviceResponse200:
    """
    Attributes:
        events (Union[Unset, list['GetV1EventDeviceResponse200EventsItem']]):
    """

    events: Union[Unset, list["GetV1EventDeviceResponse200EventsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_event_device_response_200_events_item import GetV1EventDeviceResponse200EventsItem

        d = src_dict.copy()
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = GetV1EventDeviceResponse200EventsItem.from_dict(events_item_data)

            events.append(events_item)

        get_v1_event_device_response_200 = cls(
            events=events,
        )

        get_v1_event_device_response_200.additional_properties = d
        return get_v1_event_device_response_200

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
