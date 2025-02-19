from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_added_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesAddedItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_nodes_added_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesAddedItem,
    )
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_nodes_deleted_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesDeletedItem,
    )


T = TypeVar("T", bound="PostV1FlowsTopologyResponse200NetworkTopologyItemDelta")


@_attrs_define
class PostV1FlowsTopologyResponse200NetworkTopologyItemDelta:
    """
    Attributes:
        edges_added (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesAddedItem']]):
        edges_deleted (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem']]):
        nodes_added (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesAddedItem']]):
        nodes_deleted (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesDeletedItem']]):
    """

    edges_added: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesAddedItem"]] = UNSET
    edges_deleted: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem"]] = UNSET
    nodes_added: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesAddedItem"]] = UNSET
    nodes_deleted: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesDeletedItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edges_added: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges_added, Unset):
            edges_added = []
            for edges_added_item_data in self.edges_added:
                edges_added_item = edges_added_item_data.to_dict()
                edges_added.append(edges_added_item)

        edges_deleted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges_deleted, Unset):
            edges_deleted = []
            for edges_deleted_item_data in self.edges_deleted:
                edges_deleted_item = edges_deleted_item_data.to_dict()
                edges_deleted.append(edges_deleted_item)

        nodes_added: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes_added, Unset):
            nodes_added = []
            for nodes_added_item_data in self.nodes_added:
                nodes_added_item = nodes_added_item_data.to_dict()
                nodes_added.append(nodes_added_item)

        nodes_deleted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes_deleted, Unset):
            nodes_deleted = []
            for nodes_deleted_item_data in self.nodes_deleted:
                nodes_deleted_item = nodes_deleted_item_data.to_dict()
                nodes_deleted.append(nodes_deleted_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges_added is not UNSET:
            field_dict["edgesAdded"] = edges_added
        if edges_deleted is not UNSET:
            field_dict["edgesDeleted"] = edges_deleted
        if nodes_added is not UNSET:
            field_dict["nodesAdded"] = nodes_added
        if nodes_deleted is not UNSET:
            field_dict["nodesDeleted"] = nodes_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_added_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesAddedItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_nodes_added_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesAddedItem,
        )
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_nodes_deleted_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesDeletedItem,
        )

        d = src_dict.copy()
        edges_added = []
        _edges_added = d.pop("edgesAdded", UNSET)
        for edges_added_item_data in _edges_added or []:
            edges_added_item = PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesAddedItem.from_dict(
                edges_added_item_data
            )

            edges_added.append(edges_added_item)

        edges_deleted = []
        _edges_deleted = d.pop("edgesDeleted", UNSET)
        for edges_deleted_item_data in _edges_deleted or []:
            edges_deleted_item = PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem.from_dict(
                edges_deleted_item_data
            )

            edges_deleted.append(edges_deleted_item)

        nodes_added = []
        _nodes_added = d.pop("nodesAdded", UNSET)
        for nodes_added_item_data in _nodes_added or []:
            nodes_added_item = PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesAddedItem.from_dict(
                nodes_added_item_data
            )

            nodes_added.append(nodes_added_item)

        nodes_deleted = []
        _nodes_deleted = d.pop("nodesDeleted", UNSET)
        for nodes_deleted_item_data in _nodes_deleted or []:
            nodes_deleted_item = PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaNodesDeletedItem.from_dict(
                nodes_deleted_item_data
            )

            nodes_deleted.append(nodes_deleted_item)

        post_v1_flows_topology_response_200_network_topology_item_delta = cls(
            edges_added=edges_added,
            edges_deleted=edges_deleted,
            nodes_added=nodes_added,
            nodes_deleted=nodes_deleted,
        )

        post_v1_flows_topology_response_200_network_topology_item_delta.additional_properties = d
        return post_v1_flows_topology_response_200_network_topology_item_delta

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
