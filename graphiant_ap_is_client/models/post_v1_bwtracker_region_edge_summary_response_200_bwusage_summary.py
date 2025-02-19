from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary_bwusage_top_sites_item import (
        PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummaryBwusageTopSitesItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary")


@_attrs_define
class PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary:
    """
    Attributes:
        bwusage_top_sites (Union[Unset,
            list['PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummaryBwusageTopSitesItem']]):
        edgeusage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
        percent_changed (Union[Unset, str]):  Example: TYPE_DOUBLE.
        site_count (Union[Unset, str]):  Example: TYPE_UINT64.
        totusage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    bwusage_top_sites: Union[
        Unset, list["PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummaryBwusageTopSitesItem"]
    ] = UNSET
    edgeusage_kbps: Union[Unset, str] = UNSET
    percent_changed: Union[Unset, str] = UNSET
    site_count: Union[Unset, str] = UNSET
    totusage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_top_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_top_sites, Unset):
            bwusage_top_sites = []
            for bwusage_top_sites_item_data in self.bwusage_top_sites:
                bwusage_top_sites_item = bwusage_top_sites_item_data.to_dict()
                bwusage_top_sites.append(bwusage_top_sites_item)

        edgeusage_kbps = self.edgeusage_kbps

        percent_changed = self.percent_changed

        site_count = self.site_count

        totusage_kbps = self.totusage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_top_sites is not UNSET:
            field_dict["bwusageTopSites"] = bwusage_top_sites
        if edgeusage_kbps is not UNSET:
            field_dict["edgeusageKbps"] = edgeusage_kbps
        if percent_changed is not UNSET:
            field_dict["percentChanged"] = percent_changed
        if site_count is not UNSET:
            field_dict["siteCount"] = site_count
        if totusage_kbps is not UNSET:
            field_dict["totusageKbps"] = totusage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary_bwusage_top_sites_item import (
            PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummaryBwusageTopSitesItem,
        )

        d = src_dict.copy()
        bwusage_top_sites = []
        _bwusage_top_sites = d.pop("bwusageTopSites", UNSET)
        for bwusage_top_sites_item_data in _bwusage_top_sites or []:
            bwusage_top_sites_item = (
                PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummaryBwusageTopSitesItem.from_dict(
                    bwusage_top_sites_item_data
                )
            )

            bwusage_top_sites.append(bwusage_top_sites_item)

        edgeusage_kbps = d.pop("edgeusageKbps", UNSET)

        percent_changed = d.pop("percentChanged", UNSET)

        site_count = d.pop("siteCount", UNSET)

        totusage_kbps = d.pop("totusageKbps", UNSET)

        post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary = cls(
            bwusage_top_sites=bwusage_top_sites,
            edgeusage_kbps=edgeusage_kbps,
            percent_changed=percent_changed,
            site_count=site_count,
            totusage_kbps=totusage_kbps,
        )

        post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary.additional_properties = d
        return post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary

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
