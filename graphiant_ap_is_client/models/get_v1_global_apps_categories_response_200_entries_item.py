from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_categories_response_200_entries_item_category import (
        GetV1GlobalAppsCategoriesResponse200EntriesItemCategory,
    )


T = TypeVar("T", bound="GetV1GlobalAppsCategoriesResponse200EntriesItem")


@_attrs_define
class GetV1GlobalAppsCategoriesResponse200EntriesItem:
    """
    Attributes:
        app_count (Union[Unset, str]):  Example: TYPE_INT32.
        category (Union[Unset, GetV1GlobalAppsCategoriesResponse200EntriesItemCategory]):
    """

    app_count: Union[Unset, str] = UNSET
    category: Union[Unset, "GetV1GlobalAppsCategoriesResponse200EntriesItemCategory"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_count = self.app_count

        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_count is not UNSET:
            field_dict["appCount"] = app_count
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_categories_response_200_entries_item_category import (
            GetV1GlobalAppsCategoriesResponse200EntriesItemCategory,
        )

        d = src_dict.copy()
        app_count = d.pop("appCount", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, GetV1GlobalAppsCategoriesResponse200EntriesItemCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetV1GlobalAppsCategoriesResponse200EntriesItemCategory.from_dict(_category)

        get_v1_global_apps_categories_response_200_entries_item = cls(
            app_count=app_count,
            category=category,
        )

        get_v1_global_apps_categories_response_200_entries_item.additional_properties = d
        return get_v1_global_apps_categories_response_200_entries_item

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
