from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_resolve_policy_target_body_policy_target import (
        PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget,
    )


T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetBody")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetBody:
    """
    Attributes:
        policy_target (Union[Unset, PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget]):
    """

    policy_target: Union[Unset, "PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy_target, Unset):
            policy_target = self.policy_target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy_target is not UNSET:
            field_dict["policyTarget"] = policy_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_resolve_policy_target_body_policy_target import (
            PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget,
        )

        d = src_dict.copy()
        _policy_target = d.pop("policyTarget", UNSET)
        policy_target: Union[Unset, PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget]
        if isinstance(_policy_target, Unset):
            policy_target = UNSET
        else:
            policy_target = PostV1ExtranetsResolvePolicyTargetBodyPolicyTarget.from_dict(_policy_target)

        post_v1_extranets_resolve_policy_target_body = cls(
            policy_target=policy_target,
        )

        post_v1_extranets_resolve_policy_target_body.additional_properties = d
        return post_v1_extranets_resolve_policy_target_body

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
