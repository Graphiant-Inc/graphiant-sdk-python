from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1SiteDetailsSitelistsResponse200SiteListsItem")


@_attrs_define
class PostV1SiteDetailsSitelistsResponse200SiteListsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        policy_count (Union[Unset, str]):  Example: TYPE_UINT32.
        site_count (Union[Unset, str]):  Example: TYPE_UINT32.
        site_list_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    name: Union[Unset, str] = UNSET
    policy_count: Union[Unset, str] = UNSET
    site_count: Union[Unset, str] = UNSET
    site_list_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        policy_count = self.policy_count

        site_count = self.site_count

        site_list_id = self.site_list_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if policy_count is not UNSET:
            field_dict["policyCount"] = policy_count
        if site_count is not UNSET:
            field_dict["siteCount"] = site_count
        if site_list_id is not UNSET:
            field_dict["siteListId"] = site_list_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        policy_count = d.pop("policyCount", UNSET)

        site_count = d.pop("siteCount", UNSET)

        site_list_id = d.pop("siteListId", UNSET)

        post_v1_site_details_sitelists_response_200_site_lists_item = cls(
            name=name,
            policy_count=policy_count,
            site_count=site_count,
            site_list_id=site_list_id,
        )

        post_v1_site_details_sitelists_response_200_site_lists_item.additional_properties = d
        return post_v1_site_details_sitelists_response_200_site_lists_item

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
