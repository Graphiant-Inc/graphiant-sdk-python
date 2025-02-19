from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1ExtranetsB2BIdResponse200PolicyPolicySitesItem")


@_attrs_define
class PutV1ExtranetsB2BIdResponse200PolicyPolicySitesItem:
    """
    Attributes:
        bw_allocation_site_lists (Union[Unset, str]):  Example: TYPE_INT32.
        bw_allocation_sites (Union[Unset, str]):  Example: TYPE_INT32.
        site_lists (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        sites (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    bw_allocation_site_lists: Union[Unset, str] = UNSET
    bw_allocation_sites: Union[Unset, str] = UNSET
    site_lists: Union[Unset, list[str]] = UNSET
    sites: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bw_allocation_site_lists = self.bw_allocation_site_lists

        bw_allocation_sites = self.bw_allocation_sites

        site_lists: Union[Unset, list[str]] = UNSET
        if not isinstance(self.site_lists, Unset):
            site_lists = self.site_lists

        sites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bw_allocation_site_lists is not UNSET:
            field_dict["bwAllocationSiteLists"] = bw_allocation_site_lists
        if bw_allocation_sites is not UNSET:
            field_dict["bwAllocationSites"] = bw_allocation_sites
        if site_lists is not UNSET:
            field_dict["siteLists"] = site_lists
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bw_allocation_site_lists = d.pop("bwAllocationSiteLists", UNSET)

        bw_allocation_sites = d.pop("bwAllocationSites", UNSET)

        site_lists = cast(list[str], d.pop("siteLists", UNSET))

        sites = cast(list[str], d.pop("sites", UNSET))

        put_v1_extranets_b2b_id_response_200_policy_policy_sites_item = cls(
            bw_allocation_site_lists=bw_allocation_site_lists,
            bw_allocation_sites=bw_allocation_sites,
            site_lists=site_lists,
            sites=sites,
        )

        put_v1_extranets_b2b_id_response_200_policy_policy_sites_item.additional_properties = d
        return put_v1_extranets_b2b_id_response_200_policy_policy_sites_item

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
