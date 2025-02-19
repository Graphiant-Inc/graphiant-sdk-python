from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem")


@_attrs_define
class PostV1BwtrackerRegionEdgeCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem:
    """
    Attributes:
        cloud_provider_name (Union[Unset, str]):  Example: TYPE_STRING.
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        enterprise_id (Union[Unset, str]):  Example: TYPE_UINT64.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        service_type (Union[Unset, str]):  Example: TYPE_UINT64.
        site_id (Union[Unset, str]):  Example: TYPE_UINT64.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    cloud_provider_name: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    service_type: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_provider_name = self.cloud_provider_name

        device_id = self.device_id

        enterprise_id = self.enterprise_id

        region_name = self.region_name

        service_type = self.service_type

        site_id = self.site_id

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_provider_name is not UNSET:
            field_dict["cloudProviderName"] = cloud_provider_name
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_provider_name = d.pop("cloudProviderName", UNSET)

        device_id = d.pop("deviceId", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        region_name = d.pop("regionName", UNSET)

        service_type = d.pop("serviceType", UNSET)

        site_id = d.pop("siteId", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_region_edge_csv_response_200_bwusage_csv_details_bwusage_csv_record_item = cls(
            cloud_provider_name=cloud_provider_name,
            device_id=device_id,
            enterprise_id=enterprise_id,
            region_name=region_name,
            service_type=service_type,
            site_id=site_id,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_region_edge_csv_response_200_bwusage_csv_details_bwusage_csv_record_item.additional_properties = d
        return post_v1_bwtracker_region_edge_csv_response_200_bwusage_csv_details_bwusage_csv_record_item

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
