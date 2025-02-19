from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_aggregations_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpAggregationsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_neighbors_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpNeighborsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_redistribution_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpRedistributionItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_dhcp_subnets_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfDhcpSubnetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ebgp_multipath import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ipfix_exporters_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfIpfixExportersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_nat_ruleset import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_2 import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3 import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_static_routes_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfStaticRoutesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_syslog_targets_item import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfSyslogTargetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_traffic_ruleset import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreCoreVrf")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreCoreVrf:
    """
    Attributes:
        bgp_aggregations (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpAggregationsItem']]):
        bgp_neighbors (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpNeighborsItem']]):
        bgp_redistribution (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpRedistributionItem']]):
        dhcp_subnets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfDhcpSubnetsItem']]):
        ebgp_multipath (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath]):
        ipfix_exporters (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfIpfixExportersItem']]):
        nat_ruleset (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset]):
        networks (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ospfv2 (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2]):
        ospfv3 (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3]):
        overlay_filters (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters]):
        static_routes (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfStaticRoutesItem']]):
        syslog_targets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreCoreVrfSyslogTargetsItem']]):
        traffic_ruleset (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset]):
    """

    bgp_aggregations: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpAggregationsItem"]] = UNSET
    bgp_neighbors: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpNeighborsItem"]] = UNSET
    bgp_redistribution: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpRedistributionItem"]] = UNSET
    dhcp_subnets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfDhcpSubnetsItem"]] = UNSET
    ebgp_multipath: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath"] = UNSET
    ipfix_exporters: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfIpfixExportersItem"]] = UNSET
    nat_ruleset: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset"] = UNSET
    networks: Union[Unset, list[str]] = UNSET
    ospfv2: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2"] = UNSET
    ospfv3: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3"] = UNSET
    overlay_filters: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters"] = UNSET
    static_routes: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfStaticRoutesItem"]] = UNSET
    syslog_targets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreCoreVrfSyslogTargetsItem"]] = UNSET
    traffic_ruleset: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_aggregations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_aggregations, Unset):
            bgp_aggregations = []
            for bgp_aggregations_item_data in self.bgp_aggregations:
                bgp_aggregations_item = bgp_aggregations_item_data.to_dict()
                bgp_aggregations.append(bgp_aggregations_item)

        bgp_neighbors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_neighbors, Unset):
            bgp_neighbors = []
            for bgp_neighbors_item_data in self.bgp_neighbors:
                bgp_neighbors_item = bgp_neighbors_item_data.to_dict()
                bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistribution: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_redistribution, Unset):
            bgp_redistribution = []
            for bgp_redistribution_item_data in self.bgp_redistribution:
                bgp_redistribution_item = bgp_redistribution_item_data.to_dict()
                bgp_redistribution.append(bgp_redistribution_item)

        dhcp_subnets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dhcp_subnets, Unset):
            dhcp_subnets = []
            for dhcp_subnets_item_data in self.dhcp_subnets:
                dhcp_subnets_item = dhcp_subnets_item_data.to_dict()
                dhcp_subnets.append(dhcp_subnets_item)

        ebgp_multipath: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ebgp_multipath, Unset):
            ebgp_multipath = self.ebgp_multipath.to_dict()

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        nat_ruleset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nat_ruleset, Unset):
            nat_ruleset = self.nat_ruleset.to_dict()

        networks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        ospfv2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ospfv2, Unset):
            ospfv2 = self.ospfv2.to_dict()

        ospfv3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ospfv3, Unset):
            ospfv3 = self.ospfv3.to_dict()

        overlay_filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.overlay_filters, Unset):
            overlay_filters = self.overlay_filters.to_dict()

        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        syslog_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_targets, Unset):
            syslog_targets = []
            for syslog_targets_item_data in self.syslog_targets:
                syslog_targets_item = syslog_targets_item_data.to_dict()
                syslog_targets.append(syslog_targets_item)

        traffic_ruleset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_ruleset, Unset):
            traffic_ruleset = self.traffic_ruleset.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_aggregations is not UNSET:
            field_dict["bgpAggregations"] = bgp_aggregations
        if bgp_neighbors is not UNSET:
            field_dict["bgpNeighbors"] = bgp_neighbors
        if bgp_redistribution is not UNSET:
            field_dict["bgpRedistribution"] = bgp_redistribution
        if dhcp_subnets is not UNSET:
            field_dict["dhcpSubnets"] = dhcp_subnets
        if ebgp_multipath is not UNSET:
            field_dict["ebgpMultipath"] = ebgp_multipath
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
        if nat_ruleset is not UNSET:
            field_dict["natRuleset"] = nat_ruleset
        if networks is not UNSET:
            field_dict["networks"] = networks
        if ospfv2 is not UNSET:
            field_dict["ospfv2"] = ospfv2
        if ospfv3 is not UNSET:
            field_dict["ospfv3"] = ospfv3
        if overlay_filters is not UNSET:
            field_dict["overlayFilters"] = overlay_filters
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes
        if syslog_targets is not UNSET:
            field_dict["syslogTargets"] = syslog_targets
        if traffic_ruleset is not UNSET:
            field_dict["trafficRuleset"] = traffic_ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_aggregations_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpAggregationsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_neighbors_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpNeighborsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_bgp_redistribution_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpRedistributionItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_dhcp_subnets_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfDhcpSubnetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ebgp_multipath import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ipfix_exporters_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfIpfixExportersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_nat_ruleset import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_2 import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3 import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_static_routes_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfStaticRoutesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_syslog_targets_item import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfSyslogTargetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_traffic_ruleset import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset,
        )

        d = src_dict.copy()
        bgp_aggregations = []
        _bgp_aggregations = d.pop("bgpAggregations", UNSET)
        for bgp_aggregations_item_data in _bgp_aggregations or []:
            bgp_aggregations_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpAggregationsItem.from_dict(
                bgp_aggregations_item_data
            )

            bgp_aggregations.append(bgp_aggregations_item)

        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgpNeighbors", UNSET)
        for bgp_neighbors_item_data in _bgp_neighbors or []:
            bgp_neighbors_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpNeighborsItem.from_dict(
                bgp_neighbors_item_data
            )

            bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistribution = []
        _bgp_redistribution = d.pop("bgpRedistribution", UNSET)
        for bgp_redistribution_item_data in _bgp_redistribution or []:
            bgp_redistribution_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfBgpRedistributionItem.from_dict(
                bgp_redistribution_item_data
            )

            bgp_redistribution.append(bgp_redistribution_item)

        dhcp_subnets = []
        _dhcp_subnets = d.pop("dhcpSubnets", UNSET)
        for dhcp_subnets_item_data in _dhcp_subnets or []:
            dhcp_subnets_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfDhcpSubnetsItem.from_dict(
                dhcp_subnets_item_data
            )

            dhcp_subnets.append(dhcp_subnets_item)

        _ebgp_multipath = d.pop("ebgpMultipath", UNSET)
        ebgp_multipath: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath]
        if isinstance(_ebgp_multipath, Unset):
            ebgp_multipath = UNSET
        else:
            ebgp_multipath = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfEbgpMultipath.from_dict(_ebgp_multipath)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfIpfixExportersItem.from_dict(
                ipfix_exporters_item_data
            )

            ipfix_exporters.append(ipfix_exporters_item)

        _nat_ruleset = d.pop("natRuleset", UNSET)
        nat_ruleset: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset]
        if isinstance(_nat_ruleset, Unset):
            nat_ruleset = UNSET
        else:
            nat_ruleset = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfNatRuleset.from_dict(_nat_ruleset)

        networks = cast(list[str], d.pop("networks", UNSET))

        _ospfv2 = d.pop("ospfv2", UNSET)
        ospfv2: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2]
        if isinstance(_ospfv2, Unset):
            ospfv2 = UNSET
        else:
            ospfv2 = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv2.from_dict(_ospfv2)

        _ospfv3 = d.pop("ospfv3", UNSET)
        ospfv3: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3]
        if isinstance(_ospfv3, Unset):
            ospfv3 = UNSET
        else:
            ospfv3 = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3.from_dict(_ospfv3)

        _overlay_filters = d.pop("overlayFilters", UNSET)
        overlay_filters: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters]
        if isinstance(_overlay_filters, Unset):
            overlay_filters = UNSET
        else:
            overlay_filters = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters.from_dict(_overlay_filters)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfStaticRoutesItem.from_dict(
                static_routes_item_data
            )

            static_routes.append(static_routes_item)

        syslog_targets = []
        _syslog_targets = d.pop("syslogTargets", UNSET)
        for syslog_targets_item_data in _syslog_targets or []:
            syslog_targets_item = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfSyslogTargetsItem.from_dict(
                syslog_targets_item_data
            )

            syslog_targets.append(syslog_targets_item)

        _traffic_ruleset = d.pop("trafficRuleset", UNSET)
        traffic_ruleset: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset]
        if isinstance(_traffic_ruleset, Unset):
            traffic_ruleset = UNSET
        else:
            traffic_ruleset = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset.from_dict(_traffic_ruleset)

        put_v1_devices_device_id_config_body_core_core_vrf = cls(
            bgp_aggregations=bgp_aggregations,
            bgp_neighbors=bgp_neighbors,
            bgp_redistribution=bgp_redistribution,
            dhcp_subnets=dhcp_subnets,
            ebgp_multipath=ebgp_multipath,
            ipfix_exporters=ipfix_exporters,
            nat_ruleset=nat_ruleset,
            networks=networks,
            ospfv2=ospfv2,
            ospfv3=ospfv3,
            overlay_filters=overlay_filters,
            static_routes=static_routes,
            syslog_targets=syslog_targets,
            traffic_ruleset=traffic_ruleset,
        )

        put_v1_devices_device_id_config_body_core_core_vrf.additional_properties = d
        return put_v1_devices_device_id_config_body_core_core_vrf

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
