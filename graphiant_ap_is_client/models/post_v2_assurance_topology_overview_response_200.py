from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_response_200_topology import (
        PostV2AssuranceTopologyOverviewResponse200Topology,
    )
    from ..models.post_v2_assurance_topology_overview_response_200_topology_change_ts_item import (
        PostV2AssuranceTopologyOverviewResponse200TopologyChangeTsItem,
    )
    from ..models.post_v2_assurance_topology_overview_response_200_traffic_regions_item import (
        PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200:
    """
    Attributes:
        num_applications (Union[Unset, str]):  Example: TYPE_INT32.
        num_flows (Union[Unset, str]):  Example: TYPE_INT32.
        topology (Union[Unset, PostV2AssuranceTopologyOverviewResponse200Topology]):
        topology_change_ts (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TopologyChangeTsItem']]):
        traffic_regions (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem']]):
    """

    num_applications: Union[Unset, str] = UNSET
    num_flows: Union[Unset, str] = UNSET
    topology: Union[Unset, "PostV2AssuranceTopologyOverviewResponse200Topology"] = UNSET
    topology_change_ts: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TopologyChangeTsItem"]] = UNSET
    traffic_regions: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_applications = self.num_applications

        num_flows = self.num_flows

        topology: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.to_dict()

        topology_change_ts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.topology_change_ts, Unset):
            topology_change_ts = []
            for topology_change_ts_item_data in self.topology_change_ts:
                topology_change_ts_item = topology_change_ts_item_data.to_dict()
                topology_change_ts.append(topology_change_ts_item)

        traffic_regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_regions, Unset):
            traffic_regions = []
            for traffic_regions_item_data in self.traffic_regions:
                traffic_regions_item = traffic_regions_item_data.to_dict()
                traffic_regions.append(traffic_regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_applications is not UNSET:
            field_dict["numApplications"] = num_applications
        if num_flows is not UNSET:
            field_dict["numFlows"] = num_flows
        if topology is not UNSET:
            field_dict["topology"] = topology
        if topology_change_ts is not UNSET:
            field_dict["topologyChangeTs"] = topology_change_ts
        if traffic_regions is not UNSET:
            field_dict["trafficRegions"] = traffic_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_response_200_topology import (
            PostV2AssuranceTopologyOverviewResponse200Topology,
        )
        from ..models.post_v2_assurance_topology_overview_response_200_topology_change_ts_item import (
            PostV2AssuranceTopologyOverviewResponse200TopologyChangeTsItem,
        )
        from ..models.post_v2_assurance_topology_overview_response_200_traffic_regions_item import (
            PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem,
        )

        d = src_dict.copy()
        num_applications = d.pop("numApplications", UNSET)

        num_flows = d.pop("numFlows", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, PostV2AssuranceTopologyOverviewResponse200Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = PostV2AssuranceTopologyOverviewResponse200Topology.from_dict(_topology)

        topology_change_ts = []
        _topology_change_ts = d.pop("topologyChangeTs", UNSET)
        for topology_change_ts_item_data in _topology_change_ts or []:
            topology_change_ts_item = PostV2AssuranceTopologyOverviewResponse200TopologyChangeTsItem.from_dict(
                topology_change_ts_item_data
            )

            topology_change_ts.append(topology_change_ts_item)

        traffic_regions = []
        _traffic_regions = d.pop("trafficRegions", UNSET)
        for traffic_regions_item_data in _traffic_regions or []:
            traffic_regions_item = PostV2AssuranceTopologyOverviewResponse200TrafficRegionsItem.from_dict(
                traffic_regions_item_data
            )

            traffic_regions.append(traffic_regions_item)

        post_v2_assurance_topology_overview_response_200 = cls(
            num_applications=num_applications,
            num_flows=num_flows,
            topology=topology,
            topology_change_ts=topology_change_ts,
            traffic_regions=traffic_regions,
        )

        post_v2_assurance_topology_overview_response_200.additional_properties = d
        return post_v2_assurance_topology_overview_response_200

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
