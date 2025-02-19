from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_connectivity_response_200_edges_item import (
        GetV1DevicesDeviceIdConnectivityResponse200EdgesItem,
    )
    from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item import (
        GetV1DevicesDeviceIdConnectivityResponse200NodesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdConnectivityResponse200")


@_attrs_define
class GetV1DevicesDeviceIdConnectivityResponse200:
    """
    Attributes:
        edges (Union[Unset, list['GetV1DevicesDeviceIdConnectivityResponse200EdgesItem']]):
        nodes (Union[Unset, list['GetV1DevicesDeviceIdConnectivityResponse200NodesItem']]):
    """

    edges: Union[Unset, list["GetV1DevicesDeviceIdConnectivityResponse200EdgesItem"]] = UNSET
    nodes: Union[Unset, list["GetV1DevicesDeviceIdConnectivityResponse200NodesItem"]] = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_connectivity_response_200_edges_item import (
            GetV1DevicesDeviceIdConnectivityResponse200EdgesItem,
        )
        from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item import (
            GetV1DevicesDeviceIdConnectivityResponse200NodesItem,
        )

        d = src_dict.copy()
        edges = []
        _edges = d.pop("edges", UNSET)
        for edges_item_data in _edges or []:
            edges_item = GetV1DevicesDeviceIdConnectivityResponse200EdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = GetV1DevicesDeviceIdConnectivityResponse200NodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        get_v1_devices_device_id_connectivity_response_200 = cls(
            edges=edges,
            nodes=nodes,
        )

        get_v1_devices_device_id_connectivity_response_200.additional_properties = d
        return get_v1_devices_device_id_connectivity_response_200

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
