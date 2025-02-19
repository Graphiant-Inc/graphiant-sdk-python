from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_enterprisesummary_response_200_enterprise_summary import (
        PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary,
    )


T = TypeVar("T", bound="PostV2AssuranceEnterprisesummaryResponse200")


@_attrs_define
class PostV2AssuranceEnterprisesummaryResponse200:
    """
    Attributes:
        enterprise_summary (Union[Unset, PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary]):
    """

    enterprise_summary: Union[Unset, "PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enterprise_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enterprise_summary, Unset):
            enterprise_summary = self.enterprise_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enterprise_summary is not UNSET:
            field_dict["enterpriseSummary"] = enterprise_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_enterprisesummary_response_200_enterprise_summary import (
            PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary,
        )

        d = src_dict.copy()
        _enterprise_summary = d.pop("enterpriseSummary", UNSET)
        enterprise_summary: Union[Unset, PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary]
        if isinstance(_enterprise_summary, Unset):
            enterprise_summary = UNSET
        else:
            enterprise_summary = PostV2AssuranceEnterprisesummaryResponse200EnterpriseSummary.from_dict(
                _enterprise_summary
            )

        post_v2_assurance_enterprisesummary_response_200 = cls(
            enterprise_summary=enterprise_summary,
        )

        post_v2_assurance_enterprisesummary_response_200.additional_properties = d
        return post_v2_assurance_enterprisesummary_response_200

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
