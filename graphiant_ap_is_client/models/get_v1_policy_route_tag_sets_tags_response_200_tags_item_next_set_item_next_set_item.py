from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_policy_route_tag_sets_tags_response_200_tags_item_next_set_item_next_set_item_next_set_item import (
        GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItemNextSetItem,
    )


T = TypeVar("T", bound="GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItem")


@_attrs_define
class GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        next_set (Union[Unset,
            list['GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItemNextSetItem']]):
        tag (Union[Unset, str]):  Example: TYPE_STRING.
        tag_value (Union[Unset, str]):  Example: TYPE_INT32.
    """

    id: Union[Unset, str] = UNSET
    next_set: Union[Unset, list["GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItemNextSetItem"]] = (
        UNSET
    )
    tag: Union[Unset, str] = UNSET
    tag_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        next_set: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.next_set, Unset):
            next_set = []
            for next_set_item_data in self.next_set:
                next_set_item = next_set_item_data.to_dict()
                next_set.append(next_set_item)

        tag = self.tag

        tag_value = self.tag_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if next_set is not UNSET:
            field_dict["nextSet"] = next_set
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tag_value is not UNSET:
            field_dict["tagValue"] = tag_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_policy_route_tag_sets_tags_response_200_tags_item_next_set_item_next_set_item_next_set_item import (
            GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItemNextSetItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        next_set = []
        _next_set = d.pop("nextSet", UNSET)
        for next_set_item_data in _next_set or []:
            next_set_item = GetV1PolicyRouteTagSetsTagsResponse200TagsItemNextSetItemNextSetItemNextSetItem.from_dict(
                next_set_item_data
            )

            next_set.append(next_set_item)

        tag = d.pop("tag", UNSET)

        tag_value = d.pop("tagValue", UNSET)

        get_v1_policy_route_tag_sets_tags_response_200_tags_item_next_set_item_next_set_item = cls(
            id=id,
            next_set=next_set,
            tag=tag,
            tag_value=tag_value,
        )

        get_v1_policy_route_tag_sets_tags_response_200_tags_item_next_set_item_next_set_item.additional_properties = d
        return get_v1_policy_route_tag_sets_tags_response_200_tags_item_next_set_item_next_set_item

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
