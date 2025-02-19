from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_scoredetails_response_200_score_details_score_bucket_list_item import (
        PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem,
    )


T = TypeVar("T", bound="PostV2AssuranceScoredetailsResponse200ScoreDetails")


@_attrs_define
class PostV2AssuranceScoredetailsResponse200ScoreDetails:
    """
    Attributes:
        score_bucket_list (Union[Unset, list['PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem']]):
    """

    score_bucket_list: Union[Unset, list["PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score_bucket_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.score_bucket_list, Unset):
            score_bucket_list = []
            for score_bucket_list_item_data in self.score_bucket_list:
                score_bucket_list_item = score_bucket_list_item_data.to_dict()
                score_bucket_list.append(score_bucket_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score_bucket_list is not UNSET:
            field_dict["scoreBucketList"] = score_bucket_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_scoredetails_response_200_score_details_score_bucket_list_item import (
            PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem,
        )

        d = src_dict.copy()
        score_bucket_list = []
        _score_bucket_list = d.pop("scoreBucketList", UNSET)
        for score_bucket_list_item_data in _score_bucket_list or []:
            score_bucket_list_item = PostV2AssuranceScoredetailsResponse200ScoreDetailsScoreBucketListItem.from_dict(
                score_bucket_list_item_data
            )

            score_bucket_list.append(score_bucket_list_item)

        post_v2_assurance_scoredetails_response_200_score_details = cls(
            score_bucket_list=score_bucket_list,
        )

        post_v2_assurance_scoredetails_response_200_score_details.additional_properties = d
        return post_v2_assurance_scoredetails_response_200_score_details

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
