from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarms_custom_response_200_alarms_item_alarm_filter_item import (
        GetV1AlarmsCustomResponse200AlarmsItemAlarmFilterItem,
    )


T = TypeVar("T", bound="GetV1AlarmsCustomResponse200AlarmsItemAlarm")


@_attrs_define
class GetV1AlarmsCustomResponse200AlarmsItemAlarm:
    """
    Attributes:
        component (Union[Unset, str]):  Example: graphnos-systemd.
        description (Union[Unset, str]):  Example: created to notify admins when the edge is down.
        events (Union[Unset, list[str]]):  Example: ['[systemd-unit-state-change, systemd-unit-state-down]'].
        filter_ (Union[Unset, list['GetV1AlarmsCustomResponse200AlarmsItemAlarmFilterItem']]):
        name (Union[Unset, str]):  Example: edge_down.
        recipients (Union[Unset, list[str]]):  Example: ['[support@isp.com, admin@isp.com]'].
    """

    component: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    events: Union[Unset, list[str]] = UNSET
    filter_: Union[Unset, list["GetV1AlarmsCustomResponse200AlarmsItemAlarmFilterItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    recipients: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        description = self.description

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        filter_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        name = self.name

        recipients: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if name is not UNSET:
            field_dict["name"] = name
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarms_custom_response_200_alarms_item_alarm_filter_item import (
            GetV1AlarmsCustomResponse200AlarmsItemAlarmFilterItem,
        )

        d = src_dict.copy()
        component = d.pop("component", UNSET)

        description = d.pop("description", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = GetV1AlarmsCustomResponse200AlarmsItemAlarmFilterItem.from_dict(filter_item_data)

            filter_.append(filter_item)

        name = d.pop("name", UNSET)

        recipients = cast(list[str], d.pop("recipients", UNSET))

        get_v1_alarms_custom_response_200_alarms_item_alarm = cls(
            component=component,
            description=description,
            events=events,
            filter_=filter_,
            name=name,
            recipients=recipients,
        )

        get_v1_alarms_custom_response_200_alarms_item_alarm.additional_properties = d
        return get_v1_alarms_custom_response_200_alarms_item_alarm

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
