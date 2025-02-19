from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_global_prefix_sets_item import PatchV1GlobalConfigBodyGlobalPrefixSetsItem
    from ..models.patch_v1_global_config_body_ipfix_exporters_item import PatchV1GlobalConfigBodyIpfixExportersItem
    from ..models.patch_v1_global_config_body_prefix_sets_item import PatchV1GlobalConfigBodyPrefixSetsItem
    from ..models.patch_v1_global_config_body_routing_policies_item import PatchV1GlobalConfigBodyRoutingPoliciesItem
    from ..models.patch_v1_global_config_body_snmps_item import PatchV1GlobalConfigBodySnmpsItem
    from ..models.patch_v1_global_config_body_syslog_servers_item import PatchV1GlobalConfigBodySyslogServersItem
    from ..models.patch_v1_global_config_body_traffic_policies import PatchV1GlobalConfigBodyTrafficPolicies
    from ..models.patch_v1_global_config_body_vpn_profiles_item import PatchV1GlobalConfigBodyVpnProfilesItem


T = TypeVar("T", bound="PatchV1GlobalConfigBody")


@_attrs_define
class PatchV1GlobalConfigBody:
    """
    Attributes:
        global_prefix_sets (Union[Unset, list['PatchV1GlobalConfigBodyGlobalPrefixSetsItem']]):
        ipfix_exporters (Union[Unset, list['PatchV1GlobalConfigBodyIpfixExportersItem']]):
        prefix_sets (Union[Unset, list['PatchV1GlobalConfigBodyPrefixSetsItem']]):
        routing_policies (Union[Unset, list['PatchV1GlobalConfigBodyRoutingPoliciesItem']]):
        snmps (Union[Unset, list['PatchV1GlobalConfigBodySnmpsItem']]):
        syslog_servers (Union[Unset, list['PatchV1GlobalConfigBodySyslogServersItem']]):
        traffic_policies (Union[Unset, PatchV1GlobalConfigBodyTrafficPolicies]):
        vpn_profiles (Union[Unset, list['PatchV1GlobalConfigBodyVpnProfilesItem']]):
    """

    global_prefix_sets: Union[Unset, list["PatchV1GlobalConfigBodyGlobalPrefixSetsItem"]] = UNSET
    ipfix_exporters: Union[Unset, list["PatchV1GlobalConfigBodyIpfixExportersItem"]] = UNSET
    prefix_sets: Union[Unset, list["PatchV1GlobalConfigBodyPrefixSetsItem"]] = UNSET
    routing_policies: Union[Unset, list["PatchV1GlobalConfigBodyRoutingPoliciesItem"]] = UNSET
    snmps: Union[Unset, list["PatchV1GlobalConfigBodySnmpsItem"]] = UNSET
    syslog_servers: Union[Unset, list["PatchV1GlobalConfigBodySyslogServersItem"]] = UNSET
    traffic_policies: Union[Unset, "PatchV1GlobalConfigBodyTrafficPolicies"] = UNSET
    vpn_profiles: Union[Unset, list["PatchV1GlobalConfigBodyVpnProfilesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.global_prefix_sets, Unset):
            global_prefix_sets = []
            for global_prefix_sets_item_data in self.global_prefix_sets:
                global_prefix_sets_item = global_prefix_sets_item_data.to_dict()
                global_prefix_sets.append(global_prefix_sets_item)

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_sets, Unset):
            prefix_sets = []
            for prefix_sets_item_data in self.prefix_sets:
                prefix_sets_item = prefix_sets_item_data.to_dict()
                prefix_sets.append(prefix_sets_item)

        routing_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routing_policies, Unset):
            routing_policies = []
            for routing_policies_item_data in self.routing_policies:
                routing_policies_item = routing_policies_item_data.to_dict()
                routing_policies.append(routing_policies_item)

        snmps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snmps, Unset):
            snmps = []
            for snmps_item_data in self.snmps:
                snmps_item = snmps_item_data.to_dict()
                snmps.append(snmps_item)

        syslog_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_servers, Unset):
            syslog_servers = []
            for syslog_servers_item_data in self.syslog_servers:
                syslog_servers_item = syslog_servers_item_data.to_dict()
                syslog_servers.append(syslog_servers_item)

        traffic_policies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_policies, Unset):
            traffic_policies = self.traffic_policies.to_dict()

        vpn_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vpn_profiles, Unset):
            vpn_profiles = []
            for vpn_profiles_item_data in self.vpn_profiles:
                vpn_profiles_item = vpn_profiles_item_data.to_dict()
                vpn_profiles.append(vpn_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_prefix_sets is not UNSET:
            field_dict["globalPrefixSets"] = global_prefix_sets
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
        if prefix_sets is not UNSET:
            field_dict["prefixSets"] = prefix_sets
        if routing_policies is not UNSET:
            field_dict["routingPolicies"] = routing_policies
        if snmps is not UNSET:
            field_dict["snmps"] = snmps
        if syslog_servers is not UNSET:
            field_dict["syslogServers"] = syslog_servers
        if traffic_policies is not UNSET:
            field_dict["trafficPolicies"] = traffic_policies
        if vpn_profiles is not UNSET:
            field_dict["vpnProfiles"] = vpn_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_global_prefix_sets_item import (
            PatchV1GlobalConfigBodyGlobalPrefixSetsItem,
        )
        from ..models.patch_v1_global_config_body_ipfix_exporters_item import PatchV1GlobalConfigBodyIpfixExportersItem
        from ..models.patch_v1_global_config_body_prefix_sets_item import PatchV1GlobalConfigBodyPrefixSetsItem
        from ..models.patch_v1_global_config_body_routing_policies_item import (
            PatchV1GlobalConfigBodyRoutingPoliciesItem,
        )
        from ..models.patch_v1_global_config_body_snmps_item import PatchV1GlobalConfigBodySnmpsItem
        from ..models.patch_v1_global_config_body_syslog_servers_item import PatchV1GlobalConfigBodySyslogServersItem
        from ..models.patch_v1_global_config_body_traffic_policies import PatchV1GlobalConfigBodyTrafficPolicies
        from ..models.patch_v1_global_config_body_vpn_profiles_item import PatchV1GlobalConfigBodyVpnProfilesItem

        d = src_dict.copy()
        global_prefix_sets = []
        _global_prefix_sets = d.pop("globalPrefixSets", UNSET)
        for global_prefix_sets_item_data in _global_prefix_sets or []:
            global_prefix_sets_item = PatchV1GlobalConfigBodyGlobalPrefixSetsItem.from_dict(
                global_prefix_sets_item_data
            )

            global_prefix_sets.append(global_prefix_sets_item)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PatchV1GlobalConfigBodyIpfixExportersItem.from_dict(ipfix_exporters_item_data)

            ipfix_exporters.append(ipfix_exporters_item)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PatchV1GlobalConfigBodyPrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        routing_policies = []
        _routing_policies = d.pop("routingPolicies", UNSET)
        for routing_policies_item_data in _routing_policies or []:
            routing_policies_item = PatchV1GlobalConfigBodyRoutingPoliciesItem.from_dict(routing_policies_item_data)

            routing_policies.append(routing_policies_item)

        snmps = []
        _snmps = d.pop("snmps", UNSET)
        for snmps_item_data in _snmps or []:
            snmps_item = PatchV1GlobalConfigBodySnmpsItem.from_dict(snmps_item_data)

            snmps.append(snmps_item)

        syslog_servers = []
        _syslog_servers = d.pop("syslogServers", UNSET)
        for syslog_servers_item_data in _syslog_servers or []:
            syslog_servers_item = PatchV1GlobalConfigBodySyslogServersItem.from_dict(syslog_servers_item_data)

            syslog_servers.append(syslog_servers_item)

        _traffic_policies = d.pop("trafficPolicies", UNSET)
        traffic_policies: Union[Unset, PatchV1GlobalConfigBodyTrafficPolicies]
        if isinstance(_traffic_policies, Unset):
            traffic_policies = UNSET
        else:
            traffic_policies = PatchV1GlobalConfigBodyTrafficPolicies.from_dict(_traffic_policies)

        vpn_profiles = []
        _vpn_profiles = d.pop("vpnProfiles", UNSET)
        for vpn_profiles_item_data in _vpn_profiles or []:
            vpn_profiles_item = PatchV1GlobalConfigBodyVpnProfilesItem.from_dict(vpn_profiles_item_data)

            vpn_profiles.append(vpn_profiles_item)

        patch_v1_global_config_body = cls(
            global_prefix_sets=global_prefix_sets,
            ipfix_exporters=ipfix_exporters,
            prefix_sets=prefix_sets,
            routing_policies=routing_policies,
            snmps=snmps,
            syslog_servers=syslog_servers,
            traffic_policies=traffic_policies,
            vpn_profiles=vpn_profiles,
        )

        patch_v1_global_config_body.additional_properties = d
        return patch_v1_global_config_body

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
