from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_site_csv_response_200_bwusage_csv_details import (
        PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails,
    )


T = TypeVar("T", bound="PostV1BwtrackerSiteCsvResponse200")


@_attrs_define
class PostV1BwtrackerSiteCsvResponse200:
    """
    Attributes:
        bwusage_csv_details (Union[Unset, PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails]):
    """

    bwusage_csv_details: Union[Unset, "PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_csv_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bwusage_csv_details, Unset):
            bwusage_csv_details = self.bwusage_csv_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_csv_details is not UNSET:
            field_dict["bwusageCsvDetails"] = bwusage_csv_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_site_csv_response_200_bwusage_csv_details import (
            PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails,
        )

        d = src_dict.copy()
        _bwusage_csv_details = d.pop("bwusageCsvDetails", UNSET)
        bwusage_csv_details: Union[Unset, PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails]
        if isinstance(_bwusage_csv_details, Unset):
            bwusage_csv_details = UNSET
        else:
            bwusage_csv_details = PostV1BwtrackerSiteCsvResponse200BwusageCsvDetails.from_dict(_bwusage_csv_details)

        post_v1_bwtracker_site_csv_response_200 = cls(
            bwusage_csv_details=bwusage_csv_details,
        )

        post_v1_bwtracker_site_csv_response_200.additional_properties = d
        return post_v1_bwtracker_site_csv_response_200

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
