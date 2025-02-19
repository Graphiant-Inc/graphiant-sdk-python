from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_response_200_topology_edges_item_performance_item import (
        PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItem:
    """
    Attributes:
        destination_node_id (Union[Unset, str]):  Example: TYPE_STRING.
        performance (Union[Unset, list['PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem']]):
        source_node_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    destination_node_id: Union[Unset, str] = UNSET
    performance: Union[Unset, list["PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem"]] = (
        UNSET
    )
    source_node_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_node_id = self.destination_node_id

        performance: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.performance, Unset):
            performance = []
            for performance_item_data in self.performance:
                performance_item = performance_item_data.to_dict()
                performance.append(performance_item)

        source_node_id = self.source_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_node_id is not UNSET:
            field_dict["destinationNodeId"] = destination_node_id
        if performance is not UNSET:
            field_dict["performance"] = performance
        if source_node_id is not UNSET:
            field_dict["sourceNodeId"] = source_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_response_200_topology_edges_item_performance_item import (
            PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem,
        )

        d = src_dict.copy()
        destination_node_id = d.pop("destinationNodeId", UNSET)

        performance = []
        _performance = d.pop("performance", UNSET)
        for performance_item_data in _performance or []:
            performance_item = PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem.from_dict(
                performance_item_data
            )

            performance.append(performance_item)

        source_node_id = d.pop("sourceNodeId", UNSET)

        post_v2_assurance_topology_overview_response_200_topology_edges_item = cls(
            destination_node_id=destination_node_id,
            performance=performance,
            source_node_id=source_node_id,
        )

        post_v2_assurance_topology_overview_response_200_topology_edges_item.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology_edges_item

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
