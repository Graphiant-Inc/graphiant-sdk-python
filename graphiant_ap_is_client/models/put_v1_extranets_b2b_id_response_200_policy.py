from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_extranets_b2b_id_response_200_policy_inbound_security_rules_item import (
        PutV1ExtranetsB2BIdResponse200PolicyInboundSecurityRulesItem,
    )
    from ..models.put_v1_extranets_b2b_id_response_200_policy_policy import PutV1ExtranetsB2BIdResponse200PolicyPolicy
    from ..models.put_v1_extranets_b2b_id_response_200_policy_traffic_rules_item import (
        PutV1ExtranetsB2BIdResponse200PolicyTrafficRulesItem,
    )


T = TypeVar("T", bound="PutV1ExtranetsB2BIdResponse200Policy")


@_attrs_define
class PutV1ExtranetsB2BIdResponse200Policy:
    """
    Attributes:
        dns_name (Union[Unset, str]):  Example: TYPE_STRING.
        inbound_security_rules (Union[Unset, list['PutV1ExtranetsB2BIdResponse200PolicyInboundSecurityRulesItem']]):
        policy (Union[Unset, PutV1ExtranetsB2BIdResponse200PolicyPolicy]):
        service_name (Union[Unset, str]):  Example: TYPE_STRING.
        traffic_rules (Union[Unset, list['PutV1ExtranetsB2BIdResponse200PolicyTrafficRulesItem']]):
    """

    dns_name: Union[Unset, str] = UNSET
    inbound_security_rules: Union[Unset, list["PutV1ExtranetsB2BIdResponse200PolicyInboundSecurityRulesItem"]] = UNSET
    policy: Union[Unset, "PutV1ExtranetsB2BIdResponse200PolicyPolicy"] = UNSET
    service_name: Union[Unset, str] = UNSET
    traffic_rules: Union[Unset, list["PutV1ExtranetsB2BIdResponse200PolicyTrafficRulesItem"]] = UNSET
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
        from ..models.put_v1_extranets_b2b_id_response_200_policy_inbound_security_rules_item import (
            PutV1ExtranetsB2BIdResponse200PolicyInboundSecurityRulesItem,
        )
        from ..models.put_v1_extranets_b2b_id_response_200_policy_policy import (
            PutV1ExtranetsB2BIdResponse200PolicyPolicy,
        )
        from ..models.put_v1_extranets_b2b_id_response_200_policy_traffic_rules_item import (
            PutV1ExtranetsB2BIdResponse200PolicyTrafficRulesItem,
        )

        d = src_dict.copy()
        dns_name = d.pop("dnsName", UNSET)

        inbound_security_rules = []
        _inbound_security_rules = d.pop("inboundSecurityRules", UNSET)
        for inbound_security_rules_item_data in _inbound_security_rules or []:
            inbound_security_rules_item = PutV1ExtranetsB2BIdResponse200PolicyInboundSecurityRulesItem.from_dict(
                inbound_security_rules_item_data
            )

            inbound_security_rules.append(inbound_security_rules_item)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, PutV1ExtranetsB2BIdResponse200PolicyPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PutV1ExtranetsB2BIdResponse200PolicyPolicy.from_dict(_policy)

        service_name = d.pop("serviceName", UNSET)

        traffic_rules = []
        _traffic_rules = d.pop("trafficRules", UNSET)
        for traffic_rules_item_data in _traffic_rules or []:
            traffic_rules_item = PutV1ExtranetsB2BIdResponse200PolicyTrafficRulesItem.from_dict(traffic_rules_item_data)

            traffic_rules.append(traffic_rules_item)

        put_v1_extranets_b2b_id_response_200_policy = cls(
            dns_name=dns_name,
            inbound_security_rules=inbound_security_rules,
            policy=policy,
            service_name=service_name,
            traffic_rules=traffic_rules,
        )

        put_v1_extranets_b2b_id_response_200_policy.additional_properties = d
        return put_v1_extranets_b2b_id_response_200_policy

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
