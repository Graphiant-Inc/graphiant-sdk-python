from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary import (
        PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeSummaryResponse200")


@_attrs_define
class PostV1BwtrackerRegionEdgeSummaryResponse200:
    """
    Attributes:
        bwusage_summary (Union[Unset, PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary]):
    """

    bwusage_summary: Union[Unset, "PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bwusage_summary, Unset):
            bwusage_summary = self.bwusage_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_summary is not UNSET:
            field_dict["bwusageSummary"] = bwusage_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_edge_summary_response_200_bwusage_summary import (
            PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary,
        )

        d = src_dict.copy()
        _bwusage_summary = d.pop("bwusageSummary", UNSET)
        bwusage_summary: Union[Unset, PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary]
        if isinstance(_bwusage_summary, Unset):
            bwusage_summary = UNSET
        else:
            bwusage_summary = PostV1BwtrackerRegionEdgeSummaryResponse200BwusageSummary.from_dict(_bwusage_summary)

        post_v1_bwtracker_region_edge_summary_response_200 = cls(
            bwusage_summary=bwusage_summary,
        )

        post_v1_bwtracker_region_edge_summary_response_200.additional_properties = d
        return post_v1_bwtracker_region_edge_summary_response_200

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
