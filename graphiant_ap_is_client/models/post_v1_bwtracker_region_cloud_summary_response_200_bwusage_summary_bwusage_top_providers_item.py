from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem")


@_attrs_define
class PostV1BwtrackerRegionCloudSummaryResponse200BwusageSummaryBwusageTopProvidersItem:
    """
    Attributes:
        capacity_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
        provider_id (Union[Unset, str]):  Example: TYPE_UINT64.
        provider_name (Union[Unset, str]):  Example: TYPE_STRING.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    capacity_kbps: Union[Unset, str] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_name: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity_kbps = self.capacity_kbps

        provider_id = self.provider_id

        provider_name = self.provider_name

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity_kbps is not UNSET:
            field_dict["capacityKbps"] = capacity_kbps
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        capacity_kbps = d.pop("capacityKbps", UNSET)

        provider_id = d.pop("providerId", UNSET)

        provider_name = d.pop("providerName", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary_bwusage_top_providers_item = cls(
            capacity_kbps=capacity_kbps,
            provider_id=provider_id,
            provider_name=provider_name,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary_bwusage_top_providers_item.additional_properties = d
        return post_v1_bwtracker_region_cloud_summary_response_200_bwusage_summary_bwusage_top_providers_item

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
