from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item_connections import (
        PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections,
    )


T = TypeVar("T", bound="PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem")


@_attrs_define
class PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItem:
    """
    Attributes:
        a (Union[Unset, str]):  Example: TYPE_UINT32.
        b (Union[Unset, str]):  Example: TYPE_UINT32.
        connections (Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections]):
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    a: Union[Unset, str] = UNSET
    b: Union[Unset, str] = UNSET
    connections: Union[Unset, "PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections"] = (
        UNSET
    )
    quality: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a = self.a

        b = self.b

        connections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = self.connections.to_dict()

        quality = self.quality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if connections is not UNSET:
            field_dict["connections"] = connections
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item_connections import (
            PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections,
        )

        d = src_dict.copy()
        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        _connections = d.pop("connections", UNSET)
        connections: Union[Unset, PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections]
        if isinstance(_connections, Unset):
            connections = UNSET
        else:
            connections = PostV1FlowsTopologyResponse200NetworkTopologyItemDeltaEdgesDeletedItemConnections.from_dict(
                _connections
            )

        quality = d.pop("quality", UNSET)

        post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item = cls(
            a=a,
            b=b,
            connections=connections,
            quality=quality,
        )

        post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item.additional_properties = d
        return post_v1_flows_topology_response_200_network_topology_item_delta_edges_deleted_item

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
