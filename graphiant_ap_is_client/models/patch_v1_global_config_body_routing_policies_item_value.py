from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_routing_policies_item_value_policy import (
        PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyRoutingPoliciesItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyRoutingPoliciesItemValue:
    """
    Attributes:
        policy (Union[Unset, PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy]):
    """

    policy: Union[Unset, "PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_routing_policies_item_value_policy import (
            PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy,
        )

        d = src_dict.copy()
        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy.from_dict(_policy)

        patch_v1_global_config_body_routing_policies_item_value = cls(
            policy=policy,
        )

        patch_v1_global_config_body_routing_policies_item_value.additional_properties = d
        return patch_v1_global_config_body_routing_policies_item_value

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
