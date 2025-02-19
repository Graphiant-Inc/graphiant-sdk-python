from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_config_site_body_global_prefix_set_ops_item import (
        PostV1GlobalConfigSiteBodyGlobalPrefixSetOpsItem,
    )
    from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_item import (
        PostV1GlobalConfigSiteBodyIpfixExporterOpsItem,
    )
    from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_v2_item import (
        PostV1GlobalConfigSiteBodyIpfixExporterOpsV2Item,
    )
    from ..models.post_v1_global_config_site_body_prefix_set_ops_item import PostV1GlobalConfigSiteBodyPrefixSetOpsItem
    from ..models.post_v1_global_config_site_body_routing_policy_ops_item import (
        PostV1GlobalConfigSiteBodyRoutingPolicyOpsItem,
    )
    from ..models.post_v1_global_config_site_body_snmp_ops_item import PostV1GlobalConfigSiteBodySnmpOpsItem
    from ..models.post_v1_global_config_site_body_syslog_server_ops_item import (
        PostV1GlobalConfigSiteBodySyslogServerOpsItem,
    )
    from ..models.post_v1_global_config_site_body_syslog_server_ops_v2_item import (
        PostV1GlobalConfigSiteBodySyslogServerOpsV2Item,
    )
    from ..models.post_v1_global_config_site_body_traffic_policy_ops_item import (
        PostV1GlobalConfigSiteBodyTrafficPolicyOpsItem,
    )


T = TypeVar("T", bound="PostV1GlobalConfigSiteBody")


@_attrs_define
class PostV1GlobalConfigSiteBody:
    """
    Attributes:
        global_prefix_set_ops (Union[Unset, list['PostV1GlobalConfigSiteBodyGlobalPrefixSetOpsItem']]):
        ipfix_exporter_ops (Union[Unset, list['PostV1GlobalConfigSiteBodyIpfixExporterOpsItem']]):
        ipfix_exporter_ops_v2 (Union[Unset, list['PostV1GlobalConfigSiteBodyIpfixExporterOpsV2Item']]):
        prefix_set_ops (Union[Unset, list['PostV1GlobalConfigSiteBodyPrefixSetOpsItem']]):
        routing_policy_ops (Union[Unset, list['PostV1GlobalConfigSiteBodyRoutingPolicyOpsItem']]):
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        snmp_ops (Union[Unset, list['PostV1GlobalConfigSiteBodySnmpOpsItem']]):
        syslog_server_ops (Union[Unset, list['PostV1GlobalConfigSiteBodySyslogServerOpsItem']]):
        syslog_server_ops_v2 (Union[Unset, list['PostV1GlobalConfigSiteBodySyslogServerOpsV2Item']]):
        traffic_policy_ops (Union[Unset, list['PostV1GlobalConfigSiteBodyTrafficPolicyOpsItem']]):
    """

    global_prefix_set_ops: Union[Unset, list["PostV1GlobalConfigSiteBodyGlobalPrefixSetOpsItem"]] = UNSET
    ipfix_exporter_ops: Union[Unset, list["PostV1GlobalConfigSiteBodyIpfixExporterOpsItem"]] = UNSET
    ipfix_exporter_ops_v2: Union[Unset, list["PostV1GlobalConfigSiteBodyIpfixExporterOpsV2Item"]] = UNSET
    prefix_set_ops: Union[Unset, list["PostV1GlobalConfigSiteBodyPrefixSetOpsItem"]] = UNSET
    routing_policy_ops: Union[Unset, list["PostV1GlobalConfigSiteBodyRoutingPolicyOpsItem"]] = UNSET
    site_id: Union[Unset, str] = UNSET
    snmp_ops: Union[Unset, list["PostV1GlobalConfigSiteBodySnmpOpsItem"]] = UNSET
    syslog_server_ops: Union[Unset, list["PostV1GlobalConfigSiteBodySyslogServerOpsItem"]] = UNSET
    syslog_server_ops_v2: Union[Unset, list["PostV1GlobalConfigSiteBodySyslogServerOpsV2Item"]] = UNSET
    traffic_policy_ops: Union[Unset, list["PostV1GlobalConfigSiteBodyTrafficPolicyOpsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_prefix_set_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.global_prefix_set_ops, Unset):
            global_prefix_set_ops = []
            for global_prefix_set_ops_item_data in self.global_prefix_set_ops:
                global_prefix_set_ops_item = global_prefix_set_ops_item_data.to_dict()
                global_prefix_set_ops.append(global_prefix_set_ops_item)

        ipfix_exporter_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporter_ops, Unset):
            ipfix_exporter_ops = []
            for ipfix_exporter_ops_item_data in self.ipfix_exporter_ops:
                ipfix_exporter_ops_item = ipfix_exporter_ops_item_data.to_dict()
                ipfix_exporter_ops.append(ipfix_exporter_ops_item)

        ipfix_exporter_ops_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporter_ops_v2, Unset):
            ipfix_exporter_ops_v2 = []
            for ipfix_exporter_ops_v2_item_data in self.ipfix_exporter_ops_v2:
                ipfix_exporter_ops_v2_item = ipfix_exporter_ops_v2_item_data.to_dict()
                ipfix_exporter_ops_v2.append(ipfix_exporter_ops_v2_item)

        prefix_set_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_set_ops, Unset):
            prefix_set_ops = []
            for prefix_set_ops_item_data in self.prefix_set_ops:
                prefix_set_ops_item = prefix_set_ops_item_data.to_dict()
                prefix_set_ops.append(prefix_set_ops_item)

        routing_policy_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routing_policy_ops, Unset):
            routing_policy_ops = []
            for routing_policy_ops_item_data in self.routing_policy_ops:
                routing_policy_ops_item = routing_policy_ops_item_data.to_dict()
                routing_policy_ops.append(routing_policy_ops_item)

        site_id = self.site_id

        snmp_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snmp_ops, Unset):
            snmp_ops = []
            for snmp_ops_item_data in self.snmp_ops:
                snmp_ops_item = snmp_ops_item_data.to_dict()
                snmp_ops.append(snmp_ops_item)

        syslog_server_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_server_ops, Unset):
            syslog_server_ops = []
            for syslog_server_ops_item_data in self.syslog_server_ops:
                syslog_server_ops_item = syslog_server_ops_item_data.to_dict()
                syslog_server_ops.append(syslog_server_ops_item)

        syslog_server_ops_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_server_ops_v2, Unset):
            syslog_server_ops_v2 = []
            for syslog_server_ops_v2_item_data in self.syslog_server_ops_v2:
                syslog_server_ops_v2_item = syslog_server_ops_v2_item_data.to_dict()
                syslog_server_ops_v2.append(syslog_server_ops_v2_item)

        traffic_policy_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_policy_ops, Unset):
            traffic_policy_ops = []
            for traffic_policy_ops_item_data in self.traffic_policy_ops:
                traffic_policy_ops_item = traffic_policy_ops_item_data.to_dict()
                traffic_policy_ops.append(traffic_policy_ops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_prefix_set_ops is not UNSET:
            field_dict["globalPrefixSetOps"] = global_prefix_set_ops
        if ipfix_exporter_ops is not UNSET:
            field_dict["ipfixExporterOps"] = ipfix_exporter_ops
        if ipfix_exporter_ops_v2 is not UNSET:
            field_dict["ipfixExporterOpsV2"] = ipfix_exporter_ops_v2
        if prefix_set_ops is not UNSET:
            field_dict["prefixSetOps"] = prefix_set_ops
        if routing_policy_ops is not UNSET:
            field_dict["routingPolicyOps"] = routing_policy_ops
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if snmp_ops is not UNSET:
            field_dict["snmpOps"] = snmp_ops
        if syslog_server_ops is not UNSET:
            field_dict["syslogServerOps"] = syslog_server_ops
        if syslog_server_ops_v2 is not UNSET:
            field_dict["syslogServerOpsV2"] = syslog_server_ops_v2
        if traffic_policy_ops is not UNSET:
            field_dict["trafficPolicyOps"] = traffic_policy_ops

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_config_site_body_global_prefix_set_ops_item import (
            PostV1GlobalConfigSiteBodyGlobalPrefixSetOpsItem,
        )
        from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_item import (
            PostV1GlobalConfigSiteBodyIpfixExporterOpsItem,
        )
        from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_v2_item import (
            PostV1GlobalConfigSiteBodyIpfixExporterOpsV2Item,
        )
        from ..models.post_v1_global_config_site_body_prefix_set_ops_item import (
            PostV1GlobalConfigSiteBodyPrefixSetOpsItem,
        )
        from ..models.post_v1_global_config_site_body_routing_policy_ops_item import (
            PostV1GlobalConfigSiteBodyRoutingPolicyOpsItem,
        )
        from ..models.post_v1_global_config_site_body_snmp_ops_item import PostV1GlobalConfigSiteBodySnmpOpsItem
        from ..models.post_v1_global_config_site_body_syslog_server_ops_item import (
            PostV1GlobalConfigSiteBodySyslogServerOpsItem,
        )
        from ..models.post_v1_global_config_site_body_syslog_server_ops_v2_item import (
            PostV1GlobalConfigSiteBodySyslogServerOpsV2Item,
        )
        from ..models.post_v1_global_config_site_body_traffic_policy_ops_item import (
            PostV1GlobalConfigSiteBodyTrafficPolicyOpsItem,
        )

        d = src_dict.copy()
        global_prefix_set_ops = []
        _global_prefix_set_ops = d.pop("globalPrefixSetOps", UNSET)
        for global_prefix_set_ops_item_data in _global_prefix_set_ops or []:
            global_prefix_set_ops_item = PostV1GlobalConfigSiteBodyGlobalPrefixSetOpsItem.from_dict(
                global_prefix_set_ops_item_data
            )

            global_prefix_set_ops.append(global_prefix_set_ops_item)

        ipfix_exporter_ops = []
        _ipfix_exporter_ops = d.pop("ipfixExporterOps", UNSET)
        for ipfix_exporter_ops_item_data in _ipfix_exporter_ops or []:
            ipfix_exporter_ops_item = PostV1GlobalConfigSiteBodyIpfixExporterOpsItem.from_dict(
                ipfix_exporter_ops_item_data
            )

            ipfix_exporter_ops.append(ipfix_exporter_ops_item)

        ipfix_exporter_ops_v2 = []
        _ipfix_exporter_ops_v2 = d.pop("ipfixExporterOpsV2", UNSET)
        for ipfix_exporter_ops_v2_item_data in _ipfix_exporter_ops_v2 or []:
            ipfix_exporter_ops_v2_item = PostV1GlobalConfigSiteBodyIpfixExporterOpsV2Item.from_dict(
                ipfix_exporter_ops_v2_item_data
            )

            ipfix_exporter_ops_v2.append(ipfix_exporter_ops_v2_item)

        prefix_set_ops = []
        _prefix_set_ops = d.pop("prefixSetOps", UNSET)
        for prefix_set_ops_item_data in _prefix_set_ops or []:
            prefix_set_ops_item = PostV1GlobalConfigSiteBodyPrefixSetOpsItem.from_dict(prefix_set_ops_item_data)

            prefix_set_ops.append(prefix_set_ops_item)

        routing_policy_ops = []
        _routing_policy_ops = d.pop("routingPolicyOps", UNSET)
        for routing_policy_ops_item_data in _routing_policy_ops or []:
            routing_policy_ops_item = PostV1GlobalConfigSiteBodyRoutingPolicyOpsItem.from_dict(
                routing_policy_ops_item_data
            )

            routing_policy_ops.append(routing_policy_ops_item)

        site_id = d.pop("siteId", UNSET)

        snmp_ops = []
        _snmp_ops = d.pop("snmpOps", UNSET)
        for snmp_ops_item_data in _snmp_ops or []:
            snmp_ops_item = PostV1GlobalConfigSiteBodySnmpOpsItem.from_dict(snmp_ops_item_data)

            snmp_ops.append(snmp_ops_item)

        syslog_server_ops = []
        _syslog_server_ops = d.pop("syslogServerOps", UNSET)
        for syslog_server_ops_item_data in _syslog_server_ops or []:
            syslog_server_ops_item = PostV1GlobalConfigSiteBodySyslogServerOpsItem.from_dict(
                syslog_server_ops_item_data
            )

            syslog_server_ops.append(syslog_server_ops_item)

        syslog_server_ops_v2 = []
        _syslog_server_ops_v2 = d.pop("syslogServerOpsV2", UNSET)
        for syslog_server_ops_v2_item_data in _syslog_server_ops_v2 or []:
            syslog_server_ops_v2_item = PostV1GlobalConfigSiteBodySyslogServerOpsV2Item.from_dict(
                syslog_server_ops_v2_item_data
            )

            syslog_server_ops_v2.append(syslog_server_ops_v2_item)

        traffic_policy_ops = []
        _traffic_policy_ops = d.pop("trafficPolicyOps", UNSET)
        for traffic_policy_ops_item_data in _traffic_policy_ops or []:
            traffic_policy_ops_item = PostV1GlobalConfigSiteBodyTrafficPolicyOpsItem.from_dict(
                traffic_policy_ops_item_data
            )

            traffic_policy_ops.append(traffic_policy_ops_item)

        post_v1_global_config_site_body = cls(
            global_prefix_set_ops=global_prefix_set_ops,
            ipfix_exporter_ops=ipfix_exporter_ops,
            ipfix_exporter_ops_v2=ipfix_exporter_ops_v2,
            prefix_set_ops=prefix_set_ops,
            routing_policy_ops=routing_policy_ops,
            site_id=site_id,
            snmp_ops=snmp_ops,
            syslog_server_ops=syslog_server_ops,
            syslog_server_ops_v2=syslog_server_ops_v2,
            traffic_policy_ops=traffic_policy_ops,
        )

        post_v1_global_config_site_body.additional_properties = d
        return post_v1_global_config_site_body

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
