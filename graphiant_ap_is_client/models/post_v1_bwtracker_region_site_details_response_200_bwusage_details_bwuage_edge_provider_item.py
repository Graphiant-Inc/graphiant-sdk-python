from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem")


@_attrs_define
class PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        provider_id (Union[Unset, str]):  Example: TYPE_UINT64.
        provider_name (Union[Unset, str]):  Example: TYPE_STRING.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_name: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        provider_id = self.provider_id

        provider_name = self.provider_name

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
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
        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        provider_id = d.pop("providerId", UNSET)

        provider_name = d.pop("providerName", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_edge_provider_item = cls(
            device_id=device_id,
            device_name=device_name,
            provider_id=provider_id,
            provider_name=provider_name,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_edge_provider_item.additional_properties = d
        return post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_edge_provider_item

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
