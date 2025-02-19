from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_role_summary_item import (
        PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageRoleSummaryItem,
    )
    from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_top_regions_item import (
        PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItem,
    )
    from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_min_time import (
        PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime,
    )


T = TypeVar("T", bound="PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummary")


@_attrs_define
class PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummary:
    """
    Attributes:
        bwusage_role_summary (Union[Unset,
            list['PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageRoleSummaryItem']]):
        bwusage_top_regions (Union[Unset,
            list['PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItem']]):
        min_time (Union[Unset, PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime]):
        percent_changed (Union[Unset, str]):  Example: TYPE_DOUBLE.
        provider_count (Union[Unset, str]):  Example: TYPE_UINT64.
        region_count (Union[Unset, str]):  Example: TYPE_UINT64.
        site_count (Union[Unset, str]):  Example: TYPE_UINT64.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    bwusage_role_summary: Union[
        Unset, list["PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageRoleSummaryItem"]
    ] = UNSET
    bwusage_top_regions: Union[
        Unset, list["PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItem"]
    ] = UNSET
    min_time: Union[Unset, "PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime"] = UNSET
    percent_changed: Union[Unset, str] = UNSET
    provider_count: Union[Unset, str] = UNSET
    region_count: Union[Unset, str] = UNSET
    site_count: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_role_summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_role_summary, Unset):
            bwusage_role_summary = []
            for bwusage_role_summary_item_data in self.bwusage_role_summary:
                bwusage_role_summary_item = bwusage_role_summary_item_data.to_dict()
                bwusage_role_summary.append(bwusage_role_summary_item)

        bwusage_top_regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_top_regions, Unset):
            bwusage_top_regions = []
            for bwusage_top_regions_item_data in self.bwusage_top_regions:
                bwusage_top_regions_item = bwusage_top_regions_item_data.to_dict()
                bwusage_top_regions.append(bwusage_top_regions_item)

        min_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.min_time, Unset):
            min_time = self.min_time.to_dict()

        percent_changed = self.percent_changed

        provider_count = self.provider_count

        region_count = self.region_count

        site_count = self.site_count

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_role_summary is not UNSET:
            field_dict["bwusageRoleSummary"] = bwusage_role_summary
        if bwusage_top_regions is not UNSET:
            field_dict["bwusageTopRegions"] = bwusage_top_regions
        if min_time is not UNSET:
            field_dict["minTime"] = min_time
        if percent_changed is not UNSET:
            field_dict["percentChanged"] = percent_changed
        if provider_count is not UNSET:
            field_dict["providerCount"] = provider_count
        if region_count is not UNSET:
            field_dict["regionCount"] = region_count
        if site_count is not UNSET:
            field_dict["siteCount"] = site_count
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_role_summary_item import (
            PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageRoleSummaryItem,
        )
        from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_top_regions_item import (
            PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItem,
        )
        from ..models.post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_min_time import (
            PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime,
        )

        d = src_dict.copy()
        bwusage_role_summary = []
        _bwusage_role_summary = d.pop("bwusageRoleSummary", UNSET)
        for bwusage_role_summary_item_data in _bwusage_role_summary or []:
            bwusage_role_summary_item = (
                PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageRoleSummaryItem.from_dict(
                    bwusage_role_summary_item_data
                )
            )

            bwusage_role_summary.append(bwusage_role_summary_item)

        bwusage_top_regions = []
        _bwusage_top_regions = d.pop("bwusageTopRegions", UNSET)
        for bwusage_top_regions_item_data in _bwusage_top_regions or []:
            bwusage_top_regions_item = (
                PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItem.from_dict(
                    bwusage_top_regions_item_data
                )
            )

            bwusage_top_regions.append(bwusage_top_regions_item)

        _min_time = d.pop("minTime", UNSET)
        min_time: Union[Unset, PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime]
        if isinstance(_min_time, Unset):
            min_time = UNSET
        else:
            min_time = PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryMinTime.from_dict(_min_time)

        percent_changed = d.pop("percentChanged", UNSET)

        provider_count = d.pop("providerCount", UNSET)

        region_count = d.pop("regionCount", UNSET)

        site_count = d.pop("siteCount", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary = cls(
            bwusage_role_summary=bwusage_role_summary,
            bwusage_top_regions=bwusage_top_regions,
            min_time=min_time,
            percent_changed=percent_changed,
            provider_count=provider_count,
            region_count=region_count,
            site_count=site_count,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary.additional_properties = d
        return post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary

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
