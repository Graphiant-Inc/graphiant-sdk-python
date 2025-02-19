from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_topology_response_200_nodes_item_circuit_info_item import (
        PostV2DeviceDeviceIdTopologyResponse200NodesItemCircuitInfoItem,
    )
    from ..models.post_v2_device_device_id_topology_response_200_nodes_item_connections_item import (
        PostV2DeviceDeviceIdTopologyResponse200NodesItemConnectionsItem,
    )
    from ..models.post_v2_device_device_id_topology_response_200_nodes_item_node_info import (
        PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdTopologyResponse200NodesItem")


@_attrs_define
class PostV2DeviceDeviceIdTopologyResponse200NodesItem:
    """
    Attributes:
        circuit_info (Union[Unset, list['PostV2DeviceDeviceIdTopologyResponse200NodesItemCircuitInfoItem']]):
        connections (Union[Unset, list['PostV2DeviceDeviceIdTopologyResponse200NodesItemConnectionsItem']]):
        id (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        node_info (Union[Unset, PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo]):
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    circuit_info: Union[Unset, list["PostV2DeviceDeviceIdTopologyResponse200NodesItemCircuitInfoItem"]] = UNSET
    connections: Union[Unset, list["PostV2DeviceDeviceIdTopologyResponse200NodesItemConnectionsItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_info: Union[Unset, "PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo"] = UNSET
    quality: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_info, Unset):
            circuit_info = []
            for circuit_info_item_data in self.circuit_info:
                circuit_info_item = circuit_info_item_data.to_dict()
                circuit_info.append(circuit_info_item)

        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        id = self.id

        name = self.name

        node_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.node_info, Unset):
            node_info = self.node_info.to_dict()

        quality = self.quality

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_info is not UNSET:
            field_dict["circuitInfo"] = circuit_info
        if connections is not UNSET:
            field_dict["connections"] = connections
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if node_info is not UNSET:
            field_dict["nodeInfo"] = node_info
        if quality is not UNSET:
            field_dict["quality"] = quality
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_topology_response_200_nodes_item_circuit_info_item import (
            PostV2DeviceDeviceIdTopologyResponse200NodesItemCircuitInfoItem,
        )
        from ..models.post_v2_device_device_id_topology_response_200_nodes_item_connections_item import (
            PostV2DeviceDeviceIdTopologyResponse200NodesItemConnectionsItem,
        )
        from ..models.post_v2_device_device_id_topology_response_200_nodes_item_node_info import (
            PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo,
        )

        d = src_dict.copy()
        circuit_info = []
        _circuit_info = d.pop("circuitInfo", UNSET)
        for circuit_info_item_data in _circuit_info or []:
            circuit_info_item = PostV2DeviceDeviceIdTopologyResponse200NodesItemCircuitInfoItem.from_dict(
                circuit_info_item_data
            )

            circuit_info.append(circuit_info_item)

        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = PostV2DeviceDeviceIdTopologyResponse200NodesItemConnectionsItem.from_dict(
                connections_item_data
            )

            connections.append(connections_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _node_info = d.pop("nodeInfo", UNSET)
        node_info: Union[Unset, PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo]
        if isinstance(_node_info, Unset):
            node_info = UNSET
        else:
            node_info = PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo.from_dict(_node_info)

        quality = d.pop("quality", UNSET)

        type_ = d.pop("type", UNSET)

        post_v2_device_device_id_topology_response_200_nodes_item = cls(
            circuit_info=circuit_info,
            connections=connections,
            id=id,
            name=name,
            node_info=node_info,
            quality=quality,
            type_=type_,
        )

        post_v2_device_device_id_topology_response_200_nodes_item.additional_properties = d
        return post_v2_device_device_id_topology_response_200_nodes_item

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
