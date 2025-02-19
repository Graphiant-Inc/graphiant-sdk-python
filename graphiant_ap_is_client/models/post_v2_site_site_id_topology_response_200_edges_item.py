from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_site_site_id_topology_response_200_edges_item_circuits_info_item import (
        PostV2SiteSiteIdTopologyResponse200EdgesItemCircuitsInfoItem,
    )
    from ..models.post_v2_site_site_id_topology_response_200_edges_item_connections_item import (
        PostV2SiteSiteIdTopologyResponse200EdgesItemConnectionsItem,
    )


T = TypeVar("T", bound="PostV2SiteSiteIdTopologyResponse200EdgesItem")


@_attrs_define
class PostV2SiteSiteIdTopologyResponse200EdgesItem:
    """
    Attributes:
        a (Union[Unset, str]):  Example: TYPE_UINT32.
        b (Union[Unset, str]):  Example: TYPE_UINT32.
        circuits_info (Union[Unset, list['PostV2SiteSiteIdTopologyResponse200EdgesItemCircuitsInfoItem']]):
        connections (Union[Unset, list['PostV2SiteSiteIdTopologyResponse200EdgesItemConnectionsItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    a: Union[Unset, str] = UNSET
    b: Union[Unset, str] = UNSET
    circuits_info: Union[Unset, list["PostV2SiteSiteIdTopologyResponse200EdgesItemCircuitsInfoItem"]] = UNSET
    connections: Union[Unset, list["PostV2SiteSiteIdTopologyResponse200EdgesItemConnectionsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    quality: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a = self.a

        b = self.b

        circuits_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits_info, Unset):
            circuits_info = []
            for circuits_info_item_data in self.circuits_info:
                circuits_info_item = circuits_info_item_data.to_dict()
                circuits_info.append(circuits_info_item)

        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        name = self.name

        quality = self.quality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if circuits_info is not UNSET:
            field_dict["circuitsInfo"] = circuits_info
        if connections is not UNSET:
            field_dict["connections"] = connections
        if name is not UNSET:
            field_dict["name"] = name
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_site_site_id_topology_response_200_edges_item_circuits_info_item import (
            PostV2SiteSiteIdTopologyResponse200EdgesItemCircuitsInfoItem,
        )
        from ..models.post_v2_site_site_id_topology_response_200_edges_item_connections_item import (
            PostV2SiteSiteIdTopologyResponse200EdgesItemConnectionsItem,
        )

        d = src_dict.copy()
        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        circuits_info = []
        _circuits_info = d.pop("circuitsInfo", UNSET)
        for circuits_info_item_data in _circuits_info or []:
            circuits_info_item = PostV2SiteSiteIdTopologyResponse200EdgesItemCircuitsInfoItem.from_dict(
                circuits_info_item_data
            )

            circuits_info.append(circuits_info_item)

        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = PostV2SiteSiteIdTopologyResponse200EdgesItemConnectionsItem.from_dict(
                connections_item_data
            )

            connections.append(connections_item)

        name = d.pop("name", UNSET)

        quality = d.pop("quality", UNSET)

        post_v2_site_site_id_topology_response_200_edges_item = cls(
            a=a,
            b=b,
            circuits_info=circuits_info,
            connections=connections,
            name=name,
            quality=quality,
        )

        post_v2_site_site_id_topology_response_200_edges_item.additional_properties = d
        return post_v2_site_site_id_topology_response_200_edges_item

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
