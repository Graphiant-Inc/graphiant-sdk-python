from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1AlarmCustomResponse201")


@_attrs_define
class PutV1AlarmCustomResponse201:
    """
    Attributes:
        alarm_id (Union[Unset, str]):  Example: 10000.
    """

    alarm_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alarm_id = self.alarm_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarm_id is not UNSET:
            field_dict["alarmId"] = alarm_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alarm_id = d.pop("alarmId", UNSET)

        put_v1_alarm_custom_response_201 = cls(
            alarm_id=alarm_id,
        )

        put_v1_alarm_custom_response_201.additional_properties = d
        return put_v1_alarm_custom_response_201

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
