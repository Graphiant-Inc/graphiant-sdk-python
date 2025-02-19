from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_one import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_two import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_zero import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero,
    )


T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTag")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTag:
    """
    Attributes:
        level_one (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne]):
        level_two (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo]):
        level_zero (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero]):
    """

    level_one: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne"] = UNSET
    level_two: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo"] = UNSET
    level_zero: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level_one: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_one, Unset):
            level_one = self.level_one.to_dict()

        level_two: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_two, Unset):
            level_two = self.level_two.to_dict()

        level_zero: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_zero, Unset):
            level_zero = self.level_zero.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level_one is not UNSET:
            field_dict["levelOne"] = level_one
        if level_two is not UNSET:
            field_dict["levelTwo"] = level_two
        if level_zero is not UNSET:
            field_dict["levelZero"] = level_zero

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_one import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_two import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag_level_zero import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero,
        )

        d = src_dict.copy()
        _level_one = d.pop("levelOne", UNSET)
        level_one: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne]
        if isinstance(_level_one, Unset):
            level_one = UNSET
        else:
            level_one = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelOne.from_dict(
                _level_one
            )

        _level_two = d.pop("levelTwo", UNSET)
        level_two: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo]
        if isinstance(_level_two, Unset):
            level_two = UNSET
        else:
            level_two = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelTwo.from_dict(
                _level_two
            )

        _level_zero = d.pop("levelZero", UNSET)
        level_zero: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero]
        if isinstance(_level_zero, Unset):
            level_zero = UNSET
        else:
            level_zero = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSitePolicyTagLevelZero.from_dict(
                _level_zero
            )

        post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag = cls(
            level_one=level_one,
            level_two=level_two,
            level_zero=level_zero,
        )

        post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag.additional_properties = d
        return post_v1_extranets_resolve_policy_target_response_200_devices_item_site_policy_tag

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
