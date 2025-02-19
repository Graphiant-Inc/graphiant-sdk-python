from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem")


@_attrs_define
class PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem:
    """
    Attributes:
        region_id (Union[Unset, str]):  Example: TYPE_UINT64.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_count (Union[Unset, str]):  Example: TYPE_UINT64.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    site_count: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        region_name = self.region_name

        site_count = self.site_count

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if site_count is not UNSET:
            field_dict["siteCount"] = site_count
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        site_count = d.pop("siteCount", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_enterprise_details_response_200_bwusage_details_bwusage_region_item = cls(
            region_id=region_id,
            region_name=region_name,
            site_count=site_count,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_enterprise_details_response_200_bwusage_details_bwusage_region_item.additional_properties = d
        return post_v1_bwtracker_enterprise_details_response_200_bwusage_details_bwusage_region_item

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
