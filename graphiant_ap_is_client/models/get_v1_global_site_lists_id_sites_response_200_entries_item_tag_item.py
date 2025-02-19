from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem")


@_attrs_define
class GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem:
    """
    Attributes:
        level_one (Union[Unset, str]):  Example: TYPE_INT64.
        level_two (Union[Unset, str]):  Example: TYPE_INT64.
        level_zero (Union[Unset, str]):  Example: TYPE_INT64.
    """

    level_one: Union[Unset, str] = UNSET
    level_two: Union[Unset, str] = UNSET
    level_zero: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level_one = self.level_one

        level_two = self.level_two

        level_zero = self.level_zero

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level_one is not UNSET:
            field_dict["levelOne"] = level_one
        if level_two is not UNSET:
            field_dict["levelTwo"] = level_two
        if level_zero is not UNSET:
            field_dict["levelZero"] = level_zero

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        level_one = d.pop("levelOne", UNSET)

        level_two = d.pop("levelTwo", UNSET)

        level_zero = d.pop("levelZero", UNSET)

        get_v1_global_site_lists_id_sites_response_200_entries_item_tag_item = cls(
            level_one=level_one,
            level_two=level_two,
            level_zero=level_zero,
        )

        get_v1_global_site_lists_id_sites_response_200_entries_item_tag_item.additional_properties = d
        return get_v1_global_site_lists_id_sites_response_200_entries_item_tag_item

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
