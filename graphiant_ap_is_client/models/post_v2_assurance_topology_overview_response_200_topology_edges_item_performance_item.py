from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TopologyEdgesItemPerformanceItem:
    """
    Attributes:
        jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        latency (Union[Unset, str]):  Example: TYPE_FLOAT.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    jitter: Union[Unset, str] = UNSET
    latency: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jitter = self.jitter

        latency = self.latency

        loss = self.loss

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        jitter = d.pop("jitter", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        post_v2_assurance_topology_overview_response_200_topology_edges_item_performance_item = cls(
            jitter=jitter,
            latency=latency,
            loss=loss,
        )

        post_v2_assurance_topology_overview_response_200_topology_edges_item_performance_item.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology_edges_item_performance_item

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
