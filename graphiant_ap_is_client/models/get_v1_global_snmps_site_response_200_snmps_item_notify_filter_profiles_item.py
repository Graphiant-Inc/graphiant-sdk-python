from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item_include_exclude_list_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem,
    )


T = TypeVar("T", bound="GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem")


@_attrs_define
class GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        include_exclude_list (Union[Unset,
            list['GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    id: Union[Unset, str] = UNSET
    include_exclude_list: Union[
        Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem"]
    ] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        include_exclude_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.include_exclude_list, Unset):
            include_exclude_list = []
            for include_exclude_list_item_data in self.include_exclude_list:
                include_exclude_list_item = include_exclude_list_item_data.to_dict()
                include_exclude_list.append(include_exclude_list_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if include_exclude_list is not UNSET:
            field_dict["includeExcludeList"] = include_exclude_list
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item_include_exclude_list_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        include_exclude_list = []
        _include_exclude_list = d.pop("includeExcludeList", UNSET)
        for include_exclude_list_item_data in _include_exclude_list or []:
            include_exclude_list_item = (
                GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItemIncludeExcludeListItem.from_dict(
                    include_exclude_list_item_data
                )
            )

            include_exclude_list.append(include_exclude_list_item)

        name = d.pop("name", UNSET)

        get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item = cls(
            id=id,
            include_exclude_list=include_exclude_list,
            name=name,
        )

        get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item.additional_properties = d
        return get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item

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
