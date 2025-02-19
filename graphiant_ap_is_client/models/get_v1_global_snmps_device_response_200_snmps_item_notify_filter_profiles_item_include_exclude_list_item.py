from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalSnmpsDeviceResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem")


@_attrs_define
class GetV1GlobalSnmpsDeviceResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        include (Union[Unset, str]):  Example: TYPE_BOOL.
        subtree (Union[Unset, str]):  Example: TYPE_STRING.
    """

    id: Union[Unset, str] = UNSET
    include: Union[Unset, str] = UNSET
    subtree: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        include = self.include

        subtree = self.subtree

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if include is not UNSET:
            field_dict["include"] = include
        if subtree is not UNSET:
            field_dict["subtree"] = subtree

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        include = d.pop("include", UNSET)

        subtree = d.pop("subtree", UNSET)

        get_v1_global_snmps_device_response_200_snmps_item_notify_filter_profiles_item_include_exclude_list_item = cls(
            id=id,
            include=include,
            subtree=subtree,
        )

        get_v1_global_snmps_device_response_200_snmps_item_notify_filter_profiles_item_include_exclude_list_item.additional_properties = d
        return get_v1_global_snmps_device_response_200_snmps_item_notify_filter_profiles_item_include_exclude_list_item

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
