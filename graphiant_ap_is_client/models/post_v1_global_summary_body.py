from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalSummaryBody")


@_attrs_define
class PostV1GlobalSummaryBody:
    """
    Attributes:
        ipfix_exported_type (Union[Unset, str]):  Example: TYPE_BOOL.
        prefix_set_type (Union[Unset, str]):  Example: TYPE_BOOL.
        routing_policy_type (Union[Unset, str]):  Example: TYPE_BOOL.
        snmp_type (Union[Unset, str]):  Example: TYPE_BOOL.
        syslog_server_type (Union[Unset, str]):  Example: TYPE_BOOL.
        traffic_policy_type (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    ipfix_exported_type: Union[Unset, str] = UNSET
    prefix_set_type: Union[Unset, str] = UNSET
    routing_policy_type: Union[Unset, str] = UNSET
    snmp_type: Union[Unset, str] = UNSET
    syslog_server_type: Union[Unset, str] = UNSET
    traffic_policy_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipfix_exported_type = self.ipfix_exported_type

        prefix_set_type = self.prefix_set_type

        routing_policy_type = self.routing_policy_type

        snmp_type = self.snmp_type

        syslog_server_type = self.syslog_server_type

        traffic_policy_type = self.traffic_policy_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipfix_exported_type is not UNSET:
            field_dict["ipfixExportedType"] = ipfix_exported_type
        if prefix_set_type is not UNSET:
            field_dict["prefixSetType"] = prefix_set_type
        if routing_policy_type is not UNSET:
            field_dict["routingPolicyType"] = routing_policy_type
        if snmp_type is not UNSET:
            field_dict["snmpType"] = snmp_type
        if syslog_server_type is not UNSET:
            field_dict["syslogServerType"] = syslog_server_type
        if traffic_policy_type is not UNSET:
            field_dict["trafficPolicyType"] = traffic_policy_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipfix_exported_type = d.pop("ipfixExportedType", UNSET)

        prefix_set_type = d.pop("prefixSetType", UNSET)

        routing_policy_type = d.pop("routingPolicyType", UNSET)

        snmp_type = d.pop("snmpType", UNSET)

        syslog_server_type = d.pop("syslogServerType", UNSET)

        traffic_policy_type = d.pop("trafficPolicyType", UNSET)

        post_v1_global_summary_body = cls(
            ipfix_exported_type=ipfix_exported_type,
            prefix_set_type=prefix_set_type,
            routing_policy_type=routing_policy_type,
            snmp_type=snmp_type,
            syslog_server_type=syslog_server_type,
            traffic_policy_type=traffic_policy_type,
        )

        post_v1_global_summary_body.additional_properties = d
        return post_v1_global_summary_body

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
