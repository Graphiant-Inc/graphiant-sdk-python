from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_traffic_rulesets_item_value_ruleset import (
        PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValue:
    """
    Attributes:
        ruleset (Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset]):
    """

    ruleset: Union[Unset, "PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ruleset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ruleset, Unset):
            ruleset = self.ruleset.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_traffic_rulesets_item_value_ruleset import (
            PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset,
        )

        d = src_dict.copy()
        _ruleset = d.pop("ruleset", UNSET)
        ruleset: Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset]
        if isinstance(_ruleset, Unset):
            ruleset = UNSET
        else:
            ruleset = PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItemValueRuleset.from_dict(_ruleset)

        patch_v1_global_config_body_traffic_policies_traffic_rulesets_item_value = cls(
            ruleset=ruleset,
        )

        patch_v1_global_config_body_traffic_policies_traffic_rulesets_item_value.additional_properties = d
        return patch_v1_global_config_body_traffic_policies_traffic_rulesets_item_value

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
