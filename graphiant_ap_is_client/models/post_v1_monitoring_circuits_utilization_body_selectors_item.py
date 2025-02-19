from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MonitoringCircuitsUtilizationBodySelectorsItem")


@_attrs_define
class PostV1MonitoringCircuitsUtilizationBodySelectorsItem:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    circuit_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        post_v1_monitoring_circuits_utilization_body_selectors_item = cls(
            circuit_name=circuit_name,
        )

        post_v1_monitoring_circuits_utilization_body_selectors_item.additional_properties = d
        return post_v1_monitoring_circuits_utilization_body_selectors_item

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
