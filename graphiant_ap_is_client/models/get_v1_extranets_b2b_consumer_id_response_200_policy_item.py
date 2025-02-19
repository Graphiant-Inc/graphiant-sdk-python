from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_inbound_security_rules_item import (
        GetV1ExtranetsB2BConsumerIdResponse200PolicyItemInboundSecurityRulesItem,
    )
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_outbound_security_rules_item import (
        GetV1ExtranetsB2BConsumerIdResponse200PolicyItemOutboundSecurityRulesItem,
    )
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_rules_item import (
        GetV1ExtranetsB2BConsumerIdResponse200PolicyItemRulesItem,
    )
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_traffic_rules_item import (
        GetV1ExtranetsB2BConsumerIdResponse200PolicyItemTrafficRulesItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BConsumerIdResponse200PolicyItem")


@_attrs_define
class GetV1ExtranetsB2BConsumerIdResponse200PolicyItem:
    """
    Attributes:
        consumer_lan_segment (Union[Unset, str]):  Example: TYPE_INT64.
        inbound_security_rules (Union[Unset,
            list['GetV1ExtranetsB2BConsumerIdResponse200PolicyItemInboundSecurityRulesItem']]):
        outbound_security_rules (Union[Unset,
            list['GetV1ExtranetsB2BConsumerIdResponse200PolicyItemOutboundSecurityRulesItem']]):
        restricted_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        rules (Union[Unset, list['GetV1ExtranetsB2BConsumerIdResponse200PolicyItemRulesItem']]):
        traffic_rules (Union[Unset, list['GetV1ExtranetsB2BConsumerIdResponse200PolicyItemTrafficRulesItem']]):
    """

    consumer_lan_segment: Union[Unset, str] = UNSET
    inbound_security_rules: Union[
        Unset, list["GetV1ExtranetsB2BConsumerIdResponse200PolicyItemInboundSecurityRulesItem"]
    ] = UNSET
    outbound_security_rules: Union[
        Unset, list["GetV1ExtranetsB2BConsumerIdResponse200PolicyItemOutboundSecurityRulesItem"]
    ] = UNSET
    restricted_prefixes: Union[Unset, list[str]] = UNSET
    rules: Union[Unset, list["GetV1ExtranetsB2BConsumerIdResponse200PolicyItemRulesItem"]] = UNSET
    traffic_rules: Union[Unset, list["GetV1ExtranetsB2BConsumerIdResponse200PolicyItemTrafficRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumer_lan_segment = self.consumer_lan_segment

        inbound_security_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inbound_security_rules, Unset):
            inbound_security_rules = []
            for inbound_security_rules_item_data in self.inbound_security_rules:
                inbound_security_rules_item = inbound_security_rules_item_data.to_dict()
                inbound_security_rules.append(inbound_security_rules_item)

        outbound_security_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.outbound_security_rules, Unset):
            outbound_security_rules = []
            for outbound_security_rules_item_data in self.outbound_security_rules:
                outbound_security_rules_item = outbound_security_rules_item_data.to_dict()
                outbound_security_rules.append(outbound_security_rules_item)

        restricted_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.restricted_prefixes, Unset):
            restricted_prefixes = self.restricted_prefixes

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        traffic_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_rules, Unset):
            traffic_rules = []
            for traffic_rules_item_data in self.traffic_rules:
                traffic_rules_item = traffic_rules_item_data.to_dict()
                traffic_rules.append(traffic_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumer_lan_segment is not UNSET:
            field_dict["consumerLanSegment"] = consumer_lan_segment
        if inbound_security_rules is not UNSET:
            field_dict["inboundSecurityRules"] = inbound_security_rules
        if outbound_security_rules is not UNSET:
            field_dict["outboundSecurityRules"] = outbound_security_rules
        if restricted_prefixes is not UNSET:
            field_dict["restrictedPrefixes"] = restricted_prefixes
        if rules is not UNSET:
            field_dict["rules"] = rules
        if traffic_rules is not UNSET:
            field_dict["trafficRules"] = traffic_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_inbound_security_rules_item import (
            GetV1ExtranetsB2BConsumerIdResponse200PolicyItemInboundSecurityRulesItem,
        )
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_outbound_security_rules_item import (
            GetV1ExtranetsB2BConsumerIdResponse200PolicyItemOutboundSecurityRulesItem,
        )
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_rules_item import (
            GetV1ExtranetsB2BConsumerIdResponse200PolicyItemRulesItem,
        )
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item_traffic_rules_item import (
            GetV1ExtranetsB2BConsumerIdResponse200PolicyItemTrafficRulesItem,
        )

        d = src_dict.copy()
        consumer_lan_segment = d.pop("consumerLanSegment", UNSET)

        inbound_security_rules = []
        _inbound_security_rules = d.pop("inboundSecurityRules", UNSET)
        for inbound_security_rules_item_data in _inbound_security_rules or []:
            inbound_security_rules_item = (
                GetV1ExtranetsB2BConsumerIdResponse200PolicyItemInboundSecurityRulesItem.from_dict(
                    inbound_security_rules_item_data
                )
            )

            inbound_security_rules.append(inbound_security_rules_item)

        outbound_security_rules = []
        _outbound_security_rules = d.pop("outboundSecurityRules", UNSET)
        for outbound_security_rules_item_data in _outbound_security_rules or []:
            outbound_security_rules_item = (
                GetV1ExtranetsB2BConsumerIdResponse200PolicyItemOutboundSecurityRulesItem.from_dict(
                    outbound_security_rules_item_data
                )
            )

            outbound_security_rules.append(outbound_security_rules_item)

        restricted_prefixes = cast(list[str], d.pop("restrictedPrefixes", UNSET))

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = GetV1ExtranetsB2BConsumerIdResponse200PolicyItemRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        traffic_rules = []
        _traffic_rules = d.pop("trafficRules", UNSET)
        for traffic_rules_item_data in _traffic_rules or []:
            traffic_rules_item = GetV1ExtranetsB2BConsumerIdResponse200PolicyItemTrafficRulesItem.from_dict(
                traffic_rules_item_data
            )

            traffic_rules.append(traffic_rules_item)

        get_v1_extranets_b2b_consumer_id_response_200_policy_item = cls(
            consumer_lan_segment=consumer_lan_segment,
            inbound_security_rules=inbound_security_rules,
            outbound_security_rules=outbound_security_rules,
            restricted_prefixes=restricted_prefixes,
            rules=rules,
            traffic_rules=traffic_rules,
        )

        get_v1_extranets_b2b_consumer_id_response_200_policy_item.additional_properties = d
        return get_v1_extranets_b2b_consumer_id_response_200_policy_item

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
