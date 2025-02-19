from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem")


@_attrs_define
class GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem:
    """
    Attributes:
        device_count (Union[Unset, str]):  Example: TYPE_INT32.
        level_one (Union[Unset, str]):  Example: TYPE_INT64.
        level_one_tag (Union[Unset, str]):  Example: TYPE_STRING.
        level_two (Union[Unset, str]):  Example: TYPE_INT64.
        level_two_tag (Union[Unset, str]):  Example: TYPE_STRING.
        level_zero (Union[Unset, str]):  Example: TYPE_INT64.
        level_zero_tag (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_count: Union[Unset, str] = UNSET
    level_one: Union[Unset, str] = UNSET
    level_one_tag: Union[Unset, str] = UNSET
    level_two: Union[Unset, str] = UNSET
    level_two_tag: Union[Unset, str] = UNSET
    level_zero: Union[Unset, str] = UNSET
    level_zero_tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_count = self.device_count

        level_one = self.level_one

        level_one_tag = self.level_one_tag

        level_two = self.level_two

        level_two_tag = self.level_two_tag

        level_zero = self.level_zero

        level_zero_tag = self.level_zero_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_count is not UNSET:
            field_dict["deviceCount"] = device_count
        if level_one is not UNSET:
            field_dict["levelOne"] = level_one
        if level_one_tag is not UNSET:
            field_dict["levelOneTag"] = level_one_tag
        if level_two is not UNSET:
            field_dict["levelTwo"] = level_two
        if level_two_tag is not UNSET:
            field_dict["levelTwoTag"] = level_two_tag
        if level_zero is not UNSET:
            field_dict["levelZero"] = level_zero
        if level_zero_tag is not UNSET:
            field_dict["levelZeroTag"] = level_zero_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_count = d.pop("deviceCount", UNSET)

        level_one = d.pop("levelOne", UNSET)

        level_one_tag = d.pop("levelOneTag", UNSET)

        level_two = d.pop("levelTwo", UNSET)

        level_two_tag = d.pop("levelTwoTag", UNSET)

        level_zero = d.pop("levelZero", UNSET)

        level_zero_tag = d.pop("levelZeroTag", UNSET)

        get_v1_policy_route_tag_sets_tags_summary_response_200_tags_item = cls(
            device_count=device_count,
            level_one=level_one,
            level_one_tag=level_one_tag,
            level_two=level_two,
            level_two_tag=level_two_tag,
            level_zero=level_zero,
            level_zero_tag=level_zero_tag,
        )

        get_v1_policy_route_tag_sets_tags_summary_response_200_tags_item.additional_properties = d
        return get_v1_policy_route_tag_sets_tags_summary_response_200_tags_item

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
