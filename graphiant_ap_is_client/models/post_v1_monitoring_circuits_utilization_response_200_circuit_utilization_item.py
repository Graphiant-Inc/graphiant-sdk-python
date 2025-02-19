from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item_queue_utilization_item import (
        PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItemQueueUtilizationItem,
    )


T = TypeVar("T", bound="PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem")


@_attrs_define
class PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem:
    """
    Attributes:
        config_link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        queue_utilization (Union[Unset,
            list['PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItemQueueUtilizationItem']]):
    """

    config_link_up_speed_mbps: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    queue_utilization: Union[
        Unset, list["PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItemQueueUtilizationItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_link_up_speed_mbps = self.config_link_up_speed_mbps

        name = self.name

        queue_utilization: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.queue_utilization, Unset):
            queue_utilization = []
            for queue_utilization_item_data in self.queue_utilization:
                queue_utilization_item = queue_utilization_item_data.to_dict()
                queue_utilization.append(queue_utilization_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_link_up_speed_mbps is not UNSET:
            field_dict["configLinkUpSpeedMbps"] = config_link_up_speed_mbps
        if name is not UNSET:
            field_dict["name"] = name
        if queue_utilization is not UNSET:
            field_dict["queueUtilization"] = queue_utilization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item_queue_utilization_item import (
            PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItemQueueUtilizationItem,
        )

        d = src_dict.copy()
        config_link_up_speed_mbps = d.pop("configLinkUpSpeedMbps", UNSET)

        name = d.pop("name", UNSET)

        queue_utilization = []
        _queue_utilization = d.pop("queueUtilization", UNSET)
        for queue_utilization_item_data in _queue_utilization or []:
            queue_utilization_item = (
                PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItemQueueUtilizationItem.from_dict(
                    queue_utilization_item_data
                )
            )

            queue_utilization.append(queue_utilization_item)

        post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item = cls(
            config_link_up_speed_mbps=config_link_up_speed_mbps,
            name=name,
            queue_utilization=queue_utilization,
        )

        post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item.additional_properties = d
        return post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item

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
