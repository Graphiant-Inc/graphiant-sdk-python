from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_topology_response_200_network_topology_item import (
        PostV1FlowsTopologyResponse200NetworkTopologyItem,
    )


T = TypeVar("T", bound="PostV1FlowsTopologyResponse200")


@_attrs_define
class PostV1FlowsTopologyResponse200:
    """
    Attributes:
        network_topology (Union[Unset, list['PostV1FlowsTopologyResponse200NetworkTopologyItem']]):
    """

    network_topology: Union[Unset, list["PostV1FlowsTopologyResponse200NetworkTopologyItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_topology: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.network_topology, Unset):
            network_topology = []
            for network_topology_item_data in self.network_topology:
                network_topology_item = network_topology_item_data.to_dict()
                network_topology.append(network_topology_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_topology is not UNSET:
            field_dict["networkTopology"] = network_topology

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_topology_response_200_network_topology_item import (
            PostV1FlowsTopologyResponse200NetworkTopologyItem,
        )

        d = src_dict.copy()
        network_topology = []
        _network_topology = d.pop("networkTopology", UNSET)
        for network_topology_item_data in _network_topology or []:
            network_topology_item = PostV1FlowsTopologyResponse200NetworkTopologyItem.from_dict(
                network_topology_item_data
            )

            network_topology.append(network_topology_item)

        post_v1_flows_topology_response_200 = cls(
            network_topology=network_topology,
        )

        post_v1_flows_topology_response_200.additional_properties = d
        return post_v1_flows_topology_response_200

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
