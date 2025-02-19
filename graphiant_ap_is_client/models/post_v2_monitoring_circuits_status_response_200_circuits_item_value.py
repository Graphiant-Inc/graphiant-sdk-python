from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_status_response_200_circuits_item_value_circuit_health_item import (
        PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItem,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsStatusResponse200CircuitsItemValue")


@_attrs_define
class PostV2MonitoringCircuitsStatusResponse200CircuitsItemValue:
    """
    Attributes:
        circuit_health (Union[Unset,
            list['PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItem']]):
        vrfs (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    circuit_health: Union[
        Unset, list["PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItem"]
    ] = UNSET
    vrfs: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_health: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_health, Unset):
            circuit_health = []
            for circuit_health_item_data in self.circuit_health:
                circuit_health_item = circuit_health_item_data.to_dict()
                circuit_health.append(circuit_health_item)

        vrfs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vrfs, Unset):
            vrfs = self.vrfs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_health is not UNSET:
            field_dict["circuitHealth"] = circuit_health
        if vrfs is not UNSET:
            field_dict["vrfs"] = vrfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_status_response_200_circuits_item_value_circuit_health_item import (
            PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItem,
        )

        d = src_dict.copy()
        circuit_health = []
        _circuit_health = d.pop("circuitHealth", UNSET)
        for circuit_health_item_data in _circuit_health or []:
            circuit_health_item = PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItem.from_dict(
                circuit_health_item_data
            )

            circuit_health.append(circuit_health_item)

        vrfs = cast(list[str], d.pop("vrfs", UNSET))

        post_v2_monitoring_circuits_status_response_200_circuits_item_value = cls(
            circuit_health=circuit_health,
            vrfs=vrfs,
        )

        post_v2_monitoring_circuits_status_response_200_circuits_item_value.additional_properties = d
        return post_v2_monitoring_circuits_status_response_200_circuits_item_value

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
