from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_policy_prefix_sets_response_200_prefix_set import PostV1PolicyPrefixSetsResponse200PrefixSet


T = TypeVar("T", bound="PostV1PolicyPrefixSetsResponse200")


@_attrs_define
class PostV1PolicyPrefixSetsResponse200:
    """
    Attributes:
        prefix_set (Union[Unset, PostV1PolicyPrefixSetsResponse200PrefixSet]):
    """

    prefix_set: Union[Unset, "PostV1PolicyPrefixSetsResponse200PrefixSet"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prefix_set, Unset):
            prefix_set = self.prefix_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix_set is not UNSET:
            field_dict["prefixSet"] = prefix_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_policy_prefix_sets_response_200_prefix_set import (
            PostV1PolicyPrefixSetsResponse200PrefixSet,
        )

        d = src_dict.copy()
        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PostV1PolicyPrefixSetsResponse200PrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PostV1PolicyPrefixSetsResponse200PrefixSet.from_dict(_prefix_set)

        post_v1_policy_prefix_sets_response_200 = cls(
            prefix_set=prefix_set,
        )

        post_v1_policy_prefix_sets_response_200.additional_properties = d
        return post_v1_policy_prefix_sets_response_200

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
