from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_summary_response_200_circuit_summaries_item import (
        PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsSummaryResponse200")


@_attrs_define
class PostV2MonitoringCircuitsSummaryResponse200:
    """
    Attributes:
        circuit_summaries (Union[Unset, list['PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem']]):
    """

    circuit_summaries: Union[Unset, list["PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_summaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_summaries, Unset):
            circuit_summaries = []
            for circuit_summaries_item_data in self.circuit_summaries:
                circuit_summaries_item = circuit_summaries_item_data.to_dict()
                circuit_summaries.append(circuit_summaries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_summaries is not UNSET:
            field_dict["circuitSummaries"] = circuit_summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_summary_response_200_circuit_summaries_item import (
            PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem,
        )

        d = src_dict.copy()
        circuit_summaries = []
        _circuit_summaries = d.pop("circuitSummaries", UNSET)
        for circuit_summaries_item_data in _circuit_summaries or []:
            circuit_summaries_item = PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem.from_dict(
                circuit_summaries_item_data
            )

            circuit_summaries.append(circuit_summaries_item)

        post_v2_monitoring_circuits_summary_response_200 = cls(
            circuit_summaries=circuit_summaries,
        )

        post_v2_monitoring_circuits_summary_response_200.additional_properties = d
        return post_v2_monitoring_circuits_summary_response_200

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
