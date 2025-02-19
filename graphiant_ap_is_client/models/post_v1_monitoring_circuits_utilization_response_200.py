from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item import (
        PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem,
    )


T = TypeVar("T", bound="PostV1MonitoringCircuitsUtilizationResponse200")


@_attrs_define
class PostV1MonitoringCircuitsUtilizationResponse200:
    """
    Attributes:
        circuit_utilization (Union[Unset,
            list['PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem']]):
    """

    circuit_utilization: Union[Unset, list["PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_utilization: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_utilization, Unset):
            circuit_utilization = []
            for circuit_utilization_item_data in self.circuit_utilization:
                circuit_utilization_item = circuit_utilization_item_data.to_dict()
                circuit_utilization.append(circuit_utilization_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_utilization is not UNSET:
            field_dict["circuitUtilization"] = circuit_utilization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_monitoring_circuits_utilization_response_200_circuit_utilization_item import (
            PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem,
        )

        d = src_dict.copy()
        circuit_utilization = []
        _circuit_utilization = d.pop("circuitUtilization", UNSET)
        for circuit_utilization_item_data in _circuit_utilization or []:
            circuit_utilization_item = PostV1MonitoringCircuitsUtilizationResponse200CircuitUtilizationItem.from_dict(
                circuit_utilization_item_data
            )

            circuit_utilization.append(circuit_utilization_item)

        post_v1_monitoring_circuits_utilization_response_200 = cls(
            circuit_utilization=circuit_utilization,
        )

        post_v1_monitoring_circuits_utilization_response_200.additional_properties = d
        return post_v1_monitoring_circuits_utilization_response_200

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
