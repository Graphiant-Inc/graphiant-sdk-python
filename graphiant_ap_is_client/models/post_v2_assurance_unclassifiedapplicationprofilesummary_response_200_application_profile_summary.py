from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item import (
        PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem,
    )


T = TypeVar("T", bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary")


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummary:
    """
    Attributes:
        bucket_summary_list (Union[Unset, list['PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200Applicati
            onProfileSummaryBucketSummaryListItem']]):
    """

    bucket_summary_list: Union[
        Unset,
        list[
            "PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_summary_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bucket_summary_list, Unset):
            bucket_summary_list = []
            for bucket_summary_list_item_data in self.bucket_summary_list:
                bucket_summary_list_item = bucket_summary_list_item_data.to_dict()
                bucket_summary_list.append(bucket_summary_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_summary_list is not UNSET:
            field_dict["bucketSummaryList"] = bucket_summary_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item import (
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem,
        )

        d = src_dict.copy()
        bucket_summary_list = []
        _bucket_summary_list = d.pop("bucketSummaryList", UNSET)
        for bucket_summary_list_item_data in _bucket_summary_list or []:
            bucket_summary_list_item = PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem.from_dict(
                bucket_summary_list_item_data
            )

            bucket_summary_list.append(bucket_summary_list_item)

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary = cls(
            bucket_summary_list=bucket_summary_list,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary

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
