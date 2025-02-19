from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceEndpointIntelResponse200")


@_attrs_define
class PostV2AssuranceEndpointIntelResponse200:
    """
    Attributes:
        am_categories (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        am_risk_score (Union[Unset, str]):  Example: TYPE_FLOAT.
        graphiant_risky (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    am_categories: Union[Unset, list[str]] = UNSET
    am_risk_score: Union[Unset, str] = UNSET
    graphiant_risky: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        am_categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.am_categories, Unset):
            am_categories = self.am_categories

        am_risk_score = self.am_risk_score

        graphiant_risky = self.graphiant_risky

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if am_categories is not UNSET:
            field_dict["amCategories"] = am_categories
        if am_risk_score is not UNSET:
            field_dict["amRiskScore"] = am_risk_score
        if graphiant_risky is not UNSET:
            field_dict["graphiantRisky"] = graphiant_risky

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        am_categories = cast(list[str], d.pop("amCategories", UNSET))

        am_risk_score = d.pop("amRiskScore", UNSET)

        graphiant_risky = d.pop("graphiantRisky", UNSET)

        post_v2_assurance_endpoint_intel_response_200 = cls(
            am_categories=am_categories,
            am_risk_score=am_risk_score,
            graphiant_risky=graphiant_risky,
        )

        post_v2_assurance_endpoint_intel_response_200.additional_properties = d
        return post_v2_assurance_endpoint_intel_response_200

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
