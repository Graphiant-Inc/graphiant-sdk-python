from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_response_200_devices_item_bgp import GetV1DevicesResponse200DevicesItemBgp
    from ..models.get_v1_devices_response_200_devices_item_circuits_item import (
        GetV1DevicesResponse200DevicesItemCircuitsItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_config_updated_at import (
        GetV1DevicesResponse200DevicesItemConfigUpdatedAt,
    )
    from ..models.get_v1_devices_response_200_devices_item_created_at import GetV1DevicesResponse200DevicesItemCreatedAt
    from ..models.get_v1_devices_response_200_devices_item_dns import GetV1DevicesResponse200DevicesItemDns
    from ..models.get_v1_devices_response_200_devices_item_interfaces_item import (
        GetV1DevicesResponse200DevicesItemInterfacesItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_ipfix_exporters_item import (
        GetV1DevicesResponse200DevicesItemIpfixExportersItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_ipsec_tunnels_item import (
        GetV1DevicesResponse200DevicesItemIpsecTunnelsItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_last_booted_at import (
        GetV1DevicesResponse200DevicesItemLastBootedAt,
    )
    from ..models.get_v1_devices_response_200_devices_item_local_route_tag import (
        GetV1DevicesResponse200DevicesItemLocalRouteTag,
    )
    from ..models.get_v1_devices_response_200_devices_item_location import GetV1DevicesResponse200DevicesItemLocation
    from ..models.get_v1_devices_response_200_devices_item_nat_policy import GetV1DevicesResponse200DevicesItemNatPolicy
    from ..models.get_v1_devices_response_200_devices_item_oper_staled_at import (
        GetV1DevicesResponse200DevicesItemOperStaledAt,
    )
    from ..models.get_v1_devices_response_200_devices_item_oper_updated_at import (
        GetV1DevicesResponse200DevicesItemOperUpdatedAt,
    )
    from ..models.get_v1_devices_response_200_devices_item_prefix_sets_item import (
        GetV1DevicesResponse200DevicesItemPrefixSetsItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_region import GetV1DevicesResponse200DevicesItemRegion
    from ..models.get_v1_devices_response_200_devices_item_region_override import (
        GetV1DevicesResponse200DevicesItemRegionOverride,
    )
    from ..models.get_v1_devices_response_200_devices_item_routing_policies_item import (
        GetV1DevicesResponse200DevicesItemRoutingPoliciesItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_segments_item import (
        GetV1DevicesResponse200DevicesItemSegmentsItem,
    )
    from ..models.get_v1_devices_response_200_devices_item_site import GetV1DevicesResponse200DevicesItemSite
    from ..models.get_v1_devices_response_200_devices_item_snmp import GetV1DevicesResponse200DevicesItemSnmp
    from ..models.get_v1_devices_response_200_devices_item_traffic_policy import (
        GetV1DevicesResponse200DevicesItemTrafficPolicy,
    )
    from ..models.get_v1_devices_response_200_devices_item_uptime import GetV1DevicesResponse200DevicesItemUptime


T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItem")


@_attrs_define
class GetV1DevicesResponse200DevicesItem:
    """
    Attributes:
        bgp (Union[Unset, GetV1DevicesResponse200DevicesItemBgp]):
        bgp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        circuits (Union[Unset, list['GetV1DevicesResponse200DevicesItemCircuitsItem']]):
        config_updated_at (Union[Unset, GetV1DevicesResponse200DevicesItemConfigUpdatedAt]):
        created_at (Union[Unset, GetV1DevicesResponse200DevicesItemCreatedAt]):
        dhcp_server_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        dns (Union[Unset, GetV1DevicesResponse200DevicesItemDns]):
        gdi (Union[Unset, str]):  Example: TYPE_UINT32.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interfaces (Union[Unset, list['GetV1DevicesResponse200DevicesItemInterfacesItem']]):
        internal_state (Union[Unset, str]):  Example: TYPE_ENUM.
        ipfix_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ipfix_exporters (Union[Unset, list['GetV1DevicesResponse200DevicesItemIpfixExportersItem']]):
        ipsec_tunnels (Union[Unset, list['GetV1DevicesResponse200DevicesItemIpsecTunnelsItem']]):
        last_booted_at (Union[Unset, GetV1DevicesResponse200DevicesItemLastBootedAt]):
        lldp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        local_route_tag (Union[Unset, GetV1DevicesResponse200DevicesItemLocalRouteTag]):
        local_web_server_password (Union[Unset, str]):  Example: TYPE_STRING.
        location (Union[Unset, GetV1DevicesResponse200DevicesItemLocation]):
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        nat_policy (Union[Unset, GetV1DevicesResponse200DevicesItemNatPolicy]):
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        oper_staled (Union[Unset, str]):  Example: TYPE_BOOL.
        oper_staled_at (Union[Unset, GetV1DevicesResponse200DevicesItemOperStaledAt]):
        oper_updated_at (Union[Unset, GetV1DevicesResponse200DevicesItemOperUpdatedAt]):
        ospfv_2_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ospfv_3_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        platform (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_sets (Union[Unset, list['GetV1DevicesResponse200DevicesItemPrefixSetsItem']]):
        reboot_reason (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, GetV1DevicesResponse200DevicesItemRegion]):
        region_override (Union[Unset, GetV1DevicesResponse200DevicesItemRegionOverride]):
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        routing_policies (Union[Unset, list['GetV1DevicesResponse200DevicesItemRoutingPoliciesItem']]):
        segments (Union[Unset, list['GetV1DevicesResponse200DevicesItemSegmentsItem']]):
        serial_number (Union[Unset, str]):  Example: TYPE_STRING.
        site (Union[Unset, GetV1DevicesResponse200DevicesItemSite]):
        snmp (Union[Unset, GetV1DevicesResponse200DevicesItemSnmp]):
        software_version (Union[Unset, str]):  Example: TYPE_STRING.
        static_routes_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        traffic_policy (Union[Unset, GetV1DevicesResponse200DevicesItemTrafficPolicy]):
        uptime (Union[Unset, GetV1DevicesResponse200DevicesItemUptime]):
        vrrp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    bgp: Union[Unset, "GetV1DevicesResponse200DevicesItemBgp"] = UNSET
    bgp_enabled: Union[Unset, str] = UNSET
    circuits: Union[Unset, list["GetV1DevicesResponse200DevicesItemCircuitsItem"]] = UNSET
    config_updated_at: Union[Unset, "GetV1DevicesResponse200DevicesItemConfigUpdatedAt"] = UNSET
    created_at: Union[Unset, "GetV1DevicesResponse200DevicesItemCreatedAt"] = UNSET
    dhcp_server_enabled: Union[Unset, str] = UNSET
    dns: Union[Unset, "GetV1DevicesResponse200DevicesItemDns"] = UNSET
    gdi: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interfaces: Union[Unset, list["GetV1DevicesResponse200DevicesItemInterfacesItem"]] = UNSET
    internal_state: Union[Unset, str] = UNSET
    ipfix_enabled: Union[Unset, str] = UNSET
    ipfix_exporters: Union[Unset, list["GetV1DevicesResponse200DevicesItemIpfixExportersItem"]] = UNSET
    ipsec_tunnels: Union[Unset, list["GetV1DevicesResponse200DevicesItemIpsecTunnelsItem"]] = UNSET
    last_booted_at: Union[Unset, "GetV1DevicesResponse200DevicesItemLastBootedAt"] = UNSET
    lldp_enabled: Union[Unset, str] = UNSET
    local_route_tag: Union[Unset, "GetV1DevicesResponse200DevicesItemLocalRouteTag"] = UNSET
    local_web_server_password: Union[Unset, str] = UNSET
    location: Union[Unset, "GetV1DevicesResponse200DevicesItemLocation"] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    nat_policy: Union[Unset, "GetV1DevicesResponse200DevicesItemNatPolicy"] = UNSET
    notes: Union[Unset, str] = UNSET
    oper_staled: Union[Unset, str] = UNSET
    oper_staled_at: Union[Unset, "GetV1DevicesResponse200DevicesItemOperStaledAt"] = UNSET
    oper_updated_at: Union[Unset, "GetV1DevicesResponse200DevicesItemOperUpdatedAt"] = UNSET
    ospfv_2_enabled: Union[Unset, str] = UNSET
    ospfv_3_enabled: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    prefix_sets: Union[Unset, list["GetV1DevicesResponse200DevicesItemPrefixSetsItem"]] = UNSET
    reboot_reason: Union[Unset, str] = UNSET
    region: Union[Unset, "GetV1DevicesResponse200DevicesItemRegion"] = UNSET
    region_override: Union[Unset, "GetV1DevicesResponse200DevicesItemRegionOverride"] = UNSET
    role: Union[Unset, str] = UNSET
    routing_policies: Union[Unset, list["GetV1DevicesResponse200DevicesItemRoutingPoliciesItem"]] = UNSET
    segments: Union[Unset, list["GetV1DevicesResponse200DevicesItemSegmentsItem"]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    site: Union[Unset, "GetV1DevicesResponse200DevicesItemSite"] = UNSET
    snmp: Union[Unset, "GetV1DevicesResponse200DevicesItemSnmp"] = UNSET
    software_version: Union[Unset, str] = UNSET
    static_routes_enabled: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    traffic_policy: Union[Unset, "GetV1DevicesResponse200DevicesItemTrafficPolicy"] = UNSET
    uptime: Union[Unset, "GetV1DevicesResponse200DevicesItemUptime"] = UNSET
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
        from ..models.get_v1_devices_response_200_devices_item_bgp import GetV1DevicesResponse200DevicesItemBgp
        from ..models.get_v1_devices_response_200_devices_item_circuits_item import (
            GetV1DevicesResponse200DevicesItemCircuitsItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_config_updated_at import (
            GetV1DevicesResponse200DevicesItemConfigUpdatedAt,
        )
        from ..models.get_v1_devices_response_200_devices_item_created_at import (
            GetV1DevicesResponse200DevicesItemCreatedAt,
        )
        from ..models.get_v1_devices_response_200_devices_item_dns import GetV1DevicesResponse200DevicesItemDns
        from ..models.get_v1_devices_response_200_devices_item_interfaces_item import (
            GetV1DevicesResponse200DevicesItemInterfacesItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_ipfix_exporters_item import (
            GetV1DevicesResponse200DevicesItemIpfixExportersItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_ipsec_tunnels_item import (
            GetV1DevicesResponse200DevicesItemIpsecTunnelsItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_last_booted_at import (
            GetV1DevicesResponse200DevicesItemLastBootedAt,
        )
        from ..models.get_v1_devices_response_200_devices_item_local_route_tag import (
            GetV1DevicesResponse200DevicesItemLocalRouteTag,
        )
        from ..models.get_v1_devices_response_200_devices_item_location import (
            GetV1DevicesResponse200DevicesItemLocation,
        )
        from ..models.get_v1_devices_response_200_devices_item_nat_policy import (
            GetV1DevicesResponse200DevicesItemNatPolicy,
        )
        from ..models.get_v1_devices_response_200_devices_item_oper_staled_at import (
            GetV1DevicesResponse200DevicesItemOperStaledAt,
        )
        from ..models.get_v1_devices_response_200_devices_item_oper_updated_at import (
            GetV1DevicesResponse200DevicesItemOperUpdatedAt,
        )
        from ..models.get_v1_devices_response_200_devices_item_prefix_sets_item import (
            GetV1DevicesResponse200DevicesItemPrefixSetsItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_region import GetV1DevicesResponse200DevicesItemRegion
        from ..models.get_v1_devices_response_200_devices_item_region_override import (
            GetV1DevicesResponse200DevicesItemRegionOverride,
        )
        from ..models.get_v1_devices_response_200_devices_item_routing_policies_item import (
            GetV1DevicesResponse200DevicesItemRoutingPoliciesItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_segments_item import (
            GetV1DevicesResponse200DevicesItemSegmentsItem,
        )
        from ..models.get_v1_devices_response_200_devices_item_site import GetV1DevicesResponse200DevicesItemSite
        from ..models.get_v1_devices_response_200_devices_item_snmp import GetV1DevicesResponse200DevicesItemSnmp
        from ..models.get_v1_devices_response_200_devices_item_traffic_policy import (
            GetV1DevicesResponse200DevicesItemTrafficPolicy,
        )
        from ..models.get_v1_devices_response_200_devices_item_uptime import GetV1DevicesResponse200DevicesItemUptime

        d = src_dict.copy()
        _bgp = d.pop("bgp", UNSET)
        bgp: Union[Unset, GetV1DevicesResponse200DevicesItemBgp]
        if isinstance(_bgp, Unset):
            bgp = UNSET
        else:
            bgp = GetV1DevicesResponse200DevicesItemBgp.from_dict(_bgp)

        bgp_enabled = d.pop("bgpEnabled", UNSET)

        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = GetV1DevicesResponse200DevicesItemCircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        _config_updated_at = d.pop("configUpdatedAt", UNSET)
        config_updated_at: Union[Unset, GetV1DevicesResponse200DevicesItemConfigUpdatedAt]
        if isinstance(_config_updated_at, Unset):
            config_updated_at = UNSET
        else:
            config_updated_at = GetV1DevicesResponse200DevicesItemConfigUpdatedAt.from_dict(_config_updated_at)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1DevicesResponse200DevicesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1DevicesResponse200DevicesItemCreatedAt.from_dict(_created_at)

        dhcp_server_enabled = d.pop("dhcpServerEnabled", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: Union[Unset, GetV1DevicesResponse200DevicesItemDns]
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = GetV1DevicesResponse200DevicesItemDns.from_dict(_dns)

        gdi = d.pop("gdi", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = GetV1DevicesResponse200DevicesItemInterfacesItem.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        internal_state = d.pop("internalState", UNSET)

        ipfix_enabled = d.pop("ipfixEnabled", UNSET)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = GetV1DevicesResponse200DevicesItemIpfixExportersItem.from_dict(
                ipfix_exporters_item_data
            )

            ipfix_exporters.append(ipfix_exporters_item)

        ipsec_tunnels = []
        _ipsec_tunnels = d.pop("ipsecTunnels", UNSET)
        for ipsec_tunnels_item_data in _ipsec_tunnels or []:
            ipsec_tunnels_item = GetV1DevicesResponse200DevicesItemIpsecTunnelsItem.from_dict(ipsec_tunnels_item_data)

            ipsec_tunnels.append(ipsec_tunnels_item)

        _last_booted_at = d.pop("lastBootedAt", UNSET)
        last_booted_at: Union[Unset, GetV1DevicesResponse200DevicesItemLastBootedAt]
        if isinstance(_last_booted_at, Unset):
            last_booted_at = UNSET
        else:
            last_booted_at = GetV1DevicesResponse200DevicesItemLastBootedAt.from_dict(_last_booted_at)

        lldp_enabled = d.pop("lldpEnabled", UNSET)

        _local_route_tag = d.pop("localRouteTag", UNSET)
        local_route_tag: Union[Unset, GetV1DevicesResponse200DevicesItemLocalRouteTag]
        if isinstance(_local_route_tag, Unset):
            local_route_tag = UNSET
        else:
            local_route_tag = GetV1DevicesResponse200DevicesItemLocalRouteTag.from_dict(_local_route_tag)

        local_web_server_password = d.pop("localWebServerPassword", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, GetV1DevicesResponse200DevicesItemLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GetV1DevicesResponse200DevicesItemLocation.from_dict(_location)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        _nat_policy = d.pop("natPolicy", UNSET)
        nat_policy: Union[Unset, GetV1DevicesResponse200DevicesItemNatPolicy]
        if isinstance(_nat_policy, Unset):
            nat_policy = UNSET
        else:
            nat_policy = GetV1DevicesResponse200DevicesItemNatPolicy.from_dict(_nat_policy)

        notes = d.pop("notes", UNSET)

        oper_staled = d.pop("operStaled", UNSET)

        _oper_staled_at = d.pop("operStaledAt", UNSET)
        oper_staled_at: Union[Unset, GetV1DevicesResponse200DevicesItemOperStaledAt]
        if isinstance(_oper_staled_at, Unset):
            oper_staled_at = UNSET
        else:
            oper_staled_at = GetV1DevicesResponse200DevicesItemOperStaledAt.from_dict(_oper_staled_at)

        _oper_updated_at = d.pop("operUpdatedAt", UNSET)
        oper_updated_at: Union[Unset, GetV1DevicesResponse200DevicesItemOperUpdatedAt]
        if isinstance(_oper_updated_at, Unset):
            oper_updated_at = UNSET
        else:
            oper_updated_at = GetV1DevicesResponse200DevicesItemOperUpdatedAt.from_dict(_oper_updated_at)

        ospfv_2_enabled = d.pop("ospfv2Enabled", UNSET)

        ospfv_3_enabled = d.pop("ospfv3Enabled", UNSET)

        platform = d.pop("platform", UNSET)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = GetV1DevicesResponse200DevicesItemPrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        reboot_reason = d.pop("rebootReason", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1DevicesResponse200DevicesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1DevicesResponse200DevicesItemRegion.from_dict(_region)

        _region_override = d.pop("regionOverride", UNSET)
        region_override: Union[Unset, GetV1DevicesResponse200DevicesItemRegionOverride]
        if isinstance(_region_override, Unset):
            region_override = UNSET
        else:
            region_override = GetV1DevicesResponse200DevicesItemRegionOverride.from_dict(_region_override)

        role = d.pop("role", UNSET)

        routing_policies = []
        _routing_policies = d.pop("routingPolicies", UNSET)
        for routing_policies_item_data in _routing_policies or []:
            routing_policies_item = GetV1DevicesResponse200DevicesItemRoutingPoliciesItem.from_dict(
                routing_policies_item_data
            )

            routing_policies.append(routing_policies_item)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = GetV1DevicesResponse200DevicesItemSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        serial_number = d.pop("serialNumber", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, GetV1DevicesResponse200DevicesItemSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = GetV1DevicesResponse200DevicesItemSite.from_dict(_site)

        _snmp = d.pop("snmp", UNSET)
        snmp: Union[Unset, GetV1DevicesResponse200DevicesItemSnmp]
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = GetV1DevicesResponse200DevicesItemSnmp.from_dict(_snmp)

        software_version = d.pop("softwareVersion", UNSET)

        static_routes_enabled = d.pop("staticRoutesEnabled", UNSET)

        status = d.pop("status", UNSET)

        _traffic_policy = d.pop("trafficPolicy", UNSET)
        traffic_policy: Union[Unset, GetV1DevicesResponse200DevicesItemTrafficPolicy]
        if isinstance(_traffic_policy, Unset):
            traffic_policy = UNSET
        else:
            traffic_policy = GetV1DevicesResponse200DevicesItemTrafficPolicy.from_dict(_traffic_policy)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, GetV1DevicesResponse200DevicesItemUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = GetV1DevicesResponse200DevicesItemUptime.from_dict(_uptime)

        vrrp_enabled = d.pop("vrrpEnabled", UNSET)

        get_v1_devices_response_200_devices_item = cls(
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

        get_v1_devices_response_200_devices_item.additional_properties = d
        return get_v1_devices_response_200_devices_item

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
