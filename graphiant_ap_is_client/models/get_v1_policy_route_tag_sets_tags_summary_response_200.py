from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_policy_route_tag_sets_tags_summary_response_200_tags_item import (
        GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem,
    )


T = TypeVar("T", bound="GetV1PolicyRouteTagSetsTagsSummaryResponse200")


@_attrs_define
class GetV1PolicyRouteTagSetsTagsSummaryResponse200:
    """
    Attributes:
        tags (Union[Unset, list['GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem']]):
    """

    tags: Union[Unset, list["GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_policy_route_tag_sets_tags_summary_response_200_tags_item import (
            GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem,
        )

        d = src_dict.copy()
        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = GetV1PolicyRouteTagSetsTagsSummaryResponse200TagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        get_v1_policy_route_tag_sets_tags_summary_response_200 = cls(
            tags=tags,
        )

        get_v1_policy_route_tag_sets_tags_summary_response_200.additional_properties = d
        return get_v1_policy_route_tag_sets_tags_summary_response_200

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
