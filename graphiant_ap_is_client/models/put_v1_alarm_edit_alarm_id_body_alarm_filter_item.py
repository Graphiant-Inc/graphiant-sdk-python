from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1AlarmEditAlarmIdBodyAlarmFilterItem")


@_attrs_define
class PutV1AlarmEditAlarmIdBodyAlarmFilterItem:
    """
    Attributes:
        filter_ (Union[Unset, str]):  Example: high.
        filter_type (Union[Unset, str]):  Example: Severity.
    """

    filter_: Union[Unset, str] = UNSET
    filter_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        filter_type = self.filter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_ = d.pop("filter", UNSET)

        filter_type = d.pop("filterType", UNSET)

        put_v1_alarm_edit_alarm_id_body_alarm_filter_item = cls(
            filter_=filter_,
            filter_type=filter_type,
        )

        put_v1_alarm_edit_alarm_id_body_alarm_filter_item.additional_properties = d
        return put_v1_alarm_edit_alarm_id_body_alarm_filter_item

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
