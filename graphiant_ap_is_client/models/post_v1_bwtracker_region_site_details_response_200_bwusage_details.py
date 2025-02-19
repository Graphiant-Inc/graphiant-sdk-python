from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_edge_provider_item import (
        PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem,
    )
    from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_provider_item import (
        PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageProviderItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails")


@_attrs_define
class PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails:
    """
    Attributes:
        bwuage_edge_provider (Union[Unset,
            list['PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem']]):
        bwuage_provider (Union[Unset,
            list['PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageProviderItem']]):
    """

    bwuage_edge_provider: Union[
        Unset, list["PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem"]
    ] = UNSET
    bwuage_provider: Union[
        Unset, list["PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageProviderItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwuage_edge_provider: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwuage_edge_provider, Unset):
            bwuage_edge_provider = []
            for bwuage_edge_provider_item_data in self.bwuage_edge_provider:
                bwuage_edge_provider_item = bwuage_edge_provider_item_data.to_dict()
                bwuage_edge_provider.append(bwuage_edge_provider_item)

        bwuage_provider: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwuage_provider, Unset):
            bwuage_provider = []
            for bwuage_provider_item_data in self.bwuage_provider:
                bwuage_provider_item = bwuage_provider_item_data.to_dict()
                bwuage_provider.append(bwuage_provider_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwuage_edge_provider is not UNSET:
            field_dict["bwuageEdgeProvider"] = bwuage_edge_provider
        if bwuage_provider is not UNSET:
            field_dict["bwuageProvider"] = bwuage_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_edge_provider_item import (
            PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem,
        )
        from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details_bwuage_provider_item import (
            PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageProviderItem,
        )

        d = src_dict.copy()
        bwuage_edge_provider = []
        _bwuage_edge_provider = d.pop("bwuageEdgeProvider", UNSET)
        for bwuage_edge_provider_item_data in _bwuage_edge_provider or []:
            bwuage_edge_provider_item = (
                PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageEdgeProviderItem.from_dict(
                    bwuage_edge_provider_item_data
                )
            )

            bwuage_edge_provider.append(bwuage_edge_provider_item)

        bwuage_provider = []
        _bwuage_provider = d.pop("bwuageProvider", UNSET)
        for bwuage_provider_item_data in _bwuage_provider or []:
            bwuage_provider_item = (
                PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetailsBwuageProviderItem.from_dict(
                    bwuage_provider_item_data
                )
            )

            bwuage_provider.append(bwuage_provider_item)

        post_v1_bwtracker_region_site_details_response_200_bwusage_details = cls(
            bwuage_edge_provider=bwuage_edge_provider,
            bwuage_provider=bwuage_provider,
        )

        post_v1_bwtracker_region_site_details_response_200_bwusage_details.additional_properties = d
        return post_v1_bwtracker_region_site_details_response_200_bwusage_details

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
