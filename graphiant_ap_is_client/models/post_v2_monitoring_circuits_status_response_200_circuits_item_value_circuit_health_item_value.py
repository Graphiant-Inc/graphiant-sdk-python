from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItemValue")


@_attrs_define
class PostV2MonitoringCircuitsStatusResponse200CircuitsItemValueCircuitHealthItemValue:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        post_v2_monitoring_circuits_status_response_200_circuits_item_value_circuit_health_item_value = cls()

        post_v2_monitoring_circuits_status_response_200_circuits_item_value_circuit_health_item_value.additional_properties = d
        return post_v2_monitoring_circuits_status_response_200_circuits_item_value_circuit_health_item_value

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
