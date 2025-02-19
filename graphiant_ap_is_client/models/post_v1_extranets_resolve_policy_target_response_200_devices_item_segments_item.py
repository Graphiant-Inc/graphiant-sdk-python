from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_aggregations_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpAggregationsItem,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_multipath import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_neighbors_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpNeighborsItem,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_redistributions import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_dhcp_subnets_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemDhcpSubnetsItem,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ipfix_exporters_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemIpfixExportersItem,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ospfv_2_process import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ospfv_3_process import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_overlay_filters import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_static_routes_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemStaticRoutesItem,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_syslog_targets_item import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemSyslogTargetsItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItem")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItem:
    """
    Attributes:
        bgp_aggregations (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpAggregationsItem']]):
        bgp_multipath (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath]):
        bgp_neighbors (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpNeighborsItem']]):
        bgp_redistributions (Union[Unset,
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        dhcp_subnets (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemDhcpSubnetsItem']]):
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        function (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ipfix_exporters (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemIpfixExportersItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        nat_ruleset (Union[Unset, str]):  Example: TYPE_STRING.
        networks (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ospfv_2_process (Union[Unset,
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process]):
        ospfv_3_process (Union[Unset,
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process]):
        overlay_filters (Union[Unset,
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters]):
        routable (Union[Unset, str]):  Example: TYPE_BOOL.
        route_distinguisher (Union[Unset, str]):  Example: TYPE_STRING.
        static_routes (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemStaticRoutesItem']]):
        syslog_targets (Union[Unset,
            list['PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemSyslogTargetsItem']]):
        traffic_ruleset (Union[Unset, str]):  Example: TYPE_STRING.
    """

    bgp_aggregations: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpAggregationsItem"]
    ] = UNSET
    bgp_multipath: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath"] = (
        UNSET
    )
    bgp_neighbors: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpNeighborsItem"]
    ] = UNSET
    bgp_redistributions: Union[
        Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions"
    ] = UNSET
    description: Union[Unset, str] = UNSET
    dhcp_subnets: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemDhcpSubnetsItem"]
    ] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipfix_exporters: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemIpfixExportersItem"]
    ] = UNSET
    name: Union[Unset, str] = UNSET
    nat_ruleset: Union[Unset, str] = UNSET
    networks: Union[Unset, list[str]] = UNSET
    ospfv_2_process: Union[
        Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process"
    ] = UNSET
    ospfv_3_process: Union[
        Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process"
    ] = UNSET
    overlay_filters: Union[
        Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters"
    ] = UNSET
    routable: Union[Unset, str] = UNSET
    route_distinguisher: Union[Unset, str] = UNSET
    static_routes: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemStaticRoutesItem"]
    ] = UNSET
    syslog_targets: Union[
        Unset, list["PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemSyslogTargetsItem"]
    ] = UNSET
    traffic_ruleset: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_aggregations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_aggregations, Unset):
            bgp_aggregations = []
            for bgp_aggregations_item_data in self.bgp_aggregations:
                bgp_aggregations_item = bgp_aggregations_item_data.to_dict()
                bgp_aggregations.append(bgp_aggregations_item)

        bgp_multipath: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_multipath, Unset):
            bgp_multipath = self.bgp_multipath.to_dict()

        bgp_neighbors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_neighbors, Unset):
            bgp_neighbors = []
            for bgp_neighbors_item_data in self.bgp_neighbors:
                bgp_neighbors_item = bgp_neighbors_item_data.to_dict()
                bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistributions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_redistributions, Unset):
            bgp_redistributions = self.bgp_redistributions.to_dict()

        description = self.description

        dhcp_subnets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dhcp_subnets, Unset):
            dhcp_subnets = []
            for dhcp_subnets_item_data in self.dhcp_subnets:
                dhcp_subnets_item = dhcp_subnets_item_data.to_dict()
                dhcp_subnets.append(dhcp_subnets_item)

        enterprise_id = self.enterprise_id

        function = self.function

        id = self.id

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        name = self.name

        nat_ruleset = self.nat_ruleset

        networks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        ospfv_2_process: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ospfv_2_process, Unset):
            ospfv_2_process = self.ospfv_2_process.to_dict()

        ospfv_3_process: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ospfv_3_process, Unset):
            ospfv_3_process = self.ospfv_3_process.to_dict()

        overlay_filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.overlay_filters, Unset):
            overlay_filters = self.overlay_filters.to_dict()

        routable = self.routable

        route_distinguisher = self.route_distinguisher

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

        traffic_ruleset = self.traffic_ruleset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_aggregations is not UNSET:
            field_dict["bgpAggregations"] = bgp_aggregations
        if bgp_multipath is not UNSET:
            field_dict["bgpMultipath"] = bgp_multipath
        if bgp_neighbors is not UNSET:
            field_dict["bgpNeighbors"] = bgp_neighbors
        if bgp_redistributions is not UNSET:
            field_dict["bgpRedistributions"] = bgp_redistributions
        if description is not UNSET:
            field_dict["description"] = description
        if dhcp_subnets is not UNSET:
            field_dict["dhcpSubnets"] = dhcp_subnets
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if function is not UNSET:
            field_dict["function"] = function
        if id is not UNSET:
            field_dict["id"] = id
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
        if name is not UNSET:
            field_dict["name"] = name
        if nat_ruleset is not UNSET:
            field_dict["natRuleset"] = nat_ruleset
        if networks is not UNSET:
            field_dict["networks"] = networks
        if ospfv_2_process is not UNSET:
            field_dict["ospfv2Process"] = ospfv_2_process
        if ospfv_3_process is not UNSET:
            field_dict["ospfv3Process"] = ospfv_3_process
        if overlay_filters is not UNSET:
            field_dict["overlayFilters"] = overlay_filters
        if routable is not UNSET:
            field_dict["routable"] = routable
        if route_distinguisher is not UNSET:
            field_dict["routeDistinguisher"] = route_distinguisher
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes
        if syslog_targets is not UNSET:
            field_dict["syslogTargets"] = syslog_targets
        if traffic_ruleset is not UNSET:
            field_dict["trafficRuleset"] = traffic_ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_aggregations_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpAggregationsItem,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_multipath import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_neighbors_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpNeighborsItem,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_bgp_redistributions import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_dhcp_subnets_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemDhcpSubnetsItem,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ipfix_exporters_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemIpfixExportersItem,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ospfv_2_process import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_ospfv_3_process import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_overlay_filters import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_static_routes_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemStaticRoutesItem,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item_syslog_targets_item import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemSyslogTargetsItem,
        )

        d = src_dict.copy()
        bgp_aggregations = []
        _bgp_aggregations = d.pop("bgpAggregations", UNSET)
        for bgp_aggregations_item_data in _bgp_aggregations or []:
            bgp_aggregations_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpAggregationsItem.from_dict(
                    bgp_aggregations_item_data
                )
            )

            bgp_aggregations.append(bgp_aggregations_item)

        _bgp_multipath = d.pop("bgpMultipath", UNSET)
        bgp_multipath: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath]
        if isinstance(_bgp_multipath, Unset):
            bgp_multipath = UNSET
        else:
            bgp_multipath = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpMultipath.from_dict(
                _bgp_multipath
            )

        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgpNeighbors", UNSET)
        for bgp_neighbors_item_data in _bgp_neighbors or []:
            bgp_neighbors_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpNeighborsItem.from_dict(
                    bgp_neighbors_item_data
                )
            )

            bgp_neighbors.append(bgp_neighbors_item)

        _bgp_redistributions = d.pop("bgpRedistributions", UNSET)
        bgp_redistributions: Union[
            Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions
        ]
        if isinstance(_bgp_redistributions, Unset):
            bgp_redistributions = UNSET
        else:
            bgp_redistributions = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemBgpRedistributions.from_dict(
                    _bgp_redistributions
                )
            )

        description = d.pop("description", UNSET)

        dhcp_subnets = []
        _dhcp_subnets = d.pop("dhcpSubnets", UNSET)
        for dhcp_subnets_item_data in _dhcp_subnets or []:
            dhcp_subnets_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemDhcpSubnetsItem.from_dict(
                    dhcp_subnets_item_data
                )
            )

            dhcp_subnets.append(dhcp_subnets_item)

        enterprise_id = d.pop("enterpriseId", UNSET)

        function = d.pop("function", UNSET)

        id = d.pop("id", UNSET)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemIpfixExportersItem.from_dict(
                    ipfix_exporters_item_data
                )
            )

            ipfix_exporters.append(ipfix_exporters_item)

        name = d.pop("name", UNSET)

        nat_ruleset = d.pop("natRuleset", UNSET)

        networks = cast(list[str], d.pop("networks", UNSET))

        _ospfv_2_process = d.pop("ospfv2Process", UNSET)
        ospfv_2_process: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process]
        if isinstance(_ospfv_2_process, Unset):
            ospfv_2_process = UNSET
        else:
            ospfv_2_process = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv2Process.from_dict(
                    _ospfv_2_process
                )
            )

        _ospfv_3_process = d.pop("ospfv3Process", UNSET)
        ospfv_3_process: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process]
        if isinstance(_ospfv_3_process, Unset):
            ospfv_3_process = UNSET
        else:
            ospfv_3_process = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOspfv3Process.from_dict(
                    _ospfv_3_process
                )
            )

        _overlay_filters = d.pop("overlayFilters", UNSET)
        overlay_filters: Union[
            Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters
        ]
        if isinstance(_overlay_filters, Unset):
            overlay_filters = UNSET
        else:
            overlay_filters = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemOverlayFilters.from_dict(
                    _overlay_filters
                )
            )

        routable = d.pop("routable", UNSET)

        route_distinguisher = d.pop("routeDistinguisher", UNSET)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemStaticRoutesItem.from_dict(
                    static_routes_item_data
                )
            )

            static_routes.append(static_routes_item)

        syslog_targets = []
        _syslog_targets = d.pop("syslogTargets", UNSET)
        for syslog_targets_item_data in _syslog_targets or []:
            syslog_targets_item = (
                PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemSegmentsItemSyslogTargetsItem.from_dict(
                    syslog_targets_item_data
                )
            )

            syslog_targets.append(syslog_targets_item)

        traffic_ruleset = d.pop("trafficRuleset", UNSET)

        post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item = cls(
            bgp_aggregations=bgp_aggregations,
            bgp_multipath=bgp_multipath,
            bgp_neighbors=bgp_neighbors,
            bgp_redistributions=bgp_redistributions,
            description=description,
            dhcp_subnets=dhcp_subnets,
            enterprise_id=enterprise_id,
            function=function,
            id=id,
            ipfix_exporters=ipfix_exporters,
            name=name,
            nat_ruleset=nat_ruleset,
            networks=networks,
            ospfv_2_process=ospfv_2_process,
            ospfv_3_process=ospfv_3_process,
            overlay_filters=overlay_filters,
            routable=routable,
            route_distinguisher=route_distinguisher,
            static_routes=static_routes,
            syslog_targets=syslog_targets,
            traffic_ruleset=traffic_ruleset,
        )

        post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item.additional_properties = d
        return post_v1_extranets_resolve_policy_target_response_200_devices_item_segments_item

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
