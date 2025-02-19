from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_bgp_instance import (
        PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_dns import PutV1DevicesDeviceIdConfigBodyEdgeDns
    from ..models.put_v1_devices_device_id_config_body_edge_interfaces_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_ipfix_exporters_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_local_route_tag import (
        PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_location import PutV1DevicesDeviceIdConfigBodyEdgeLocation
    from ..models.put_v1_devices_device_id_config_body_edge_nat_policy import (
        PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_prefix_sets_item import (
        PutV1DevicesDeviceIdConfigBodyEdgePrefixSetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_route_policies_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeRoutePoliciesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_site import PutV1DevicesDeviceIdConfigBodyEdgeSite
    from ..models.put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp import PutV1DevicesDeviceIdConfigBodyEdgeSnmp
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_global_object_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_traffic_policy import (
        PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdge")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdge:
    """
    Attributes:
        bgp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        bgp_instance (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance]):
        circuits (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItem']]):
        dhcp_server_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        dns (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDns]):
        interfaces (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItem']]):
        ipfix_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ipfix_exporters (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItem']]):
        lldp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        local_route_tag (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag]):
        local_web_server_password (Union[Unset, str]):  Example: TYPE_STRING.
        location (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocation]):
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        nat_policy (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy]):
        ospfv_2_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        ospfv_3_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        prefix_sets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgePrefixSetsItem']]):
        region (Union[Unset, str]):  Example: TYPE_ENUM.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        route_policies (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeRoutePoliciesItem']]):
        segments (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItem']]):
        site (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSite]):
        site_to_site_vpn (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItem']]):
        snmp (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSnmp]):
        snmp_global_object (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItem']]):
        static_routes_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        traffic_policy (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy]):
        vrrp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    bgp_enabled: Union[Unset, str] = UNSET
    bgp_instance: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance"] = UNSET
    circuits: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItem"]] = UNSET
    dhcp_server_enabled: Union[Unset, str] = UNSET
    dns: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeDns"] = UNSET
    interfaces: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItem"]] = UNSET
    ipfix_enabled: Union[Unset, str] = UNSET
    ipfix_exporters: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItem"]] = UNSET
    lldp_enabled: Union[Unset, str] = UNSET
    local_route_tag: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag"] = UNSET
    local_web_server_password: Union[Unset, str] = UNSET
    location: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeLocation"] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nat_policy: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy"] = UNSET
    ospfv_2_enabled: Union[Unset, str] = UNSET
    ospfv_3_enabled: Union[Unset, str] = UNSET
    prefix_sets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgePrefixSetsItem"]] = UNSET
    region: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    route_policies: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeRoutePoliciesItem"]] = UNSET
    segments: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItem"]] = UNSET
    site: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSite"] = UNSET
    site_to_site_vpn: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItem"]] = UNSET
    snmp: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSnmp"] = UNSET
    snmp_global_object: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItem"]] = UNSET
    static_routes_enabled: Union[Unset, str] = UNSET
    traffic_policy: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy"] = UNSET
    vrrp_enabled: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_enabled = self.bgp_enabled

        bgp_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_instance, Unset):
            bgp_instance = self.bgp_instance.to_dict()

        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        dhcp_server_enabled = self.dhcp_server_enabled

        dns: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        ipfix_enabled = self.ipfix_enabled

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        lldp_enabled = self.lldp_enabled

        local_route_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_route_tag, Unset):
            local_route_tag = self.local_route_tag.to_dict()

        local_web_server_password = self.local_web_server_password

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        maintenance_mode = self.maintenance_mode

        name = self.name

        nat_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nat_policy, Unset):
            nat_policy = self.nat_policy.to_dict()

        ospfv_2_enabled = self.ospfv_2_enabled

        ospfv_3_enabled = self.ospfv_3_enabled

        prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_sets, Unset):
            prefix_sets = []
            for prefix_sets_item_data in self.prefix_sets:
                prefix_sets_item = prefix_sets_item_data.to_dict()
                prefix_sets.append(prefix_sets_item)

        region = self.region

        region_name = self.region_name

        route_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.route_policies, Unset):
            route_policies = []
            for route_policies_item_data in self.route_policies:
                route_policies_item = route_policies_item_data.to_dict()
                route_policies.append(route_policies_item)

        segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        site_to_site_vpn: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_to_site_vpn, Unset):
            site_to_site_vpn = []
            for site_to_site_vpn_item_data in self.site_to_site_vpn:
                site_to_site_vpn_item = site_to_site_vpn_item_data.to_dict()
                site_to_site_vpn.append(site_to_site_vpn_item)

        snmp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        snmp_global_object: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snmp_global_object, Unset):
            snmp_global_object = []
            for snmp_global_object_item_data in self.snmp_global_object:
                snmp_global_object_item = snmp_global_object_item_data.to_dict()
                snmp_global_object.append(snmp_global_object_item)

        static_routes_enabled = self.static_routes_enabled

        traffic_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_policy, Unset):
            traffic_policy = self.traffic_policy.to_dict()

        vrrp_enabled = self.vrrp_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_enabled is not UNSET:
            field_dict["bgpEnabled"] = bgp_enabled
        if bgp_instance is not UNSET:
            field_dict["bgpInstance"] = bgp_instance
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if dhcp_server_enabled is not UNSET:
            field_dict["dhcpServerEnabled"] = dhcp_server_enabled
        if dns is not UNSET:
            field_dict["dns"] = dns
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if ipfix_enabled is not UNSET:
            field_dict["ipfixEnabled"] = ipfix_enabled
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
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
        if name is not UNSET:
            field_dict["name"] = name
        if nat_policy is not UNSET:
            field_dict["natPolicy"] = nat_policy
        if ospfv_2_enabled is not UNSET:
            field_dict["ospfv2Enabled"] = ospfv_2_enabled
        if ospfv_3_enabled is not UNSET:
            field_dict["ospfv3Enabled"] = ospfv_3_enabled
        if prefix_sets is not UNSET:
            field_dict["prefixSets"] = prefix_sets
        if region is not UNSET:
            field_dict["region"] = region
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if route_policies is not UNSET:
            field_dict["routePolicies"] = route_policies
        if segments is not UNSET:
            field_dict["segments"] = segments
        if site is not UNSET:
            field_dict["site"] = site
        if site_to_site_vpn is not UNSET:
            field_dict["siteToSiteVpn"] = site_to_site_vpn
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if snmp_global_object is not UNSET:
            field_dict["snmpGlobalObject"] = snmp_global_object
        if static_routes_enabled is not UNSET:
            field_dict["staticRoutesEnabled"] = static_routes_enabled
        if traffic_policy is not UNSET:
            field_dict["trafficPolicy"] = traffic_policy
        if vrrp_enabled is not UNSET:
            field_dict["vrrpEnabled"] = vrrp_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_bgp_instance import (
            PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_dns import PutV1DevicesDeviceIdConfigBodyEdgeDns
        from ..models.put_v1_devices_device_id_config_body_edge_interfaces_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_ipfix_exporters_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_local_route_tag import (
            PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_location import (
            PutV1DevicesDeviceIdConfigBodyEdgeLocation,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_nat_policy import (
            PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_prefix_sets_item import (
            PutV1DevicesDeviceIdConfigBodyEdgePrefixSetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_route_policies_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeRoutePoliciesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_site import PutV1DevicesDeviceIdConfigBodyEdgeSite
        from ..models.put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp import PutV1DevicesDeviceIdConfigBodyEdgeSnmp
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_global_object_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_traffic_policy import (
            PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy,
        )

        d = src_dict.copy()
        bgp_enabled = d.pop("bgpEnabled", UNSET)

        _bgp_instance = d.pop("bgpInstance", UNSET)
        bgp_instance: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance]
        if isinstance(_bgp_instance, Unset):
            bgp_instance = UNSET
        else:
            bgp_instance = PutV1DevicesDeviceIdConfigBodyEdgeBgpInstance.from_dict(_bgp_instance)

        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        dhcp_server_enabled = d.pop("dhcpServerEnabled", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDns]
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = PutV1DevicesDeviceIdConfigBodyEdgeDns.from_dict(_dns)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItem.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        ipfix_enabled = d.pop("ipfixEnabled", UNSET)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItem.from_dict(
                ipfix_exporters_item_data
            )

            ipfix_exporters.append(ipfix_exporters_item)

        lldp_enabled = d.pop("lldpEnabled", UNSET)

        _local_route_tag = d.pop("localRouteTag", UNSET)
        local_route_tag: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag]
        if isinstance(_local_route_tag, Unset):
            local_route_tag = UNSET
        else:
            local_route_tag = PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag.from_dict(_local_route_tag)

        local_web_server_password = d.pop("localWebServerPassword", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = PutV1DevicesDeviceIdConfigBodyEdgeLocation.from_dict(_location)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        name = d.pop("name", UNSET)

        _nat_policy = d.pop("natPolicy", UNSET)
        nat_policy: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy]
        if isinstance(_nat_policy, Unset):
            nat_policy = UNSET
        else:
            nat_policy = PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy.from_dict(_nat_policy)

        ospfv_2_enabled = d.pop("ospfv2Enabled", UNSET)

        ospfv_3_enabled = d.pop("ospfv3Enabled", UNSET)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PutV1DevicesDeviceIdConfigBodyEdgePrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        region = d.pop("region", UNSET)

        region_name = d.pop("regionName", UNSET)

        route_policies = []
        _route_policies = d.pop("routePolicies", UNSET)
        for route_policies_item_data in _route_policies or []:
            route_policies_item = PutV1DevicesDeviceIdConfigBodyEdgeRoutePoliciesItem.from_dict(
                route_policies_item_data
            )

            route_policies.append(route_policies_item)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PutV1DevicesDeviceIdConfigBodyEdgeSite.from_dict(_site)

        site_to_site_vpn = []
        _site_to_site_vpn = d.pop("siteToSiteVpn", UNSET)
        for site_to_site_vpn_item_data in _site_to_site_vpn or []:
            site_to_site_vpn_item = PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItem.from_dict(
                site_to_site_vpn_item_data
            )

            site_to_site_vpn.append(site_to_site_vpn_item)

        _snmp = d.pop("snmp", UNSET)
        snmp: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSnmp]
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = PutV1DevicesDeviceIdConfigBodyEdgeSnmp.from_dict(_snmp)

        snmp_global_object = []
        _snmp_global_object = d.pop("snmpGlobalObject", UNSET)
        for snmp_global_object_item_data in _snmp_global_object or []:
            snmp_global_object_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItem.from_dict(
                snmp_global_object_item_data
            )

            snmp_global_object.append(snmp_global_object_item)

        static_routes_enabled = d.pop("staticRoutesEnabled", UNSET)

        _traffic_policy = d.pop("trafficPolicy", UNSET)
        traffic_policy: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy]
        if isinstance(_traffic_policy, Unset):
            traffic_policy = UNSET
        else:
            traffic_policy = PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicy.from_dict(_traffic_policy)

        vrrp_enabled = d.pop("vrrpEnabled", UNSET)

        put_v1_devices_device_id_config_body_edge = cls(
            bgp_enabled=bgp_enabled,
            bgp_instance=bgp_instance,
            circuits=circuits,
            dhcp_server_enabled=dhcp_server_enabled,
            dns=dns,
            interfaces=interfaces,
            ipfix_enabled=ipfix_enabled,
            ipfix_exporters=ipfix_exporters,
            lldp_enabled=lldp_enabled,
            local_route_tag=local_route_tag,
            local_web_server_password=local_web_server_password,
            location=location,
            maintenance_mode=maintenance_mode,
            name=name,
            nat_policy=nat_policy,
            ospfv_2_enabled=ospfv_2_enabled,
            ospfv_3_enabled=ospfv_3_enabled,
            prefix_sets=prefix_sets,
            region=region,
            region_name=region_name,
            route_policies=route_policies,
            segments=segments,
            site=site,
            site_to_site_vpn=site_to_site_vpn,
            snmp=snmp,
            snmp_global_object=snmp_global_object,
            static_routes_enabled=static_routes_enabled,
            traffic_policy=traffic_policy,
            vrrp_enabled=vrrp_enabled,
        )

        put_v1_devices_device_id_config_body_edge.additional_properties = d
        return put_v1_devices_device_id_config_body_edge

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
