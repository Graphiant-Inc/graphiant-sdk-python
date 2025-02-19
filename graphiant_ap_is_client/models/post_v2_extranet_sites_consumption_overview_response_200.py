from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item import (
        PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem,
    )
    from ..models.post_v2_extranet_sites_consumption_overview_response_200_regions_item import (
        PostV2ExtranetSitesConsumptionOverviewResponse200RegionsItem,
    )
    from ..models.post_v2_extranet_sites_consumption_overview_response_200_sites_item import (
        PostV2ExtranetSitesConsumptionOverviewResponse200SitesItem,
    )


T = TypeVar("T", bound="PostV2ExtranetSitesConsumptionOverviewResponse200")


@_attrs_define
class PostV2ExtranetSitesConsumptionOverviewResponse200:
    """
    Attributes:
        lan_segments (Union[Unset, list['PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem']]):
        regions (Union[Unset, list['PostV2ExtranetSitesConsumptionOverviewResponse200RegionsItem']]):
        sites (Union[Unset, list['PostV2ExtranetSitesConsumptionOverviewResponse200SitesItem']]):
    """

    lan_segments: Union[Unset, list["PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem"]] = UNSET
    regions: Union[Unset, list["PostV2ExtranetSitesConsumptionOverviewResponse200RegionsItem"]] = UNSET
    sites: Union[Unset, list["PostV2ExtranetSitesConsumptionOverviewResponse200SitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = []
            for lan_segments_item_data in self.lan_segments:
                lan_segments_item = lan_segments_item_data.to_dict()
                lan_segments.append(lan_segments_item)

        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if regions is not UNSET:
            field_dict["regions"] = regions
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item import (
            PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem,
        )
        from ..models.post_v2_extranet_sites_consumption_overview_response_200_regions_item import (
            PostV2ExtranetSitesConsumptionOverviewResponse200RegionsItem,
        )
        from ..models.post_v2_extranet_sites_consumption_overview_response_200_sites_item import (
            PostV2ExtranetSitesConsumptionOverviewResponse200SitesItem,
        )

        d = src_dict.copy()
        lan_segments = []
        _lan_segments = d.pop("lanSegments", UNSET)
        for lan_segments_item_data in _lan_segments or []:
            lan_segments_item = PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem.from_dict(
                lan_segments_item_data
            )

            lan_segments.append(lan_segments_item)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = PostV2ExtranetSitesConsumptionOverviewResponse200RegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PostV2ExtranetSitesConsumptionOverviewResponse200SitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        post_v2_extranet_sites_consumption_overview_response_200 = cls(
            lan_segments=lan_segments,
            regions=regions,
            sites=sites,
        )

        post_v2_extranet_sites_consumption_overview_response_200.additional_properties = d
        return post_v2_extranet_sites_consumption_overview_response_200

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
