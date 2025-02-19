from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem")


@_attrs_define
class PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem:
    """
    Attributes:
        edge_count (Union[Unset, str]):  Example: TYPE_UINT64.
        location_id (Union[Unset, str]):  Example: TYPE_UINT64.
        location_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_id (Union[Unset, str]):  Example: TYPE_UINT64.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    edge_count: Union[Unset, str] = UNSET
    location_id: Union[Unset, str] = UNSET
    location_name: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge_count = self.edge_count

        location_id = self.location_id

        location_name = self.location_name

        site_id = self.site_id

        site_name = self.site_name

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_count is not UNSET:
            field_dict["edgeCount"] = edge_count
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        edge_count = d.pop("edgeCount", UNSET)

        location_id = d.pop("locationId", UNSET)

        location_name = d.pop("locationName", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_region_edge_details_response_200_bwusage_details_bwuage_sites_item = cls(
            edge_count=edge_count,
            location_id=location_id,
            location_name=location_name,
            site_id=site_id,
            site_name=site_name,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_region_edge_details_response_200_bwusage_details_bwuage_sites_item.additional_properties = d
        return post_v1_bwtracker_region_edge_details_response_200_bwusage_details_bwuage_sites_item

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
