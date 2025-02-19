from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_policy_route_tag_sets_body_tag import PostV1PolicyRouteTagSetsBodyTag


T = TypeVar("T", bound="PostV1PolicyRouteTagSetsBody")


@_attrs_define
class PostV1PolicyRouteTagSetsBody:
    """
    Attributes:
        tag (Union[Unset, PostV1PolicyRouteTagSetsBodyTag]):
    """

    tag: Union[Unset, "PostV1PolicyRouteTagSetsBodyTag"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_policy_route_tag_sets_body_tag import PostV1PolicyRouteTagSetsBodyTag

        d = src_dict.copy()
        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, PostV1PolicyRouteTagSetsBodyTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = PostV1PolicyRouteTagSetsBodyTag.from_dict(_tag)

        post_v1_policy_route_tag_sets_body = cls(
            tag=tag,
        )

        post_v1_policy_route_tag_sets_body.additional_properties = d
        return post_v1_policy_route_tag_sets_body

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
