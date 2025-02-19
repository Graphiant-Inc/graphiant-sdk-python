from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_response_200_topology_nodes_item_location import (
        PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TopologyNodesItem:
    """
    Attributes:
        active (Union[Unset, str]):  Example: TYPE_BOOL.
        location (Union[Unset, PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        node_id (Union[Unset, str]):  Example: TYPE_STRING.
        node_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    active: Union[Unset, str] = UNSET
    location: Union[Unset, "PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation"] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        name = self.name

        node_id = self.node_id

        node_type = self.node_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_response_200_topology_nodes_item_location import (
            PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation,
        )

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation.from_dict(_location)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        node_type = d.pop("nodeType", UNSET)

        post_v2_assurance_topology_overview_response_200_topology_nodes_item = cls(
            active=active,
            location=location,
            name=name,
            node_id=node_id,
            node_type=node_type,
        )

        post_v2_assurance_topology_overview_response_200_topology_nodes_item.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology_nodes_item

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
