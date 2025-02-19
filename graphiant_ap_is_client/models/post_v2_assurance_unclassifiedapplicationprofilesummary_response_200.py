from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary import (
        PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary,
    )


T = TypeVar("T", bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200")


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200:
    """
    Attributes:
        application_profile_summary (Union[Unset,
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary]):
    """

    application_profile_summary: Union[
        Unset, "PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_profile_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.application_profile_summary, Unset):
            application_profile_summary = self.application_profile_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_profile_summary is not UNSET:
            field_dict["applicationProfileSummary"] = application_profile_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary import (
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary,
        )

        d = src_dict.copy()
        _application_profile_summary = d.pop("applicationProfileSummary", UNSET)
        application_profile_summary: Union[
            Unset, PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary
        ]
        if isinstance(_application_profile_summary, Unset):
            application_profile_summary = UNSET
        else:
            application_profile_summary = (
                PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary.from_dict(
                    _application_profile_summary
                )
            )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200 = cls(
            application_profile_summary=application_profile_summary,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_response_200

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
