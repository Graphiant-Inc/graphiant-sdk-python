from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AllowlistCreateBody")


@_attrs_define
class PostV2AllowlistCreateBody:
    """
    Attributes:
        alert_id (Union[Unset, str]):  Example: TYPE_STRING.
        note_text (Union[Unset, str]):  Example: TYPE_STRING.
    """

    alert_id: Union[Unset, str] = UNSET
    note_text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_id = self.alert_id

        note_text = self.note_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if note_text is not UNSET:
            field_dict["noteText"] = note_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("alertId", UNSET)

        note_text = d.pop("noteText", UNSET)

        post_v2_allowlist_create_body = cls(
            alert_id=alert_id,
            note_text=note_text,
        )

        post_v2_allowlist_create_body.additional_properties = d
        return post_v2_allowlist_create_body

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
