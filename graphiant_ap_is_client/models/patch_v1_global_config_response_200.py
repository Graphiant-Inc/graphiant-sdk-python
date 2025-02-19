from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_response_200_global_prefix_sets_item import (
        PatchV1GlobalConfigResponse200GlobalPrefixSetsItem,
    )
    from ..models.patch_v1_global_config_response_200_ipfix_exporters_item import (
        PatchV1GlobalConfigResponse200IpfixExportersItem,
    )
    from ..models.patch_v1_global_config_response_200_prefix_sets_item import (
        PatchV1GlobalConfigResponse200PrefixSetsItem,
    )
    from ..models.patch_v1_global_config_response_200_routing_policies_item import (
        PatchV1GlobalConfigResponse200RoutingPoliciesItem,
    )
    from ..models.patch_v1_global_config_response_200_snmps_item import PatchV1GlobalConfigResponse200SnmpsItem
    from ..models.patch_v1_global_config_response_200_syslog_servers_item import (
        PatchV1GlobalConfigResponse200SyslogServersItem,
    )
    from ..models.patch_v1_global_config_response_200_traffic_policies_item import (
        PatchV1GlobalConfigResponse200TrafficPoliciesItem,
    )
    from ..models.patch_v1_global_config_response_200_vpn_profiles_item import (
        PatchV1GlobalConfigResponse200VpnProfilesItem,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigResponse200")


@_attrs_define
class PatchV1GlobalConfigResponse200:
    """
    Attributes:
        global_prefix_sets (Union[Unset, list['PatchV1GlobalConfigResponse200GlobalPrefixSetsItem']]):
        ipfix_exporters (Union[Unset, list['PatchV1GlobalConfigResponse200IpfixExportersItem']]):
        prefix_sets (Union[Unset, list['PatchV1GlobalConfigResponse200PrefixSetsItem']]):
        routing_policies (Union[Unset, list['PatchV1GlobalConfigResponse200RoutingPoliciesItem']]):
        snmps (Union[Unset, list['PatchV1GlobalConfigResponse200SnmpsItem']]):
        status (Union[Unset, str]):  Example: TYPE_STRING.
        syslog_servers (Union[Unset, list['PatchV1GlobalConfigResponse200SyslogServersItem']]):
        traffic_policies (Union[Unset, list['PatchV1GlobalConfigResponse200TrafficPoliciesItem']]):
        vpn_profiles (Union[Unset, list['PatchV1GlobalConfigResponse200VpnProfilesItem']]):
    """

    global_prefix_sets: Union[Unset, list["PatchV1GlobalConfigResponse200GlobalPrefixSetsItem"]] = UNSET
    ipfix_exporters: Union[Unset, list["PatchV1GlobalConfigResponse200IpfixExportersItem"]] = UNSET
    prefix_sets: Union[Unset, list["PatchV1GlobalConfigResponse200PrefixSetsItem"]] = UNSET
    routing_policies: Union[Unset, list["PatchV1GlobalConfigResponse200RoutingPoliciesItem"]] = UNSET
    snmps: Union[Unset, list["PatchV1GlobalConfigResponse200SnmpsItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    syslog_servers: Union[Unset, list["PatchV1GlobalConfigResponse200SyslogServersItem"]] = UNSET
    traffic_policies: Union[Unset, list["PatchV1GlobalConfigResponse200TrafficPoliciesItem"]] = UNSET
    vpn_profiles: Union[Unset, list["PatchV1GlobalConfigResponse200VpnProfilesItem"]] = UNSET
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

        status = self.status

        syslog_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_servers, Unset):
            syslog_servers = []
            for syslog_servers_item_data in self.syslog_servers:
                syslog_servers_item = syslog_servers_item_data.to_dict()
                syslog_servers.append(syslog_servers_item)

        traffic_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_policies, Unset):
            traffic_policies = []
            for traffic_policies_item_data in self.traffic_policies:
                traffic_policies_item = traffic_policies_item_data.to_dict()
                traffic_policies.append(traffic_policies_item)

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
        if status is not UNSET:
            field_dict["status"] = status
        if syslog_servers is not UNSET:
            field_dict["syslogServers"] = syslog_servers
        if traffic_policies is not UNSET:
            field_dict["trafficPolicies"] = traffic_policies
        if vpn_profiles is not UNSET:
            field_dict["vpnProfiles"] = vpn_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_response_200_global_prefix_sets_item import (
            PatchV1GlobalConfigResponse200GlobalPrefixSetsItem,
        )
        from ..models.patch_v1_global_config_response_200_ipfix_exporters_item import (
            PatchV1GlobalConfigResponse200IpfixExportersItem,
        )
        from ..models.patch_v1_global_config_response_200_prefix_sets_item import (
            PatchV1GlobalConfigResponse200PrefixSetsItem,
        )
        from ..models.patch_v1_global_config_response_200_routing_policies_item import (
            PatchV1GlobalConfigResponse200RoutingPoliciesItem,
        )
        from ..models.patch_v1_global_config_response_200_snmps_item import PatchV1GlobalConfigResponse200SnmpsItem
        from ..models.patch_v1_global_config_response_200_syslog_servers_item import (
            PatchV1GlobalConfigResponse200SyslogServersItem,
        )
        from ..models.patch_v1_global_config_response_200_traffic_policies_item import (
            PatchV1GlobalConfigResponse200TrafficPoliciesItem,
        )
        from ..models.patch_v1_global_config_response_200_vpn_profiles_item import (
            PatchV1GlobalConfigResponse200VpnProfilesItem,
        )

        d = src_dict.copy()
        global_prefix_sets = []
        _global_prefix_sets = d.pop("globalPrefixSets", UNSET)
        for global_prefix_sets_item_data in _global_prefix_sets or []:
            global_prefix_sets_item = PatchV1GlobalConfigResponse200GlobalPrefixSetsItem.from_dict(
                global_prefix_sets_item_data
            )

            global_prefix_sets.append(global_prefix_sets_item)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PatchV1GlobalConfigResponse200IpfixExportersItem.from_dict(ipfix_exporters_item_data)

            ipfix_exporters.append(ipfix_exporters_item)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PatchV1GlobalConfigResponse200PrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        routing_policies = []
        _routing_policies = d.pop("routingPolicies", UNSET)
        for routing_policies_item_data in _routing_policies or []:
            routing_policies_item = PatchV1GlobalConfigResponse200RoutingPoliciesItem.from_dict(
                routing_policies_item_data
            )

            routing_policies.append(routing_policies_item)

        snmps = []
        _snmps = d.pop("snmps", UNSET)
        for snmps_item_data in _snmps or []:
            snmps_item = PatchV1GlobalConfigResponse200SnmpsItem.from_dict(snmps_item_data)

            snmps.append(snmps_item)

        status = d.pop("status", UNSET)

        syslog_servers = []
        _syslog_servers = d.pop("syslogServers", UNSET)
        for syslog_servers_item_data in _syslog_servers or []:
            syslog_servers_item = PatchV1GlobalConfigResponse200SyslogServersItem.from_dict(syslog_servers_item_data)

            syslog_servers.append(syslog_servers_item)

        traffic_policies = []
        _traffic_policies = d.pop("trafficPolicies", UNSET)
        for traffic_policies_item_data in _traffic_policies or []:
            traffic_policies_item = PatchV1GlobalConfigResponse200TrafficPoliciesItem.from_dict(
                traffic_policies_item_data
            )

            traffic_policies.append(traffic_policies_item)

        vpn_profiles = []
        _vpn_profiles = d.pop("vpnProfiles", UNSET)
        for vpn_profiles_item_data in _vpn_profiles or []:
            vpn_profiles_item = PatchV1GlobalConfigResponse200VpnProfilesItem.from_dict(vpn_profiles_item_data)

            vpn_profiles.append(vpn_profiles_item)

        patch_v1_global_config_response_200 = cls(
            global_prefix_sets=global_prefix_sets,
            ipfix_exporters=ipfix_exporters,
            prefix_sets=prefix_sets,
            routing_policies=routing_policies,
            snmps=snmps,
            status=status,
            syslog_servers=syslog_servers,
            traffic_policies=traffic_policies,
            vpn_profiles=vpn_profiles,
        )

        patch_v1_global_config_response_200.additional_properties = d
        return patch_v1_global_config_response_200

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
