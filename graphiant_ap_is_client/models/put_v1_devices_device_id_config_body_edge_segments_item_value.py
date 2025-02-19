from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_aggregations_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpAggregationsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_neighbors_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpNeighborsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_redistribution_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpRedistributionItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_dhcp_subnets_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueDhcpSubnetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ebgp_multipath import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ipfix_exporters_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueIpfixExportersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_nat_ruleset import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ospfv_2 import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ospfv_3 import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_overlay_filters import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_static_routes_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueStaticRoutesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_syslog_targets_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueSyslogTargetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_traffic_ruleset import (
        PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValue:
    """
    Attributes:
        bgp_aggregations (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpAggregationsItem']]):
        bgp_neighbors (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpNeighborsItem']]):
        bgp_redistribution (Union[Unset,
            list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpRedistributionItem']]):
        dhcp_subnets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueDhcpSubnetsItem']]):
        ebgp_multipath (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath]):
        ipfix_exporters (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueIpfixExportersItem']]):
        nat_ruleset (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset]):
        networks (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ospfv2 (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2]):
        ospfv3 (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3]):
        overlay_filters (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters]):
        static_routes (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueStaticRoutesItem']]):
        syslog_targets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueSyslogTargetsItem']]):
        traffic_ruleset (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset]):
    """

    bgp_aggregations: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpAggregationsItem"]] = (
        UNSET
    )
    bgp_neighbors: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpNeighborsItem"]] = UNSET
    bgp_redistribution: Union[
        Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpRedistributionItem"]
    ] = UNSET
    dhcp_subnets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueDhcpSubnetsItem"]] = UNSET
    ebgp_multipath: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath"] = UNSET
    ipfix_exporters: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueIpfixExportersItem"]] = UNSET
    nat_ruleset: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset"] = UNSET
    networks: Union[Unset, list[str]] = UNSET
    ospfv2: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2"] = UNSET
    ospfv3: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3"] = UNSET
    overlay_filters: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters"] = UNSET
    static_routes: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueStaticRoutesItem"]] = UNSET
    syslog_targets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueSyslogTargetsItem"]] = UNSET
    traffic_ruleset: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset"] = UNSET
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
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_aggregations_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpAggregationsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_neighbors_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpNeighborsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_bgp_redistribution_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpRedistributionItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_dhcp_subnets_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueDhcpSubnetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ebgp_multipath import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ipfix_exporters_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueIpfixExportersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_nat_ruleset import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ospfv_2 import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_ospfv_3 import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_overlay_filters import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_static_routes_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueStaticRoutesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_syslog_targets_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueSyslogTargetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_segments_item_value_traffic_ruleset import (
            PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset,
        )

        d = src_dict.copy()
        bgp_aggregations = []
        _bgp_aggregations = d.pop("bgpAggregations", UNSET)
        for bgp_aggregations_item_data in _bgp_aggregations or []:
            bgp_aggregations_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpAggregationsItem.from_dict(
                bgp_aggregations_item_data
            )

            bgp_aggregations.append(bgp_aggregations_item)

        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgpNeighbors", UNSET)
        for bgp_neighbors_item_data in _bgp_neighbors or []:
            bgp_neighbors_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpNeighborsItem.from_dict(
                bgp_neighbors_item_data
            )

            bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistribution = []
        _bgp_redistribution = d.pop("bgpRedistribution", UNSET)
        for bgp_redistribution_item_data in _bgp_redistribution or []:
            bgp_redistribution_item = (
                PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueBgpRedistributionItem.from_dict(
                    bgp_redistribution_item_data
                )
            )

            bgp_redistribution.append(bgp_redistribution_item)

        dhcp_subnets = []
        _dhcp_subnets = d.pop("dhcpSubnets", UNSET)
        for dhcp_subnets_item_data in _dhcp_subnets or []:
            dhcp_subnets_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueDhcpSubnetsItem.from_dict(
                dhcp_subnets_item_data
            )

            dhcp_subnets.append(dhcp_subnets_item)

        _ebgp_multipath = d.pop("ebgpMultipath", UNSET)
        ebgp_multipath: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath]
        if isinstance(_ebgp_multipath, Unset):
            ebgp_multipath = UNSET
        else:
            ebgp_multipath = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueEbgpMultipath.from_dict(_ebgp_multipath)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueIpfixExportersItem.from_dict(
                ipfix_exporters_item_data
            )

            ipfix_exporters.append(ipfix_exporters_item)

        _nat_ruleset = d.pop("natRuleset", UNSET)
        nat_ruleset: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset]
        if isinstance(_nat_ruleset, Unset):
            nat_ruleset = UNSET
        else:
            nat_ruleset = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueNatRuleset.from_dict(_nat_ruleset)

        networks = cast(list[str], d.pop("networks", UNSET))

        _ospfv2 = d.pop("ospfv2", UNSET)
        ospfv2: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2]
        if isinstance(_ospfv2, Unset):
            ospfv2 = UNSET
        else:
            ospfv2 = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv2.from_dict(_ospfv2)

        _ospfv3 = d.pop("ospfv3", UNSET)
        ospfv3: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3]
        if isinstance(_ospfv3, Unset):
            ospfv3 = UNSET
        else:
            ospfv3 = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOspfv3.from_dict(_ospfv3)

        _overlay_filters = d.pop("overlayFilters", UNSET)
        overlay_filters: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters]
        if isinstance(_overlay_filters, Unset):
            overlay_filters = UNSET
        else:
            overlay_filters = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueOverlayFilters.from_dict(
                _overlay_filters
            )

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueStaticRoutesItem.from_dict(
                static_routes_item_data
            )

            static_routes.append(static_routes_item)

        syslog_targets = []
        _syslog_targets = d.pop("syslogTargets", UNSET)
        for syslog_targets_item_data in _syslog_targets or []:
            syslog_targets_item = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueSyslogTargetsItem.from_dict(
                syslog_targets_item_data
            )

            syslog_targets.append(syslog_targets_item)

        _traffic_ruleset = d.pop("trafficRuleset", UNSET)
        traffic_ruleset: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset]
        if isinstance(_traffic_ruleset, Unset):
            traffic_ruleset = UNSET
        else:
            traffic_ruleset = PutV1DevicesDeviceIdConfigBodyEdgeSegmentsItemValueTrafficRuleset.from_dict(
                _traffic_ruleset
            )

        put_v1_devices_device_id_config_body_edge_segments_item_value = cls(
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

        put_v1_devices_device_id_config_body_edge_segments_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_segments_item_value

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
