from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_prefix_sets_response_200_prefix_sets_item import (
        PostV1GlobalPrefixSetsResponse200PrefixSetsItem,
    )


T = TypeVar("T", bound="PostV1GlobalPrefixSetsResponse200")


@_attrs_define
class PostV1GlobalPrefixSetsResponse200:
    """
    Attributes:
        prefix_sets (Union[Unset, list['PostV1GlobalPrefixSetsResponse200PrefixSetsItem']]):
    """

    prefix_sets: Union[Unset, list["PostV1GlobalPrefixSetsResponse200PrefixSetsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_sets, Unset):
            prefix_sets = []
            for prefix_sets_item_data in self.prefix_sets:
                prefix_sets_item = prefix_sets_item_data.to_dict()
                prefix_sets.append(prefix_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix_sets is not UNSET:
            field_dict["prefixSets"] = prefix_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_prefix_sets_response_200_prefix_sets_item import (
            PostV1GlobalPrefixSetsResponse200PrefixSetsItem,
        )

        d = src_dict.copy()
        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PostV1GlobalPrefixSetsResponse200PrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        post_v1_global_prefix_sets_response_200 = cls(
            prefix_sets=prefix_sets,
        )

        post_v1_global_prefix_sets_response_200.additional_properties = d
        return post_v1_global_prefix_sets_response_200

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
