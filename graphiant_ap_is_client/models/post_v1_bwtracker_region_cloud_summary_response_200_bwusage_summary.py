from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary_bwusage_top_providers_item import (
        PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummary")


@_attrs_define
class PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummary:
    """
    Attributes:
        bwusage_top_providers (Union[Unset,
            list['PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem']]):
        cloudusage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
        percent_changed (Union[Unset, str]):  Example: TYPE_DOUBLE.
        provider_count (Union[Unset, str]):  Example: TYPE_UINT64.
        providerusage_kbps (Union[Unset, str]):  Example: TYPE_UINT64.
        totusage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    bwusage_top_providers: Union[
        Unset, list["PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem"]
    ] = UNSET
    cloudusage_kbps: Union[Unset, str] = UNSET
    percent_changed: Union[Unset, str] = UNSET
    provider_count: Union[Unset, str] = UNSET
    providerusage_kbps: Union[Unset, str] = UNSET
    totusage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_top_providers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_top_providers, Unset):
            bwusage_top_providers = []
            for bwusage_top_providers_item_data in self.bwusage_top_providers:
                bwusage_top_providers_item = bwusage_top_providers_item_data.to_dict()
                bwusage_top_providers.append(bwusage_top_providers_item)

        cloudusage_kbps = self.cloudusage_kbps

        percent_changed = self.percent_changed

        provider_count = self.provider_count

        providerusage_kbps = self.providerusage_kbps

        totusage_kbps = self.totusage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_top_providers is not UNSET:
            field_dict["bwusageTopProviders"] = bwusage_top_providers
        if cloudusage_kbps is not UNSET:
            field_dict["cloudusageKbps"] = cloudusage_kbps
        if percent_changed is not UNSET:
            field_dict["percentChanged"] = percent_changed
        if provider_count is not UNSET:
            field_dict["providerCount"] = provider_count
        if providerusage_kbps is not UNSET:
            field_dict["providerusageKbps"] = providerusage_kbps
        if totusage_kbps is not UNSET:
            field_dict["totusageKbps"] = totusage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary_bwusage_top_providers_item import (
            PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem,
        )

        d = src_dict.copy()
        bwusage_top_providers = []
        _bwusage_top_providers = d.pop("bwusageTopProviders", UNSET)
        for bwusage_top_providers_item_data in _bwusage_top_providers or []:
            bwusage_top_providers_item = (
                PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem.from_dict(
                    bwusage_top_providers_item_data
                )
            )

            bwusage_top_providers.append(bwusage_top_providers_item)

        cloudusage_kbps = d.pop("cloudusageKbps", UNSET)

        percent_changed = d.pop("percentChanged", UNSET)

        provider_count = d.pop("providerCount", UNSET)

        providerusage_kbps = d.pop("providerusageKbps", UNSET)

        totusage_kbps = d.pop("totusageKbps", UNSET)

        post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary = cls(
            bwusage_top_providers=bwusage_top_providers,
            cloudusage_kbps=cloudusage_kbps,
            percent_changed=percent_changed,
            provider_count=provider_count,
            providerusage_kbps=providerusage_kbps,
            totusage_kbps=totusage_kbps,
        )

        post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary.additional_properties = d
        return post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary

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
