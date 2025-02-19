from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion:
    """
    Attributes:
        region_id (Union[Unset, str]):  Example: TYPE_INT32.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        region_name = self.region_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        post_v2_assurance_topology_overview_response_200_traffic_regions_item_region = cls(
            region_id=region_id,
            region_name=region_name,
        )

        post_v2_assurance_topology_overview_response_200_traffic_regions_item_region.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_traffic_regions_item_region

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
