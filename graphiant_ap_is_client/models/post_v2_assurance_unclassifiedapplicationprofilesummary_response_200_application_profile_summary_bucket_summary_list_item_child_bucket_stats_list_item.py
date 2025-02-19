from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem",
)


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem:
    """
    Attributes:
        assurance_bucket (Union[Unset, str]):  Example: TYPE_ENUM.
        bucket_name_to_display (Union[Unset, str]):  Example: TYPE_STRING.
        prev_unique_app_count (Union[Unset, str]):  Example: TYPE_INT64.
        unique_app_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    assurance_bucket: Union[Unset, str] = UNSET
    bucket_name_to_display: Union[Unset, str] = UNSET
    prev_unique_app_count: Union[Unset, str] = UNSET
    unique_app_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assurance_bucket = self.assurance_bucket

        bucket_name_to_display = self.bucket_name_to_display

        prev_unique_app_count = self.prev_unique_app_count

        unique_app_count = self.unique_app_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assurance_bucket is not UNSET:
            field_dict["assuranceBucket"] = assurance_bucket
        if bucket_name_to_display is not UNSET:
            field_dict["bucketNameToDisplay"] = bucket_name_to_display
        if prev_unique_app_count is not UNSET:
            field_dict["prevUniqueAppCount"] = prev_unique_app_count
        if unique_app_count is not UNSET:
            field_dict["uniqueAppCount"] = unique_app_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        assurance_bucket = d.pop("assuranceBucket", UNSET)

        bucket_name_to_display = d.pop("bucketNameToDisplay", UNSET)

        prev_unique_app_count = d.pop("prevUniqueAppCount", UNSET)

        unique_app_count = d.pop("uniqueAppCount", UNSET)

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_child_bucket_stats_list_item = cls(
            assurance_bucket=assurance_bucket,
            bucket_name_to_display=bucket_name_to_display,
            prev_unique_app_count=prev_unique_app_count,
            unique_app_count=unique_app_count,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_child_bucket_stats_list_item.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_child_bucket_stats_list_item

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
