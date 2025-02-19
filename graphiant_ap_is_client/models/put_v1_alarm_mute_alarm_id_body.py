from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1AlarmMuteAlarmIdBody")


@_attrs_define
class PutV1AlarmMuteAlarmIdBody:
    """
    Attributes:
        mute (Union[Unset, str]):  Example: true.
    """

    mute: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mute = self.mute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mute is not UNSET:
            field_dict["mute"] = mute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        mute = d.pop("mute", UNSET)

        put_v1_alarm_mute_alarm_id_body = cls(
            mute=mute,
        )

        put_v1_alarm_mute_alarm_id_body.additional_properties = d
        return put_v1_alarm_mute_alarm_id_body

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
