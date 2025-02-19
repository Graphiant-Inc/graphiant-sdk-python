from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteV2AssuranceDeleteclassifiedapplicationBody")


@_attrs_define
class DeleteV2AssuranceDeleteclassifiedapplicationBody:
    """
    Attributes:
        classification_entry_id_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    classification_entry_id_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification_entry_id_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.classification_entry_id_list, Unset):
            classification_entry_id_list = self.classification_entry_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification_entry_id_list is not UNSET:
            field_dict["classificationEntryIdList"] = classification_entry_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        classification_entry_id_list = cast(list[str], d.pop("classificationEntryIdList", UNSET))

        delete_v2_assurance_deleteclassifiedapplication_body = cls(
            classification_entry_id_list=classification_entry_id_list,
        )

        delete_v2_assurance_deleteclassifiedapplication_body.additional_properties = d
        return delete_v2_assurance_deleteclassifiedapplication_body

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
