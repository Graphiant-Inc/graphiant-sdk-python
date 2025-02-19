from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1LogsBodySelectorsItem")


@_attrs_define
class PostV1LogsBodySelectorsItem:
    """
    Attributes:
        field (Union[Unset, str]):  Example: TYPE_ENUM.
        values (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    field: Union[Unset, str] = UNSET
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        post_v1_logs_body_selectors_item = cls(
            field=field,
            values=values,
        )

        post_v1_logs_body_selectors_item.additional_properties = d
        return post_v1_logs_body_selectors_item

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
