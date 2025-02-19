from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalAttachedEdgesBody")


@_attrs_define
class PostV1GlobalAttachedEdgesBody:
    """
    Attributes:
        ipfix_exported_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        prefix_set_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        routing_policy_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        snmp_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        syslog_server_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        traffic_policy_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    ipfix_exported_ids: Union[Unset, list[str]] = UNSET
    prefix_set_ids: Union[Unset, list[str]] = UNSET
    routing_policy_ids: Union[Unset, list[str]] = UNSET
    snmp_ids: Union[Unset, list[str]] = UNSET
    syslog_server_ids: Union[Unset, list[str]] = UNSET
    traffic_policy_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipfix_exported_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipfix_exported_ids, Unset):
            ipfix_exported_ids = self.ipfix_exported_ids

        prefix_set_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.prefix_set_ids, Unset):
            prefix_set_ids = self.prefix_set_ids

        routing_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.routing_policy_ids, Unset):
            routing_policy_ids = self.routing_policy_ids

        snmp_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.snmp_ids, Unset):
            snmp_ids = self.snmp_ids

        syslog_server_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.syslog_server_ids, Unset):
            syslog_server_ids = self.syslog_server_ids

        traffic_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.traffic_policy_ids, Unset):
            traffic_policy_ids = self.traffic_policy_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipfix_exported_ids is not UNSET:
            field_dict["ipfixExportedIds"] = ipfix_exported_ids
        if prefix_set_ids is not UNSET:
            field_dict["prefixSetIds"] = prefix_set_ids
        if routing_policy_ids is not UNSET:
            field_dict["routingPolicyIds"] = routing_policy_ids
        if snmp_ids is not UNSET:
            field_dict["snmpIds"] = snmp_ids
        if syslog_server_ids is not UNSET:
            field_dict["syslogServerIds"] = syslog_server_ids
        if traffic_policy_ids is not UNSET:
            field_dict["trafficPolicyIds"] = traffic_policy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipfix_exported_ids = cast(list[str], d.pop("ipfixExportedIds", UNSET))

        prefix_set_ids = cast(list[str], d.pop("prefixSetIds", UNSET))

        routing_policy_ids = cast(list[str], d.pop("routingPolicyIds", UNSET))

        snmp_ids = cast(list[str], d.pop("snmpIds", UNSET))

        syslog_server_ids = cast(list[str], d.pop("syslogServerIds", UNSET))

        traffic_policy_ids = cast(list[str], d.pop("trafficPolicyIds", UNSET))

        post_v1_global_attached_edges_body = cls(
            ipfix_exported_ids=ipfix_exported_ids,
            prefix_set_ids=prefix_set_ids,
            routing_policy_ids=routing_policy_ids,
            snmp_ids=snmp_ids,
            syslog_server_ids=syslog_server_ids,
            traffic_policy_ids=traffic_policy_ids,
        )

        post_v1_global_attached_edges_body.additional_properties = d
        return post_v1_global_attached_edges_body

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
