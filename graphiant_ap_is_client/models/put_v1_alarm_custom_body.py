from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_alarm_custom_body_alarm import PutV1AlarmCustomBodyAlarm


T = TypeVar("T", bound="PutV1AlarmCustomBody")


@_attrs_define
class PutV1AlarmCustomBody:
    """
    Attributes:
        alarm (Union[Unset, PutV1AlarmCustomBodyAlarm]):
    """

    alarm: Union[Unset, "PutV1AlarmCustomBodyAlarm"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alarm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.alarm, Unset):
            alarm = self.alarm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarm is not UNSET:
            field_dict["alarm"] = alarm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_alarm_custom_body_alarm import PutV1AlarmCustomBodyAlarm

        d = src_dict.copy()
        _alarm = d.pop("alarm", UNSET)
        alarm: Union[Unset, PutV1AlarmCustomBodyAlarm]
        if isinstance(_alarm, Unset):
            alarm = UNSET
        else:
            alarm = PutV1AlarmCustomBodyAlarm.from_dict(_alarm)

        put_v1_alarm_custom_body = cls(
            alarm=alarm,
        )

        put_v1_alarm_custom_body.additional_properties = d
        return put_v1_alarm_custom_body

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
