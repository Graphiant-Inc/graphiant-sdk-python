from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats",
)


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats:
    """
    Attributes:
        prev_unique_app_count (Union[Unset, str]):  Example: TYPE_INT64.
        prev_unique_threat_count (Union[Unset, str]):  Example: TYPE_INT64.
        unique_app_count (Union[Unset, str]):  Example: TYPE_INT64.
        unique_threat_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    prev_unique_app_count: Union[Unset, str] = UNSET
    prev_unique_threat_count: Union[Unset, str] = UNSET
    unique_app_count: Union[Unset, str] = UNSET
    unique_threat_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prev_unique_app_count = self.prev_unique_app_count

        prev_unique_threat_count = self.prev_unique_threat_count

        unique_app_count = self.unique_app_count

        unique_threat_count = self.unique_threat_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prev_unique_app_count is not UNSET:
            field_dict["prevUniqueAppCount"] = prev_unique_app_count
        if prev_unique_threat_count is not UNSET:
            field_dict["prevUniqueThreatCount"] = prev_unique_threat_count
        if unique_app_count is not UNSET:
            field_dict["uniqueAppCount"] = unique_app_count
        if unique_threat_count is not UNSET:
            field_dict["uniqueThreatCount"] = unique_threat_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        prev_unique_app_count = d.pop("prevUniqueAppCount", UNSET)

        prev_unique_threat_count = d.pop("prevUniqueThreatCount", UNSET)

        unique_app_count = d.pop("uniqueAppCount", UNSET)

        unique_threat_count = d.pop("uniqueThreatCount", UNSET)

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_bucket_stats = cls(
            prev_unique_app_count=prev_unique_app_count,
            prev_unique_threat_count=prev_unique_threat_count,
            unique_app_count=unique_app_count,
            unique_threat_count=unique_threat_count,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_bucket_stats.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_bucket_stats

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
