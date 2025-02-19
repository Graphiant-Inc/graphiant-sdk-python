from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuitsummary_circuit_name_body_time_window import (
        PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsummaryCircuitNameBody")


@_attrs_define
class PostV2MonitoringCircuitsummaryCircuitNameBody:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        time_window (Union[Unset, PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow]):
    """

    circuit_name: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuitsummary_circuit_name_body_time_window import (
            PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow,
        )

        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2MonitoringCircuitsummaryCircuitNameBodyTimeWindow.from_dict(_time_window)

        post_v2_monitoring_circuitsummary_circuit_name_body = cls(
            circuit_name=circuit_name,
            time_window=time_window,
        )

        post_v2_monitoring_circuitsummary_circuit_name_body.additional_properties = d
        return post_v2_monitoring_circuitsummary_circuit_name_body

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
