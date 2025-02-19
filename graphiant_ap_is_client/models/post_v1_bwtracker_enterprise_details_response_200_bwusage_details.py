from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_enterprise_details_response_200_bwusage_details_bwusage_region_item import (
        PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetails")


@_attrs_define
class PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetails:
    """
    Attributes:
        bwusage_region (Union[Unset,
            list['PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem']]):
    """

    bwusage_region: Union[Unset, list["PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_region: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_region, Unset):
            bwusage_region = []
            for bwusage_region_item_data in self.bwusage_region:
                bwusage_region_item = bwusage_region_item_data.to_dict()
                bwusage_region.append(bwusage_region_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_region is not UNSET:
            field_dict["bwusageRegion"] = bwusage_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_enterprise_details_response_200_bwusage_details_bwusage_region_item import (
            PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem,
        )

        d = src_dict.copy()
        bwusage_region = []
        _bwusage_region = d.pop("bwusageRegion", UNSET)
        for bwusage_region_item_data in _bwusage_region or []:
            bwusage_region_item = PostV1BwtrackerEnterpriseDetailsResponse200BwusageDetailsBwusageRegionItem.from_dict(
                bwusage_region_item_data
            )

            bwusage_region.append(bwusage_region_item)

        post_v1_bwtracker_enterprise_details_response_200_bwusage_details = cls(
            bwusage_region=bwusage_region,
        )

        post_v1_bwtracker_enterprise_details_response_200_bwusage_details.additional_properties = d
        return post_v1_bwtracker_enterprise_details_response_200_bwusage_details

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
