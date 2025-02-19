from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringCircuitsVisualizationBodySelectorsItem")


@_attrs_define
class PostV2MonitoringCircuitsVisualizationBodySelectorsItem:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        core_location (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    circuit_name: Union[Unset, str] = UNSET
    core_location: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        core_location = self.core_location

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if core_location is not UNSET:
            field_dict["coreLocation"] = core_location
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        core_location = d.pop("coreLocation", UNSET)

        type_ = d.pop("type", UNSET)

        post_v2_monitoring_circuits_visualization_body_selectors_item = cls(
            circuit_name=circuit_name,
            core_location=core_location,
            type_=type_,
        )

        post_v2_monitoring_circuits_visualization_body_selectors_item.additional_properties = d
        return post_v2_monitoring_circuits_visualization_body_selectors_item

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
