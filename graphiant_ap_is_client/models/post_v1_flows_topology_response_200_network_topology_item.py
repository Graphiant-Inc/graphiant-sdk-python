from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_topology_response_200_network_topology_item_circuit_status_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemCircuitStatusItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDelta,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_edges_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemEdgesItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_nodes_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemNodesItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_time_window import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow,
    )


T = TypeVar("T", bound="PostV1FlowsTopologyResponse200NetworkTopologyItem")


@_attrs_define
class PostV1FlowsTopologyResponse200NetworkTopologyItem:
    """
    Attributes:
        circuit_status (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemCircuitStatusItem']]):
        delta (Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemDelta]):
        edges (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemEdgesItem']]):
        flows (Union[Unset, str]):  Example: TYPE_UINT32.
        nodes (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemNodesItem']]):
        time_window (Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow]):
    """

    circuit_status: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemCircuitStatusItem"]] = UNSET
    delta: Union[Unset, "PostV1FlowsTopologyResponse200NetworkTopologyItemDelta"] = UNSET
    edges: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemEdgesItem"]] = UNSET
    flows: Union[Unset, str] = UNSET
    nodes: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemNodesItem"]] = UNSET
    time_window: Union[Unset, "PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_status, Unset):
            circuit_status = []
            for circuit_status_item_data in self.circuit_status:
                circuit_status_item = circuit_status_item_data.to_dict()
                circuit_status.append(circuit_status_item)

        delta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.delta, Unset):
            delta = self.delta.to_dict()

        edges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        flows = self.flows

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_status is not UNSET:
            field_dict["circuitStatus"] = circuit_status
        if delta is not UNSET:
            field_dict["delta"] = delta
        if edges is not UNSET:
            field_dict["edges"] = edges
        if flows is not UNSET:
            field_dict["flows"] = flows
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_topology_response_200_network_topology_item_circuit_status_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemCircuitStatusItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDelta,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_edges_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemEdgesItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_nodes_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemNodesItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_time_window import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow,
        )

        d = src_dict.copy()
        circuit_status = []
        _circuit_status = d.pop("circuitStatus", UNSET)
        for circuit_status_item_data in _circuit_status or []:
            circuit_status_item = PostV1FlowsTopologyResponse200NetworkTopologyItemCircuitStatusItem.from_dict(
                circuit_status_item_data
            )

            circuit_status.append(circuit_status_item)

        _delta = d.pop("delta", UNSET)
        delta: Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemDelta]
        if isinstance(_delta, Unset):
            delta = UNSET
        else:
            delta = PostV1FlowsTopologyResponse200NetworkTopologyItemDelta.from_dict(_delta)

        edges = []
        _edges = d.pop("edges", UNSET)
        for edges_item_data in _edges or []:
            edges_item = PostV1FlowsTopologyResponse200NetworkTopologyItemEdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        flows = d.pop("flows", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = PostV1FlowsTopologyResponse200NetworkTopologyItemNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1FlowsTopologyResponse200NetworkTopologyItemTimeWindow.from_dict(_time_window)

        post_v1_flows_topology_response_200_network_topology_item = cls(
            circuit_status=circuit_status,
            delta=delta,
            edges=edges,
            flows=flows,
            nodes=nodes,
            time_window=time_window,
        )

        post_v1_flows_topology_response_200_network_topology_item.additional_properties = d
        return post_v1_flows_topology_response_200_network_topology_item

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
