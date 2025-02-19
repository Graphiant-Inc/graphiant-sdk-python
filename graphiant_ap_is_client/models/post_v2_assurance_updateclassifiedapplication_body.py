from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_updateclassifiedapplication_body_classified_application_list_item import (
        PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem,
    )


T = TypeVar("T", bound="PostV2AssuranceUpdateclassifiedapplicationBody")


@_attrs_define
class PostV2AssuranceUpdateclassifiedapplicationBody:
    """
    Attributes:
        classified_application_list (Union[Unset,
            list['PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem']]):
    """

    classified_application_list: Union[
        Unset, list["PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classified_application_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.classified_application_list, Unset):
            classified_application_list = []
            for classified_application_list_item_data in self.classified_application_list:
                classified_application_list_item = classified_application_list_item_data.to_dict()
                classified_application_list.append(classified_application_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classified_application_list is not UNSET:
            field_dict["classifiedApplicationList"] = classified_application_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_updateclassifiedapplication_body_classified_application_list_item import (
            PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem,
        )

        d = src_dict.copy()
        classified_application_list = []
        _classified_application_list = d.pop("classifiedApplicationList", UNSET)
        for classified_application_list_item_data in _classified_application_list or []:
            classified_application_list_item = (
                PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem.from_dict(
                    classified_application_list_item_data
                )
            )

            classified_application_list.append(classified_application_list_item)

        post_v2_assurance_updateclassifiedapplication_body = cls(
            classified_application_list=classified_application_list,
        )

        post_v2_assurance_updateclassifiedapplication_body.additional_properties = d
        return post_v2_assurance_updateclassifiedapplication_body

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
