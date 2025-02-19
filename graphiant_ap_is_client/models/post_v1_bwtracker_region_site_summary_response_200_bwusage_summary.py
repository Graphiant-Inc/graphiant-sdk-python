from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_summary_response_200_bwusage_summary_bwuage_region_item import (
        PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummaryBwuageRegionItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummary")


@_attrs_define
class PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummary:
    """
    Attributes:
        bwuage_region (Union[Unset, list['PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummaryBwuageRegionItem']]):
        edge_count (Union[Unset, str]):  Example: TYPE_UINT64.
        provider_count (Union[Unset, str]):  Example: TYPE_UINT64.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    bwuage_region: Union[Unset, list["PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummaryBwuageRegionItem"]] = (
        UNSET
    )
    edge_count: Union[Unset, str] = UNSET
    provider_count: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwuage_region: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwuage_region, Unset):
            bwuage_region = []
            for bwuage_region_item_data in self.bwuage_region:
                bwuage_region_item = bwuage_region_item_data.to_dict()
                bwuage_region.append(bwuage_region_item)

        edge_count = self.edge_count

        provider_count = self.provider_count

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwuage_region is not UNSET:
            field_dict["bwuageRegion"] = bwuage_region
        if edge_count is not UNSET:
            field_dict["edgeCount"] = edge_count
        if provider_count is not UNSET:
            field_dict["providerCount"] = provider_count
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_summary_response_200_bwusage_summary_bwuage_region_item import (
            PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummaryBwuageRegionItem,
        )

        d = src_dict.copy()
        bwuage_region = []
        _bwuage_region = d.pop("bwuageRegion", UNSET)
        for bwuage_region_item_data in _bwuage_region or []:
            bwuage_region_item = PostV1BwtrackerRegionSiteSummaryResponse200BwusageSummaryBwuageRegionItem.from_dict(
                bwuage_region_item_data
            )

            bwuage_region.append(bwuage_region_item)

        edge_count = d.pop("edgeCount", UNSET)

        provider_count = d.pop("providerCount", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_region_site_summary_response_200_bwusage_summary = cls(
            bwuage_region=bwuage_region,
            edge_count=edge_count,
            provider_count=provider_count,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_region_site_summary_response_200_bwusage_summary.additional_properties = d
        return post_v1_bwtracker_region_site_summary_response_200_bwusage_summary

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
