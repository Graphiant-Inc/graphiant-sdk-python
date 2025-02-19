from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_site_site_id_topology_response_200_edges_item import (
        PostV2SiteSiteIdTopologyResponse200EdgesItem,
    )
    from ..models.post_v2_site_site_id_topology_response_200_nodes_item import (
        PostV2SiteSiteIdTopologyResponse200NodesItem,
    )
    from ..models.post_v2_site_site_id_topology_response_200_snapshots_item import (
        PostV2SiteSiteIdTopologyResponse200SnapshotsItem,
    )


T = TypeVar("T", bound="PostV2SiteSiteIdTopologyResponse200")


@_attrs_define
class PostV2SiteSiteIdTopologyResponse200:
    """
    Attributes:
        edges (Union[Unset, list['PostV2SiteSiteIdTopologyResponse200EdgesItem']]):
        nodes (Union[Unset, list['PostV2SiteSiteIdTopologyResponse200NodesItem']]):
        snapshots (Union[Unset, list['PostV2SiteSiteIdTopologyResponse200SnapshotsItem']]):
    """

    edges: Union[Unset, list["PostV2SiteSiteIdTopologyResponse200EdgesItem"]] = UNSET
    nodes: Union[Unset, list["PostV2SiteSiteIdTopologyResponse200NodesItem"]] = UNSET
    snapshots: Union[Unset, list["PostV2SiteSiteIdTopologyResponse200SnapshotsItem"]] = UNSET
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

        snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_site_site_id_topology_response_200_edges_item import (
            PostV2SiteSiteIdTopologyResponse200EdgesItem,
        )
        from ..models.post_v2_site_site_id_topology_response_200_nodes_item import (
            PostV2SiteSiteIdTopologyResponse200NodesItem,
        )
        from ..models.post_v2_site_site_id_topology_response_200_snapshots_item import (
            PostV2SiteSiteIdTopologyResponse200SnapshotsItem,
        )

        d = src_dict.copy()
        edges = []
        _edges = d.pop("edges", UNSET)
        for edges_item_data in _edges or []:
            edges_item = PostV2SiteSiteIdTopologyResponse200EdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = PostV2SiteSiteIdTopologyResponse200NodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        snapshots = []
        _snapshots = d.pop("snapshots", UNSET)
        for snapshots_item_data in _snapshots or []:
            snapshots_item = PostV2SiteSiteIdTopologyResponse200SnapshotsItem.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        post_v2_site_site_id_topology_response_200 = cls(
            edges=edges,
            nodes=nodes,
            snapshots=snapshots,
        )

        post_v2_site_site_id_topology_response_200.additional_properties = d
        return post_v2_site_site_id_topology_response_200

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
