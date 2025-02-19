from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuitsummary_circuit_name_response_200_circuit_summary import (
        PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsummaryCircuitNameResponse200")


@_attrs_define
class PostV2MonitoringCircuitsummaryCircuitNameResponse200:
    """
    Attributes:
        circuit_summary (Union[Unset, PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary]):
    """

    circuit_summary: Union[Unset, "PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.circuit_summary, Unset):
            circuit_summary = self.circuit_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_summary is not UNSET:
            field_dict["circuitSummary"] = circuit_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuitsummary_circuit_name_response_200_circuit_summary import (
            PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary,
        )

        d = src_dict.copy()
        _circuit_summary = d.pop("circuitSummary", UNSET)
        circuit_summary: Union[Unset, PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary]
        if isinstance(_circuit_summary, Unset):
            circuit_summary = UNSET
        else:
            circuit_summary = PostV2MonitoringCircuitsummaryCircuitNameResponse200CircuitSummary.from_dict(
                _circuit_summary
            )

        post_v2_monitoring_circuitsummary_circuit_name_response_200 = cls(
            circuit_summary=circuit_summary,
        )

        post_v2_monitoring_circuitsummary_circuit_name_response_200.additional_properties = d
        return post_v2_monitoring_circuitsummary_circuit_name_response_200

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
