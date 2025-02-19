from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TopologyNodesItemLocation:
    """
    Attributes:
        lat (Union[Unset, str]):  Example: TYPE_FLOAT.
        long (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    lat: Union[Unset, str] = UNSET
    long: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        long = self.long

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat", UNSET)

        long = d.pop("long", UNSET)

        post_v2_assurance_topology_overview_response_200_topology_nodes_item_location = cls(
            lat=lat,
            long=long,
        )

        post_v2_assurance_topology_overview_response_200_topology_nodes_item_location.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology_nodes_item_location

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
