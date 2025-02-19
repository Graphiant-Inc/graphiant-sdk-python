from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details import (
        PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteDetailsResponse200")


@_attrs_define
class PostV1BwtrackerRegionSiteDetailsResponse200:
    """
    Attributes:
        bwusage_details (Union[Unset, PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails]):
    """

    bwusage_details: Union[Unset, "PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bwusage_details, Unset):
            bwusage_details = self.bwusage_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_details is not UNSET:
            field_dict["bwusageDetails"] = bwusage_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_details_response_200_bwusage_details import (
            PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails,
        )

        d = src_dict.copy()
        _bwusage_details = d.pop("bwusageDetails", UNSET)
        bwusage_details: Union[Unset, PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails]
        if isinstance(_bwusage_details, Unset):
            bwusage_details = UNSET
        else:
            bwusage_details = PostV1BwtrackerRegionSiteDetailsResponse200BwusageDetails.from_dict(_bwusage_details)

        post_v1_bwtracker_region_site_details_response_200 = cls(
            bwusage_details=bwusage_details,
        )

        post_v1_bwtracker_region_site_details_response_200.additional_properties = d
        return post_v1_bwtracker_region_site_details_response_200

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
