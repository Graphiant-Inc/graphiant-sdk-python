from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_consumer_body_policy_item_rules_item import (
        PostV1ExtranetsB2BConsumerBodyPolicyItemRulesItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerBodyPolicyItem")


@_attrs_define
class PostV1ExtranetsB2BConsumerBodyPolicyItem:
    """
    Attributes:
        consumer_lan_segment (Union[Unset, str]):  Example: TYPE_INT64.
        restricted_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        rules (Union[Unset, list['PostV1ExtranetsB2BConsumerBodyPolicyItemRulesItem']]):
    """

    consumer_lan_segment: Union[Unset, str] = UNSET
    restricted_prefixes: Union[Unset, list[str]] = UNSET
    rules: Union[Unset, list["PostV1ExtranetsB2BConsumerBodyPolicyItemRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumer_lan_segment = self.consumer_lan_segment

        restricted_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.restricted_prefixes, Unset):
            restricted_prefixes = self.restricted_prefixes

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumer_lan_segment is not UNSET:
            field_dict["consumerLanSegment"] = consumer_lan_segment
        if restricted_prefixes is not UNSET:
            field_dict["restrictedPrefixes"] = restricted_prefixes
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_consumer_body_policy_item_rules_item import (
            PostV1ExtranetsB2BConsumerBodyPolicyItemRulesItem,
        )

        d = src_dict.copy()
        consumer_lan_segment = d.pop("consumerLanSegment", UNSET)

        restricted_prefixes = cast(list[str], d.pop("restrictedPrefixes", UNSET))

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = PostV1ExtranetsB2BConsumerBodyPolicyItemRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        post_v1_extranets_b2b_consumer_body_policy_item = cls(
            consumer_lan_segment=consumer_lan_segment,
            restricted_prefixes=restricted_prefixes,
            rules=rules,
        )

        post_v1_extranets_b2b_consumer_body_policy_item.additional_properties = d
        return post_v1_extranets_b2b_consumer_body_policy_item

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
