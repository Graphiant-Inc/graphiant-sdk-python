from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item_action import (
        GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction,
    )
    from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item_match import (
        GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch,
    )


T = TypeVar("T", bound="GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItem")


@_attrs_define
class GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItem:
    """
    Attributes:
        action (Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        index (Union[Unset, str]):  Example: TYPE_UINT32.
        match (Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    action: Union[Unset, "GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction"] = (
        UNSET
    )
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    match: Union[Unset, "GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch"] = (
        UNSET
    )
    name: Union[Unset, str] = UNSET
    seq: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        description = self.description

        id = self.id

        index = self.index

        match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        name = self.name

        seq = self.seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if match is not UNSET:
            field_dict["match"] = match
        if name is not UNSET:
            field_dict["name"] = name
        if seq is not UNSET:
            field_dict["seq"] = seq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item_action import (
            GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction,
        )
        from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item_match import (
            GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch,
        )

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemAction.from_dict(
                _action
            )

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        _match = d.pop("match", UNSET)
        match: Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyTrafficRulesetsItemRulesItemMatch.from_dict(
                _match
            )

        name = d.pop("name", UNSET)

        seq = d.pop("seq", UNSET)

        get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item = cls(
            action=action,
            description=description,
            id=id,
            index=index,
            match=match,
            name=name,
            seq=seq,
        )

        get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item.additional_properties = d
        return get_v1_global_traffic_policies_site_response_200_traffic_policy_traffic_rulesets_item_rules_item

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
