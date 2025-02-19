from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem")


@_attrs_define
class PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem:
    """
    Attributes:
        end_time (Union[Unset, str]):  Example: TYPE_INT64.
        flow_count (Union[Unset, str]):  Example: TYPE_INT64.
        start_time (Union[Unset, str]):  Example: TYPE_INT64.
    """

    end_time: Union[Unset, str] = UNSET
    flow_count: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        flow_count = self.flow_count

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if flow_count is not UNSET:
            field_dict["flowCount"] = flow_count
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end_time = d.pop("endTime", UNSET)

        flow_count = d.pop("flowCount", UNSET)

        start_time = d.pop("startTime", UNSET)

        post_v2_assurance_bucketdetails_response_200_bucket_details_trend_value_list_item = cls(
            end_time=end_time,
            flow_count=flow_count,
            start_time=start_time,
        )

        post_v2_assurance_bucketdetails_response_200_bucket_details_trend_value_list_item.additional_properties = d
        return post_v2_assurance_bucketdetails_response_200_bucket_details_trend_value_list_item

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
