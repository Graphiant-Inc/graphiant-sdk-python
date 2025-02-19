from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceCreateclassifiedapplicationResponse200")


@_attrs_define
class PostV2AssuranceCreateclassifiedapplicationResponse200:
    """
    Attributes:
        classification_entry_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    classification_entry_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification_entry_id = self.classification_entry_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification_entry_id is not UNSET:
            field_dict["classificationEntryId"] = classification_entry_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        classification_entry_id = d.pop("classificationEntryId", UNSET)

        post_v2_assurance_createclassifiedapplication_response_200 = cls(
            classification_entry_id=classification_entry_id,
        )

        post_v2_assurance_createclassifiedapplication_response_200.additional_properties = d
        return post_v2_assurance_createclassifiedapplication_response_200

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
