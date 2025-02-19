from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_response_200_topology_edges_item import (
        PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem,
    )
    from ..models.post_v2_assurance_topology_overview_response_200_topology_nodes_item import (
        PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem,
    )
    from ..models.post_v2_assurance_topology_overview_response_200_topology_paths_item import (
        PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200Topology")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200Topology:
    """
    Attributes:
        edges (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem']]):
        nodes (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem']]):
        paths (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem']]):
    """

    edges: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem"]] = UNSET
    nodes: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem"]] = UNSET
    paths: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        paths: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()
                paths.append(paths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_response_200_topology_edges_item import (
            PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem,
        )
        from ..models.post_v2_assurance_topology_overview_response_200_topology_nodes_item import (
            PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem,
        )
        from ..models.post_v2_assurance_topology_overview_response_200_topology_paths_item import (
            PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem,
        )

        d = src_dict.copy()
        edges = []
        _edges = d.pop("edges", UNSET)
        for edges_item_data in _edges or []:
            edges_item = PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        paths = []
        _paths = d.pop("paths", UNSET)
        for paths_item_data in _paths or []:
            paths_item = PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem.from_dict(paths_item_data)

            paths.append(paths_item)

        post_v2_assurance_topology_overview_response_200_topology = cls(
            edges=edges,
            nodes=nodes,
            paths=paths,
        )

        post_v2_assurance_topology_overview_response_200_topology.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology

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
