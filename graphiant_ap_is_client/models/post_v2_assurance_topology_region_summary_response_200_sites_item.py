from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyRegionSummaryResponse200SitesItem")


@_attrs_define
class PostV2AssuranceTopologyRegionSummaryResponse200SitesItem:
    """
    Attributes:
        edge_count (Union[Unset, str]):  Example: TYPE_INT32.
        lan_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        pop_names (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        tags (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    edge_count: Union[Unset, str] = UNSET
    lan_segments: Union[Unset, list[str]] = UNSET
    pop_names: Union[Unset, list[str]] = UNSET
    region_name: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge_count = self.edge_count

        lan_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = self.lan_segments

        pop_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pop_names, Unset):
            pop_names = self.pop_names

        region_name = self.region_name

        site_id = self.site_id

        site_name = self.site_name

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_count is not UNSET:
            field_dict["edgeCount"] = edge_count
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if pop_names is not UNSET:
            field_dict["popNames"] = pop_names
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        edge_count = d.pop("edgeCount", UNSET)

        lan_segments = cast(list[str], d.pop("lanSegments", UNSET))

        pop_names = cast(list[str], d.pop("popNames", UNSET))

        region_name = d.pop("regionName", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        post_v2_assurance_topology_region_summary_response_200_sites_item = cls(
            edge_count=edge_count,
            lan_segments=lan_segments,
            pop_names=pop_names,
            region_name=region_name,
            site_id=site_id,
            site_name=site_name,
            tags=tags,
        )

        post_v2_assurance_topology_region_summary_response_200_sites_item.additional_properties = d
        return post_v2_assurance_topology_region_summary_response_200_sites_item

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
