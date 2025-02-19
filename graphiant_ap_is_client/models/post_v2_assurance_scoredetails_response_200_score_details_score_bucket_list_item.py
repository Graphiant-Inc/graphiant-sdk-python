from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem")


@_attrs_define
class PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem:
    """
    Attributes:
        curr_score (Union[Unset, str]):  Example: TYPE_INT64.
        max_score (Union[Unset, str]):  Example: TYPE_INT64.
        score_bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    curr_score: Union[Unset, str] = UNSET
    max_score: Union[Unset, str] = UNSET
    score_bucket_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        curr_score = self.curr_score

        max_score = self.max_score

        score_bucket_id = self.score_bucket_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curr_score is not UNSET:
            field_dict["currScore"] = curr_score
        if max_score is not UNSET:
            field_dict["maxScore"] = max_score
        if score_bucket_id is not UNSET:
            field_dict["scoreBucketId"] = score_bucket_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        curr_score = d.pop("currScore", UNSET)

        max_score = d.pop("maxScore", UNSET)

        score_bucket_id = d.pop("scoreBucketId", UNSET)

        post_v2_assurance_scoredetails_response_200_score_details_score_bucket_list_item = cls(
            curr_score=curr_score,
            max_score=max_score,
            score_bucket_id=score_bucket_id,
        )

        post_v2_assurance_scoredetails_response_200_score_details_score_bucket_list_item.additional_properties = d
        return post_v2_assurance_scoredetails_response_200_score_details_score_bucket_list_item

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
