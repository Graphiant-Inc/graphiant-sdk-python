from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_source_segments_body_target import PostV1ExtranetsSourceSegmentsBodyTarget


T = TypeVar("T", bound="PostV1ExtranetsSourceSegmentsBody")


@_attrs_define
class PostV1ExtranetsSourceSegmentsBody:
    """
    Attributes:
        filter_ (Union[Unset, str]):  Example: TYPE_STRING.
        target (Union[Unset, PostV1ExtranetsSourceSegmentsBodyTarget]):
    """

    filter_: Union[Unset, str] = UNSET
    target: Union[Unset, "PostV1ExtranetsSourceSegmentsBodyTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_source_segments_body_target import PostV1ExtranetsSourceSegmentsBodyTarget

        d = src_dict.copy()
        filter_ = d.pop("filter", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PostV1ExtranetsSourceSegmentsBodyTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PostV1ExtranetsSourceSegmentsBodyTarget.from_dict(_target)

        post_v1_extranets_source_segments_body = cls(
            filter_=filter_,
            target=target,
        )

        post_v1_extranets_source_segments_body.additional_properties = d
        return post_v1_extranets_source_segments_body

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
