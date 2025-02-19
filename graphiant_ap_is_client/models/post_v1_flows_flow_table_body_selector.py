from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1FlowsFlowTableBodySelector")


@_attrs_define
class PostV1FlowsFlowTableBodySelector:
    """
    Attributes:
        circuit_name (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        sla_class (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
    """

    circuit_name: Union[Unset, list[str]] = UNSET
    sla_class: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.circuit_name, Unset):
            circuit_name = self.circuit_name

        sla_class: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sla_class, Unset):
            sla_class = self.sla_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = cast(list[str], d.pop("circuitName", UNSET))

        sla_class = cast(list[str], d.pop("slaClass", UNSET))

        post_v1_flows_flow_table_body_selector = cls(
            circuit_name=circuit_name,
            sla_class=sla_class,
        )

        post_v1_flows_flow_table_body_selector.additional_properties = d
        return post_v1_flows_flow_table_body_selector

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
