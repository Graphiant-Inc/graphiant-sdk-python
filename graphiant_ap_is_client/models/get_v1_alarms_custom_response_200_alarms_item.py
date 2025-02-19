from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarms_custom_response_200_alarms_item_alarm import GetV1AlarmsCustomResponse200AlarmsItemAlarm


T = TypeVar("T", bound="GetV1AlarmsCustomResponse200AlarmsItem")


@_attrs_define
class GetV1AlarmsCustomResponse200AlarmsItem:
    """
    Attributes:
        alarm (Union[Unset, GetV1AlarmsCustomResponse200AlarmsItemAlarm]):
        alarm_id (Union[Unset, str]):  Example: 10000.
    """

    alarm: Union[Unset, "GetV1AlarmsCustomResponse200AlarmsItemAlarm"] = UNSET
    alarm_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alarm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.alarm, Unset):
            alarm = self.alarm.to_dict()

        alarm_id = self.alarm_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarm is not UNSET:
            field_dict["alarm"] = alarm
        if alarm_id is not UNSET:
            field_dict["alarmId"] = alarm_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarms_custom_response_200_alarms_item_alarm import (
            GetV1AlarmsCustomResponse200AlarmsItemAlarm,
        )

        d = src_dict.copy()
        _alarm = d.pop("alarm", UNSET)
        alarm: Union[Unset, GetV1AlarmsCustomResponse200AlarmsItemAlarm]
        if isinstance(_alarm, Unset):
            alarm = UNSET
        else:
            alarm = GetV1AlarmsCustomResponse200AlarmsItemAlarm.from_dict(_alarm)

        alarm_id = d.pop("alarmId", UNSET)

        get_v1_alarms_custom_response_200_alarms_item = cls(
            alarm=alarm,
            alarm_id=alarm_id,
        )

        get_v1_alarms_custom_response_200_alarms_item.additional_properties = d
        return get_v1_alarms_custom_response_200_alarms_item

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
