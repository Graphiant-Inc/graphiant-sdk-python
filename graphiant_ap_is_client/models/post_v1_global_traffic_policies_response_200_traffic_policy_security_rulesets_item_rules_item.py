from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item_rules_item_match import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch,
    )


T = TypeVar("T", bound="PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItem")


@_attrs_define
class PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItem:
    """
    Attributes:
        action (Union[Unset, str]):  Example: TYPE_ENUM.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        downlink_burst_rate (Union[Unset, str]):  Example: TYPE_UINT32.
        downlink_policer_rate (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        index (Union[Unset, str]):  Example: TYPE_UINT32.
        logging (Union[Unset, str]):  Example: TYPE_BOOL.
        match (Union[Unset, PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
        uplink_burst_rate (Union[Unset, str]):  Example: TYPE_UINT32.
        uplink_policer_rate (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    downlink_burst_rate: Union[Unset, str] = UNSET
    downlink_policer_rate: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    logging: Union[Unset, str] = UNSET
    match: Union[Unset, "PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch"] = UNSET
    name: Union[Unset, str] = UNSET
    seq: Union[Unset, str] = UNSET
    uplink_burst_rate: Union[Unset, str] = UNSET
    uplink_policer_rate: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        description = self.description

        downlink_burst_rate = self.downlink_burst_rate

        downlink_policer_rate = self.downlink_policer_rate

        id = self.id

        index = self.index

        logging = self.logging

        match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        name = self.name

        seq = self.seq

        uplink_burst_rate = self.uplink_burst_rate

        uplink_policer_rate = self.uplink_policer_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if downlink_burst_rate is not UNSET:
            field_dict["downlinkBurstRate"] = downlink_burst_rate
        if downlink_policer_rate is not UNSET:
            field_dict["downlinkPolicerRate"] = downlink_policer_rate
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if logging is not UNSET:
            field_dict["logging"] = logging
        if match is not UNSET:
            field_dict["match"] = match
        if name is not UNSET:
            field_dict["name"] = name
        if seq is not UNSET:
            field_dict["seq"] = seq
        if uplink_burst_rate is not UNSET:
            field_dict["uplinkBurstRate"] = uplink_burst_rate
        if uplink_policer_rate is not UNSET:
            field_dict["uplinkPolicerRate"] = uplink_policer_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item_rules_item_match import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch,
        )

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        description = d.pop("description", UNSET)

        downlink_burst_rate = d.pop("downlinkBurstRate", UNSET)

        downlink_policer_rate = d.pop("downlinkPolicerRate", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        logging = d.pop("logging", UNSET)

        _match = d.pop("match", UNSET)
        match: Union[Unset, PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItemRulesItemMatch.from_dict(
                _match
            )

        name = d.pop("name", UNSET)

        seq = d.pop("seq", UNSET)

        uplink_burst_rate = d.pop("uplinkBurstRate", UNSET)

        uplink_policer_rate = d.pop("uplinkPolicerRate", UNSET)

        post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item_rules_item = cls(
            action=action,
            description=description,
            downlink_burst_rate=downlink_burst_rate,
            downlink_policer_rate=downlink_policer_rate,
            id=id,
            index=index,
            logging=logging,
            match=match,
            name=name,
            seq=seq,
            uplink_burst_rate=uplink_burst_rate,
            uplink_policer_rate=uplink_policer_rate,
        )

        post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item_rules_item.additional_properties = d
        return post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item_rules_item

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
