from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerResponse200PolicyItemInboundSecurityRulesItemMatch")


@_attrs_define
class PostV1ExtranetsB2BConsumerResponse200PolicyItemInboundSecurityRulesItemMatch:
    """
    Attributes:
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        destination_prefix (Union[Unset, str]):  Example: TYPE_STRING.
        icmp_type (Union[Unset, str]):  Example: TYPE_UINT32.
        protocol (Union[Unset, str]):  Example: TYPE_UINT32.
        source_port (Union[Unset, str]):  Example: TYPE_UINT32.
        source_prefix (Union[Unset, str]):  Example: TYPE_STRING.
    """

    destination_port: Union[Unset, str] = UNSET
    destination_prefix: Union[Unset, str] = UNSET
    icmp_type: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    source_port: Union[Unset, str] = UNSET
    source_prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_port = self.destination_port

        destination_prefix = self.destination_prefix

        icmp_type = self.icmp_type

        protocol = self.protocol

        source_port = self.source_port

        source_prefix = self.source_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if destination_prefix is not UNSET:
            field_dict["destinationPrefix"] = destination_prefix
        if icmp_type is not UNSET:
            field_dict["icmpType"] = icmp_type
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source_port is not UNSET:
            field_dict["sourcePort"] = source_port
        if source_prefix is not UNSET:
            field_dict["sourcePrefix"] = source_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_port = d.pop("destinationPort", UNSET)

        destination_prefix = d.pop("destinationPrefix", UNSET)

        icmp_type = d.pop("icmpType", UNSET)

        protocol = d.pop("protocol", UNSET)

        source_port = d.pop("sourcePort", UNSET)

        source_prefix = d.pop("sourcePrefix", UNSET)

        post_v1_extranets_b2b_consumer_response_200_policy_item_inbound_security_rules_item_match = cls(
            destination_port=destination_port,
            destination_prefix=destination_prefix,
            icmp_type=icmp_type,
            protocol=protocol,
            source_port=source_port,
            source_prefix=source_prefix,
        )

        post_v1_extranets_b2b_consumer_response_200_policy_item_inbound_security_rules_item_match.additional_properties = d
        return post_v1_extranets_b2b_consumer_response_200_policy_item_inbound_security_rules_item_match

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
