from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_inbound_security_rules_item import (
        GetV1ExtranetsB2BIdProducerResponse200PolicyInboundSecurityRulesItem,
    )
    from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_policy import (
        GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy,
    )
    from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_traffic_rules_item import (
        GetV1ExtranetsB2BIdProducerResponse200PolicyTrafficRulesItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BIdProducerResponse200Policy")


@_attrs_define
class GetV1ExtranetsB2BIdProducerResponse200Policy:
    """
    Attributes:
        dns_name (Union[Unset, str]):  Example: TYPE_STRING.
        inbound_security_rules (Union[Unset,
            list['GetV1ExtranetsB2BIdProducerResponse200PolicyInboundSecurityRulesItem']]):
        policy (Union[Unset, GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy]):
        service_name (Union[Unset, str]):  Example: TYPE_STRING.
        traffic_rules (Union[Unset, list['GetV1ExtranetsB2BIdProducerResponse200PolicyTrafficRulesItem']]):
    """

    dns_name: Union[Unset, str] = UNSET
    inbound_security_rules: Union[
        Unset, list["GetV1ExtranetsB2BIdProducerResponse200PolicyInboundSecurityRulesItem"]
    ] = UNSET
    policy: Union[Unset, "GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy"] = UNSET
    service_name: Union[Unset, str] = UNSET
    traffic_rules: Union[Unset, list["GetV1ExtranetsB2BIdProducerResponse200PolicyTrafficRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_name = self.dns_name

        inbound_security_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inbound_security_rules, Unset):
            inbound_security_rules = []
            for inbound_security_rules_item_data in self.inbound_security_rules:
                inbound_security_rules_item = inbound_security_rules_item_data.to_dict()
                inbound_security_rules.append(inbound_security_rules_item)

        policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        service_name = self.service_name

        traffic_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_rules, Unset):
            traffic_rules = []
            for traffic_rules_item_data in self.traffic_rules:
                traffic_rules_item = traffic_rules_item_data.to_dict()
                traffic_rules.append(traffic_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name
        if inbound_security_rules is not UNSET:
            field_dict["inboundSecurityRules"] = inbound_security_rules
        if policy is not UNSET:
            field_dict["policy"] = policy
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if traffic_rules is not UNSET:
            field_dict["trafficRules"] = traffic_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_inbound_security_rules_item import (
            GetV1ExtranetsB2BIdProducerResponse200PolicyInboundSecurityRulesItem,
        )
        from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_policy import (
            GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy,
        )
        from ..models.get_v1_extranets_b2b_id_producer_response_200_policy_traffic_rules_item import (
            GetV1ExtranetsB2BIdProducerResponse200PolicyTrafficRulesItem,
        )

        d = src_dict.copy()
        dns_name = d.pop("dnsName", UNSET)

        inbound_security_rules = []
        _inbound_security_rules = d.pop("inboundSecurityRules", UNSET)
        for inbound_security_rules_item_data in _inbound_security_rules or []:
            inbound_security_rules_item = (
                GetV1ExtranetsB2BIdProducerResponse200PolicyInboundSecurityRulesItem.from_dict(
                    inbound_security_rules_item_data
                )
            )

            inbound_security_rules.append(inbound_security_rules_item)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = GetV1ExtranetsB2BIdProducerResponse200PolicyPolicy.from_dict(_policy)

        service_name = d.pop("serviceName", UNSET)

        traffic_rules = []
        _traffic_rules = d.pop("trafficRules", UNSET)
        for traffic_rules_item_data in _traffic_rules or []:
            traffic_rules_item = GetV1ExtranetsB2BIdProducerResponse200PolicyTrafficRulesItem.from_dict(
                traffic_rules_item_data
            )

            traffic_rules.append(traffic_rules_item)

        get_v1_extranets_b2b_id_producer_response_200_policy = cls(
            dns_name=dns_name,
            inbound_security_rules=inbound_security_rules,
            policy=policy,
            service_name=service_name,
            traffic_rules=traffic_rules,
        )

        get_v1_extranets_b2b_id_producer_response_200_policy.additional_properties = d
        return get_v1_extranets_b2b_id_producer_response_200_policy

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
