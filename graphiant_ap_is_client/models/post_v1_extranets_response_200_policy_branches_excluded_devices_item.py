from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_bgp import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_circuits_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCircuitsItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_config_updated_at import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_created_at import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_dns import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_interfaces_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemInterfacesItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_ipfix_exporters_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpfixExportersItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_ipsec_tunnels_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpsecTunnelsItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_last_booted_at import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_local_route_tag import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_location import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_nat_policy import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_oper_staled_at import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_oper_updated_at import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_prefix_sets_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemPrefixSetsItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_region import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_region_override import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_routing_policies_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRoutingPoliciesItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_segments_item import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSegmentsItem,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_site import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_snmp import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_traffic_policy import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy,
    )
    from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_uptime import (
        PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime,
    )


T = TypeVar("T", bound="PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItem")


@_attrs_define
class PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItem:
    """
    Attributes:
        bgp (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp]):
        bgp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        circuits (Union[Unset, list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCircuitsItem']]):
        config_updated_at (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt]):
        created_at (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt]):
        dhcp_server_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        dns (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns]):
        gdi (Union[Unset, str]):  Example: TYPE_UINT32.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interfaces (Union[Unset, list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemInterfacesItem']]):
        internal_state (Union[Unset, str]):  Example: TYPE_ENUM.
        ipfix_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ipfix_exporters (Union[Unset,
            list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpfixExportersItem']]):
        ipsec_tunnels (Union[Unset,
            list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpsecTunnelsItem']]):
        last_booted_at (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt]):
        lldp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        local_route_tag (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag]):
        local_web_server_password (Union[Unset, str]):  Example: TYPE_STRING.
        location (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation]):
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        nat_policy (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy]):
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        oper_staled (Union[Unset, str]):  Example: TYPE_BOOL.
        oper_staled_at (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt]):
        oper_updated_at (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt]):
        ospfv_2_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ospfv_3_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        platform (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_sets (Union[Unset, list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemPrefixSetsItem']]):
        reboot_reason (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion]):
        region_override (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride]):
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        routing_policies (Union[Unset,
            list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRoutingPoliciesItem']]):
        segments (Union[Unset, list['PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSegmentsItem']]):
        serial_number (Union[Unset, str]):  Example: TYPE_STRING.
        site (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite]):
        snmp (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp]):
        software_version (Union[Unset, str]):  Example: TYPE_STRING.
        static_routes_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        traffic_policy (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy]):
        uptime (Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime]):
        vrrp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    bgp: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp"] = UNSET
    bgp_enabled: Union[Unset, str] = UNSET
    circuits: Union[Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCircuitsItem"]] = UNSET
    config_updated_at: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt"] = (
        UNSET
    )
    created_at: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt"] = UNSET
    dhcp_server_enabled: Union[Unset, str] = UNSET
    dns: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns"] = UNSET
    gdi: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interfaces: Union[Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemInterfacesItem"]] = UNSET
    internal_state: Union[Unset, str] = UNSET
    ipfix_enabled: Union[Unset, str] = UNSET
    ipfix_exporters: Union[
        Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpfixExportersItem"]
    ] = UNSET
    ipsec_tunnels: Union[Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpsecTunnelsItem"]] = (
        UNSET
    )
    last_booted_at: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt"] = UNSET
    lldp_enabled: Union[Unset, str] = UNSET
    local_route_tag: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag"] = UNSET
    local_web_server_password: Union[Unset, str] = UNSET
    location: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation"] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    nat_policy: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy"] = UNSET
    notes: Union[Unset, str] = UNSET
    oper_staled: Union[Unset, str] = UNSET
    oper_staled_at: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt"] = UNSET
    oper_updated_at: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt"] = UNSET
    ospfv_2_enabled: Union[Unset, str] = UNSET
    ospfv_3_enabled: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    prefix_sets: Union[Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemPrefixSetsItem"]] = UNSET
    reboot_reason: Union[Unset, str] = UNSET
    region: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion"] = UNSET
    region_override: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride"] = UNSET
    role: Union[Unset, str] = UNSET
    routing_policies: Union[
        Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRoutingPoliciesItem"]
    ] = UNSET
    segments: Union[Unset, list["PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSegmentsItem"]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    site: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite"] = UNSET
    snmp: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp"] = UNSET
    software_version: Union[Unset, str] = UNSET
    static_routes_enabled: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    traffic_policy: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy"] = UNSET
    uptime: Union[Unset, "PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime"] = UNSET
    vrrp_enabled: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp, Unset):
            bgp = self.bgp.to_dict()

        bgp_enabled = self.bgp_enabled

        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        config_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config_updated_at, Unset):
            config_updated_at = self.config_updated_at.to_dict()

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        dhcp_server_enabled = self.dhcp_server_enabled

        dns: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        gdi = self.gdi

        hostname = self.hostname

        id = self.id

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        internal_state = self.internal_state

        ipfix_enabled = self.ipfix_enabled

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        ipsec_tunnels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipsec_tunnels, Unset):
            ipsec_tunnels = []
            for ipsec_tunnels_item_data in self.ipsec_tunnels:
                ipsec_tunnels_item = ipsec_tunnels_item_data.to_dict()
                ipsec_tunnels.append(ipsec_tunnels_item)

        last_booted_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_booted_at, Unset):
            last_booted_at = self.last_booted_at.to_dict()

        lldp_enabled = self.lldp_enabled

        local_route_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_route_tag, Unset):
            local_route_tag = self.local_route_tag.to_dict()

        local_web_server_password = self.local_web_server_password

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        maintenance_mode = self.maintenance_mode

        nat_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nat_policy, Unset):
            nat_policy = self.nat_policy.to_dict()

        notes = self.notes

        oper_staled = self.oper_staled

        oper_staled_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oper_staled_at, Unset):
            oper_staled_at = self.oper_staled_at.to_dict()

        oper_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oper_updated_at, Unset):
            oper_updated_at = self.oper_updated_at.to_dict()

        ospfv_2_enabled = self.ospfv_2_enabled

        ospfv_3_enabled = self.ospfv_3_enabled

        platform = self.platform

        prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_sets, Unset):
            prefix_sets = []
            for prefix_sets_item_data in self.prefix_sets:
                prefix_sets_item = prefix_sets_item_data.to_dict()
                prefix_sets.append(prefix_sets_item)

        reboot_reason = self.reboot_reason

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        region_override: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region_override, Unset):
            region_override = self.region_override.to_dict()

        role = self.role

        routing_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routing_policies, Unset):
            routing_policies = []
            for routing_policies_item_data in self.routing_policies:
                routing_policies_item = routing_policies_item_data.to_dict()
                routing_policies.append(routing_policies_item)

        segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        serial_number = self.serial_number

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        snmp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        software_version = self.software_version

        static_routes_enabled = self.static_routes_enabled

        status = self.status

        traffic_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_policy, Unset):
            traffic_policy = self.traffic_policy.to_dict()

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        vrrp_enabled = self.vrrp_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp is not UNSET:
            field_dict["bgp"] = bgp
        if bgp_enabled is not UNSET:
            field_dict["bgpEnabled"] = bgp_enabled
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if config_updated_at is not UNSET:
            field_dict["configUpdatedAt"] = config_updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if dhcp_server_enabled is not UNSET:
            field_dict["dhcpServerEnabled"] = dhcp_server_enabled
        if dns is not UNSET:
            field_dict["dns"] = dns
        if gdi is not UNSET:
            field_dict["gdi"] = gdi
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if internal_state is not UNSET:
            field_dict["internalState"] = internal_state
        if ipfix_enabled is not UNSET:
            field_dict["ipfixEnabled"] = ipfix_enabled
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
        if ipsec_tunnels is not UNSET:
            field_dict["ipsecTunnels"] = ipsec_tunnels
        if last_booted_at is not UNSET:
            field_dict["lastBootedAt"] = last_booted_at
        if lldp_enabled is not UNSET:
            field_dict["lldpEnabled"] = lldp_enabled
        if local_route_tag is not UNSET:
            field_dict["localRouteTag"] = local_route_tag
        if local_web_server_password is not UNSET:
            field_dict["localWebServerPassword"] = local_web_server_password
        if location is not UNSET:
            field_dict["location"] = location
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if nat_policy is not UNSET:
            field_dict["natPolicy"] = nat_policy
        if notes is not UNSET:
            field_dict["notes"] = notes
        if oper_staled is not UNSET:
            field_dict["operStaled"] = oper_staled
        if oper_staled_at is not UNSET:
            field_dict["operStaledAt"] = oper_staled_at
        if oper_updated_at is not UNSET:
            field_dict["operUpdatedAt"] = oper_updated_at
        if ospfv_2_enabled is not UNSET:
            field_dict["ospfv2Enabled"] = ospfv_2_enabled
        if ospfv_3_enabled is not UNSET:
            field_dict["ospfv3Enabled"] = ospfv_3_enabled
        if platform is not UNSET:
            field_dict["platform"] = platform
        if prefix_sets is not UNSET:
            field_dict["prefixSets"] = prefix_sets
        if reboot_reason is not UNSET:
            field_dict["rebootReason"] = reboot_reason
        if region is not UNSET:
            field_dict["region"] = region
        if region_override is not UNSET:
            field_dict["regionOverride"] = region_override
        if role is not UNSET:
            field_dict["role"] = role
        if routing_policies is not UNSET:
            field_dict["routingPolicies"] = routing_policies
        if segments is not UNSET:
            field_dict["segments"] = segments
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if site is not UNSET:
            field_dict["site"] = site
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if static_routes_enabled is not UNSET:
            field_dict["staticRoutesEnabled"] = static_routes_enabled
        if status is not UNSET:
            field_dict["status"] = status
        if traffic_policy is not UNSET:
            field_dict["trafficPolicy"] = traffic_policy
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if vrrp_enabled is not UNSET:
            field_dict["vrrpEnabled"] = vrrp_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_bgp import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_circuits_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCircuitsItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_config_updated_at import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_created_at import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_dns import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_interfaces_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemInterfacesItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_ipfix_exporters_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpfixExportersItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_ipsec_tunnels_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpsecTunnelsItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_last_booted_at import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_local_route_tag import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_location import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_nat_policy import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_oper_staled_at import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_oper_updated_at import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_prefix_sets_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemPrefixSetsItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_region import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_region_override import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_routing_policies_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRoutingPoliciesItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_segments_item import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSegmentsItem,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_site import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_snmp import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_traffic_policy import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy,
        )
        from ..models.post_v1_extranets_response_200_policy_branches_excluded_devices_item_uptime import (
            PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime,
        )

        d = src_dict.copy()
        _bgp = d.pop("bgp", UNSET)
        bgp: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp]
        if isinstance(_bgp, Unset):
            bgp = UNSET
        else:
            bgp = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemBgp.from_dict(_bgp)

        bgp_enabled = d.pop("bgpEnabled", UNSET)

        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCircuitsItem.from_dict(
                circuits_item_data
            )

            circuits.append(circuits_item)

        _config_updated_at = d.pop("configUpdatedAt", UNSET)
        config_updated_at: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt]
        if isinstance(_config_updated_at, Unset):
            config_updated_at = UNSET
        else:
            config_updated_at = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemConfigUpdatedAt.from_dict(
                _config_updated_at
            )

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemCreatedAt.from_dict(_created_at)

        dhcp_server_enabled = d.pop("dhcpServerEnabled", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns]
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemDns.from_dict(_dns)

        gdi = d.pop("gdi", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemInterfacesItem.from_dict(
                interfaces_item_data
            )

            interfaces.append(interfaces_item)

        internal_state = d.pop("internalState", UNSET)

        ipfix_enabled = d.pop("ipfixEnabled", UNSET)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = (
                PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpfixExportersItem.from_dict(
                    ipfix_exporters_item_data
                )
            )

            ipfix_exporters.append(ipfix_exporters_item)

        ipsec_tunnels = []
        _ipsec_tunnels = d.pop("ipsecTunnels", UNSET)
        for ipsec_tunnels_item_data in _ipsec_tunnels or []:
            ipsec_tunnels_item = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemIpsecTunnelsItem.from_dict(
                ipsec_tunnels_item_data
            )

            ipsec_tunnels.append(ipsec_tunnels_item)

        _last_booted_at = d.pop("lastBootedAt", UNSET)
        last_booted_at: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt]
        if isinstance(_last_booted_at, Unset):
            last_booted_at = UNSET
        else:
            last_booted_at = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLastBootedAt.from_dict(
                _last_booted_at
            )

        lldp_enabled = d.pop("lldpEnabled", UNSET)

        _local_route_tag = d.pop("localRouteTag", UNSET)
        local_route_tag: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag]
        if isinstance(_local_route_tag, Unset):
            local_route_tag = UNSET
        else:
            local_route_tag = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocalRouteTag.from_dict(
                _local_route_tag
            )

        local_web_server_password = d.pop("localWebServerPassword", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemLocation.from_dict(_location)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        _nat_policy = d.pop("natPolicy", UNSET)
        nat_policy: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy]
        if isinstance(_nat_policy, Unset):
            nat_policy = UNSET
        else:
            nat_policy = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemNatPolicy.from_dict(_nat_policy)

        notes = d.pop("notes", UNSET)

        oper_staled = d.pop("operStaled", UNSET)

        _oper_staled_at = d.pop("operStaledAt", UNSET)
        oper_staled_at: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt]
        if isinstance(_oper_staled_at, Unset):
            oper_staled_at = UNSET
        else:
            oper_staled_at = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperStaledAt.from_dict(
                _oper_staled_at
            )

        _oper_updated_at = d.pop("operUpdatedAt", UNSET)
        oper_updated_at: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt]
        if isinstance(_oper_updated_at, Unset):
            oper_updated_at = UNSET
        else:
            oper_updated_at = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemOperUpdatedAt.from_dict(
                _oper_updated_at
            )

        ospfv_2_enabled = d.pop("ospfv2Enabled", UNSET)

        ospfv_3_enabled = d.pop("ospfv3Enabled", UNSET)

        platform = d.pop("platform", UNSET)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemPrefixSetsItem.from_dict(
                prefix_sets_item_data
            )

            prefix_sets.append(prefix_sets_item)

        reboot_reason = d.pop("rebootReason", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegion.from_dict(_region)

        _region_override = d.pop("regionOverride", UNSET)
        region_override: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride]
        if isinstance(_region_override, Unset):
            region_override = UNSET
        else:
            region_override = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRegionOverride.from_dict(
                _region_override
            )

        role = d.pop("role", UNSET)

        routing_policies = []
        _routing_policies = d.pop("routingPolicies", UNSET)
        for routing_policies_item_data in _routing_policies or []:
            routing_policies_item = (
                PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemRoutingPoliciesItem.from_dict(
                    routing_policies_item_data
                )
            )

            routing_policies.append(routing_policies_item)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSegmentsItem.from_dict(
                segments_item_data
            )

            segments.append(segments_item)

        serial_number = d.pop("serialNumber", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSite.from_dict(_site)

        _snmp = d.pop("snmp", UNSET)
        snmp: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp]
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemSnmp.from_dict(_snmp)

        software_version = d.pop("softwareVersion", UNSET)

        static_routes_enabled = d.pop("staticRoutesEnabled", UNSET)

        status = d.pop("status", UNSET)

        _traffic_policy = d.pop("trafficPolicy", UNSET)
        traffic_policy: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy]
        if isinstance(_traffic_policy, Unset):
            traffic_policy = UNSET
        else:
            traffic_policy = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemTrafficPolicy.from_dict(
                _traffic_policy
            )

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = PostV1ExtranetsResponse200PolicyBranchesExcludedDevicesItemUptime.from_dict(_uptime)

        vrrp_enabled = d.pop("vrrpEnabled", UNSET)

        post_v1_extranets_response_200_policy_branches_excluded_devices_item = cls(
            bgp=bgp,
            bgp_enabled=bgp_enabled,
            circuits=circuits,
            config_updated_at=config_updated_at,
            created_at=created_at,
            dhcp_server_enabled=dhcp_server_enabled,
            dns=dns,
            gdi=gdi,
            hostname=hostname,
            id=id,
            interfaces=interfaces,
            internal_state=internal_state,
            ipfix_enabled=ipfix_enabled,
            ipfix_exporters=ipfix_exporters,
            ipsec_tunnels=ipsec_tunnels,
            last_booted_at=last_booted_at,
            lldp_enabled=lldp_enabled,
            local_route_tag=local_route_tag,
            local_web_server_password=local_web_server_password,
            location=location,
            maintenance_mode=maintenance_mode,
            nat_policy=nat_policy,
            notes=notes,
            oper_staled=oper_staled,
            oper_staled_at=oper_staled_at,
            oper_updated_at=oper_updated_at,
            ospfv_2_enabled=ospfv_2_enabled,
            ospfv_3_enabled=ospfv_3_enabled,
            platform=platform,
            prefix_sets=prefix_sets,
            reboot_reason=reboot_reason,
            region=region,
            region_override=region_override,
            role=role,
            routing_policies=routing_policies,
            segments=segments,
            serial_number=serial_number,
            site=site,
            snmp=snmp,
            software_version=software_version,
            static_routes_enabled=static_routes_enabled,
            status=status,
            traffic_policy=traffic_policy,
            uptime=uptime,
            vrrp_enabled=vrrp_enabled,
        )

        post_v1_extranets_response_200_policy_branches_excluded_devices_item.additional_properties = d
        return post_v1_extranets_response_200_policy_branches_excluded_devices_item

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
