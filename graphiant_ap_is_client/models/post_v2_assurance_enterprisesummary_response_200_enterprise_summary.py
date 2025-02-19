from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary")


@_attrs_define
class PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary:
    """
    Attributes:
        flows_analyzed (Union[Unset, str]):  Example: TYPE_INT64.
        gap_score (Union[Unset, str]):  Example: TYPE_INT64.
        prev_gap_score (Union[Unset, str]):  Example: TYPE_INT64.
        risk_bin (Union[Unset, str]):  Example: TYPE_INT64.
        threat_count (Union[Unset, str]):  Example: TYPE_INT64.
        unique_apps_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    flows_analyzed: Union[Unset, str] = UNSET
    gap_score: Union[Unset, str] = UNSET
    prev_gap_score: Union[Unset, str] = UNSET
    risk_bin: Union[Unset, str] = UNSET
    threat_count: Union[Unset, str] = UNSET
    unique_apps_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flows_analyzed = self.flows_analyzed

        gap_score = self.gap_score

        prev_gap_score = self.prev_gap_score

        risk_bin = self.risk_bin

        threat_count = self.threat_count

        unique_apps_count = self.unique_apps_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flows_analyzed is not UNSET:
            field_dict["flowsAnalyzed"] = flows_analyzed
        if gap_score is not UNSET:
            field_dict["gapScore"] = gap_score
        if prev_gap_score is not UNSET:
            field_dict["prevGapScore"] = prev_gap_score
        if risk_bin is not UNSET:
            field_dict["riskBin"] = risk_bin
        if threat_count is not UNSET:
            field_dict["threatCount"] = threat_count
        if unique_apps_count is not UNSET:
            field_dict["uniqueAppsCount"] = unique_apps_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        flows_analyzed = d.pop("flowsAnalyzed", UNSET)

        gap_score = d.pop("gapScore", UNSET)

        prev_gap_score = d.pop("prevGapScore", UNSET)

        risk_bin = d.pop("riskBin", UNSET)

        threat_count = d.pop("threatCount", UNSET)

        unique_apps_count = d.pop("uniqueAppsCount", UNSET)

        post_v2_assurance_enterprisesummary_response_200_enterprise_summary = cls(
            flows_analyzed=flows_analyzed,
            gap_score=gap_score,
            prev_gap_score=prev_gap_score,
            risk_bin=risk_bin,
            threat_count=threat_count,
            unique_apps_count=unique_apps_count,
        )

        post_v2_assurance_enterprisesummary_response_200_enterprise_summary.additional_properties = d
        return post_v2_assurance_enterprisesummary_response_200_enterprise_summary

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
