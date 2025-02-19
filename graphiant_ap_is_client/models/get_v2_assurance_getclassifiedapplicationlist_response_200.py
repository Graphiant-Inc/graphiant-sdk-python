from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_assurance_getclassifiedapplicationlist_response_200_classified_application_list_item import (
        GetV2AssuranceGetclassifiedapplicationlistResponse200ClassifiedApplicationListItem,
    )


T = TypeVar("T", bound="GetV2AssuranceGetclassifiedapplicationlistResponse200")


@_attrs_define
class GetV2AssuranceGetclassifiedapplicationlistResponse200:
    """
    Attributes:
        classified_application_list (Union[Unset,
            list['GetV2AssuranceGetclassifiedapplicationlistResponse200ClassifiedApplicationListItem']]):
    """

    classified_application_list: Union[
        Unset, list["GetV2AssuranceGetclassifiedapplicationlistResponse200ClassifiedApplicationListItem"]
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
        from ..models.get_v2_assurance_getclassifiedapplicationlist_response_200_classified_application_list_item import (
            GetV2AssuranceGetclassifiedapplicationlistResponse200ClassifiedApplicationListItem,
        )

        d = src_dict.copy()
        classified_application_list = []
        _classified_application_list = d.pop("classifiedApplicationList", UNSET)
        for classified_application_list_item_data in _classified_application_list or []:
            classified_application_list_item = (
                GetV2AssuranceGetclassifiedapplicationlistResponse200ClassifiedApplicationListItem.from_dict(
                    classified_application_list_item_data
                )
            )

            classified_application_list.append(classified_application_list_item)

        get_v2_assurance_getclassifiedapplicationlist_response_200 = cls(
            classified_application_list=classified_application_list,
        )

        get_v2_assurance_getclassifiedapplicationlist_response_200.additional_properties = d
        return get_v2_assurance_getclassifiedapplicationlist_response_200

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
