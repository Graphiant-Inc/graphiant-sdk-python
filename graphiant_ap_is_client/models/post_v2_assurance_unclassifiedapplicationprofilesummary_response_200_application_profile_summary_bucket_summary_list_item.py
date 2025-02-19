from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_bucket_stats import (
        PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats,
    )
    from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_child_bucket_stats_list_item import (
        PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem,
    )


T = TypeVar(
    "T",
    bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem",
)


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItem:
    """
    Attributes:
        assurance_bucket (Union[Unset, str]):  Example: TYPE_ENUM.
        bucket_color (Union[Unset, str]):  Example: TYPE_ENUM.
        bucket_name_to_display (Union[Unset, str]):  Example: TYPE_STRING.
        bucket_stats (Union[Unset, PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSumm
            aryBucketSummaryListItemBucketStats]):
        child_bucket_list (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
        child_bucket_stats_list (Union[Unset, list['PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200Appli
            cationProfileSummaryBucketSummaryListItemChildBucketStatsListItem']]):
        is_root (Union[Unset, str]):  Example: TYPE_BOOL.
        is_terminal (Union[Unset, str]):  Example: TYPE_BOOL.
        parent_bucket_list (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
    """

    assurance_bucket: Union[Unset, str] = UNSET
    bucket_color: Union[Unset, str] = UNSET
    bucket_name_to_display: Union[Unset, str] = UNSET
    bucket_stats: Union[
        Unset,
        "PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats",
    ] = UNSET
    child_bucket_list: Union[Unset, list[str]] = UNSET
    child_bucket_stats_list: Union[
        Unset,
        list[
            "PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem"
        ],
    ] = UNSET
    is_root: Union[Unset, str] = UNSET
    is_terminal: Union[Unset, str] = UNSET
    parent_bucket_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assurance_bucket = self.assurance_bucket

        bucket_color = self.bucket_color

        bucket_name_to_display = self.bucket_name_to_display

        bucket_stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_stats, Unset):
            bucket_stats = self.bucket_stats.to_dict()

        child_bucket_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.child_bucket_list, Unset):
            child_bucket_list = self.child_bucket_list

        child_bucket_stats_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.child_bucket_stats_list, Unset):
            child_bucket_stats_list = []
            for child_bucket_stats_list_item_data in self.child_bucket_stats_list:
                child_bucket_stats_list_item = child_bucket_stats_list_item_data.to_dict()
                child_bucket_stats_list.append(child_bucket_stats_list_item)

        is_root = self.is_root

        is_terminal = self.is_terminal

        parent_bucket_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.parent_bucket_list, Unset):
            parent_bucket_list = self.parent_bucket_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assurance_bucket is not UNSET:
            field_dict["assuranceBucket"] = assurance_bucket
        if bucket_color is not UNSET:
            field_dict["bucketColor"] = bucket_color
        if bucket_name_to_display is not UNSET:
            field_dict["bucketNameToDisplay"] = bucket_name_to_display
        if bucket_stats is not UNSET:
            field_dict["bucketStats"] = bucket_stats
        if child_bucket_list is not UNSET:
            field_dict["childBucketList"] = child_bucket_list
        if child_bucket_stats_list is not UNSET:
            field_dict["childBucketStatsList"] = child_bucket_stats_list
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root
        if is_terminal is not UNSET:
            field_dict["isTerminal"] = is_terminal
        if parent_bucket_list is not UNSET:
            field_dict["parentBucketList"] = parent_bucket_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_bucket_stats import (
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats,
        )
        from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item_child_bucket_stats_list_item import (
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem,
        )

        d = src_dict.copy()
        assurance_bucket = d.pop("assuranceBucket", UNSET)

        bucket_color = d.pop("bucketColor", UNSET)

        bucket_name_to_display = d.pop("bucketNameToDisplay", UNSET)

        _bucket_stats = d.pop("bucketStats", UNSET)
        bucket_stats: Union[
            Unset,
            PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats,
        ]
        if isinstance(_bucket_stats, Unset):
            bucket_stats = UNSET
        else:
            bucket_stats = PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemBucketStats.from_dict(
                _bucket_stats
            )

        child_bucket_list = cast(list[str], d.pop("childBucketList", UNSET))

        child_bucket_stats_list = []
        _child_bucket_stats_list = d.pop("childBucketStatsList", UNSET)
        for child_bucket_stats_list_item_data in _child_bucket_stats_list or []:
            child_bucket_stats_list_item = PostV2AssuranceUnclassifiedapplicationprofilesummaryResponse200ApplicationProfileSummaryBucketSummaryListItemChildBucketStatsListItem.from_dict(
                child_bucket_stats_list_item_data
            )

            child_bucket_stats_list.append(child_bucket_stats_list_item)

        is_root = d.pop("isRoot", UNSET)

        is_terminal = d.pop("isTerminal", UNSET)

        parent_bucket_list = cast(list[str], d.pop("parentBucketList", UNSET))

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item = cls(
            assurance_bucket=assurance_bucket,
            bucket_color=bucket_color,
            bucket_name_to_display=bucket_name_to_display,
            bucket_stats=bucket_stats,
            child_bucket_list=child_bucket_list,
            child_bucket_stats_list=child_bucket_stats_list,
            is_root=is_root,
            is_terminal=is_terminal,
            parent_bucket_list=parent_bucket_list,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_response_200_application_profile_summary_bucket_summary_list_item

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
