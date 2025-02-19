from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_edge_details_response_200_bwusage_details_bwuage_sites_item import (
        PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetails")


@_attrs_define
class PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetails:
    """
    Attributes:
        bwuage_sites (Union[Unset, list['PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem']]):
    """

    bwuage_sites: Union[Unset, list["PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwuage_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwuage_sites, Unset):
            bwuage_sites = []
            for bwuage_sites_item_data in self.bwuage_sites:
                bwuage_sites_item = bwuage_sites_item_data.to_dict()
                bwuage_sites.append(bwuage_sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwuage_sites is not UNSET:
            field_dict["bwuageSites"] = bwuage_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_edge_details_response_200_bwusage_details_bwuage_sites_item import (
            PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem,
        )

        d = src_dict.copy()
        bwuage_sites = []
        _bwuage_sites = d.pop("bwuageSites", UNSET)
        for bwuage_sites_item_data in _bwuage_sites or []:
            bwuage_sites_item = PostV1BwtrackerRegionEdgeDetailsResponse200BwusageDetailsBwuageSitesItem.from_dict(
                bwuage_sites_item_data
            )

            bwuage_sites.append(bwuage_sites_item)

        post_v1_bwtracker_region_edge_details_response_200_bwusage_details = cls(
            bwuage_sites=bwuage_sites,
        )

        post_v1_bwtracker_region_edge_details_response_200_bwusage_details.additional_properties = d
        return post_v1_bwtracker_region_edge_details_response_200_bwusage_details

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
