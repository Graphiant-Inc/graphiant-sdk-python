from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_nat_policy_nat_policy_rulesets_item_rules_item import (
        PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItemRulesItem,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItem")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        rules (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItemRulesItem']]):
    """

    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rules: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItemRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_nat_policy_nat_policy_rulesets_item_rules_item import (
            PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItemRulesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = PostV1DevicesDeviceIdDraftBodyDraftNatPolicyNatPolicyRulesetsItemRulesItem.from_dict(
                rules_item_data
            )

            rules.append(rules_item)

        post_v1_devices_device_id_draft_body_draft_nat_policy_nat_policy_rulesets_item = cls(
            description=description,
            id=id,
            name=name,
            rules=rules,
        )

        post_v1_devices_device_id_draft_body_draft_nat_policy_nat_policy_rulesets_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_nat_policy_nat_policy_rulesets_item

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
