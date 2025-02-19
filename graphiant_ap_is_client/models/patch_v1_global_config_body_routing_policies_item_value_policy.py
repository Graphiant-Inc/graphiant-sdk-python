from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_routing_policies_item_value_policy_statements_item import (
        PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicyStatementsItem,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy")


@_attrs_define
class PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicy:
    """
    Attributes:
        attach_point (Union[Unset, str]):  Example: TYPE_ENUM.
        default_action (Union[Unset, str]):  Example: TYPE_ENUM.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_global_sync (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        statements (Union[Unset, list['PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicyStatementsItem']]):
    """

    attach_point: Union[Unset, str] = UNSET
    default_action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    is_global_sync: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    statements: Union[Unset, list["PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicyStatementsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attach_point = self.attach_point

        default_action = self.default_action

        description = self.description

        global_id = self.global_id

        is_global_sync = self.is_global_sync

        name = self.name

        statements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attach_point is not UNSET:
            field_dict["attachPoint"] = attach_point
        if default_action is not UNSET:
            field_dict["defaultAction"] = default_action
        if description is not UNSET:
            field_dict["description"] = description
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if is_global_sync is not UNSET:
            field_dict["isGlobalSync"] = is_global_sync
        if name is not UNSET:
            field_dict["name"] = name
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_routing_policies_item_value_policy_statements_item import (
            PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicyStatementsItem,
        )

        d = src_dict.copy()
        attach_point = d.pop("attachPoint", UNSET)

        default_action = d.pop("defaultAction", UNSET)

        description = d.pop("description", UNSET)

        global_id = d.pop("globalId", UNSET)

        is_global_sync = d.pop("isGlobalSync", UNSET)

        name = d.pop("name", UNSET)

        statements = []
        _statements = d.pop("statements", UNSET)
        for statements_item_data in _statements or []:
            statements_item = PatchV1GlobalConfigBodyRoutingPoliciesItemValuePolicyStatementsItem.from_dict(
                statements_item_data
            )

            statements.append(statements_item)

        patch_v1_global_config_body_routing_policies_item_value_policy = cls(
            attach_point=attach_point,
            default_action=default_action,
            description=description,
            global_id=global_id,
            is_global_sync=is_global_sync,
            name=name,
            statements=statements,
        )

        patch_v1_global_config_body_routing_policies_item_value_policy.additional_properties = d
        return patch_v1_global_config_body_routing_policies_item_value_policy

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
