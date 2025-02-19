from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_response_200_traffic_regions_item_region import (
        PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem:
    """
    Attributes:
        num_sites (Union[Unset, str]):  Example: TYPE_INT32.
        region (Union[Unset, PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion]):
    """

    num_sites: Union[Unset, str] = UNSET
    region: Union[Unset, "PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_sites = self.num_sites

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_sites is not UNSET:
            field_dict["numSites"] = num_sites
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_response_200_traffic_regions_item_region import (
            PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion,
        )

        d = src_dict.copy()
        num_sites = d.pop("numSites", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItemRegion.from_dict(_region)

        post_v2_assurance_topology_overview_response_200_traffic_regions_item = cls(
            num_sites=num_sites,
            region=region,
        )

        post_v2_assurance_topology_overview_response_200_traffic_regions_item.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_traffic_regions_item

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
