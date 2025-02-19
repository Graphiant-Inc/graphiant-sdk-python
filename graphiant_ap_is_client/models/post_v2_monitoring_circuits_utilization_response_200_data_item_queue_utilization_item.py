from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem")


@_attrs_define
class PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem:
    """
    Attributes:
        allocated_pct (Union[Unset, str]):  Example: TYPE_UINT32.
        default_queue (Union[Unset, str]):  Example: TYPE_BOOL.
        excess_weight (Union[Unset, str]):  Example: TYPE_UINT32.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        utilization_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        utilization_pct (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    allocated_pct: Union[Unset, str] = UNSET
    default_queue: Union[Unset, str] = UNSET
    excess_weight: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    utilization_kbps: Union[Unset, str] = UNSET
    utilization_pct: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated_pct = self.allocated_pct

        default_queue = self.default_queue

        excess_weight = self.excess_weight

        sla_class = self.sla_class

        utilization_kbps = self.utilization_kbps

        utilization_pct = self.utilization_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated_pct is not UNSET:
            field_dict["allocatedPct"] = allocated_pct
        if default_queue is not UNSET:
            field_dict["defaultQueue"] = default_queue
        if excess_weight is not UNSET:
            field_dict["excessWeight"] = excess_weight
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if utilization_kbps is not UNSET:
            field_dict["utilizationKbps"] = utilization_kbps
        if utilization_pct is not UNSET:
            field_dict["utilizationPct"] = utilization_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allocated_pct = d.pop("allocatedPct", UNSET)

        default_queue = d.pop("defaultQueue", UNSET)

        excess_weight = d.pop("excessWeight", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        utilization_kbps = d.pop("utilizationKbps", UNSET)

        utilization_pct = d.pop("utilizationPct", UNSET)

        post_v2_monitoring_circuits_utilization_response_200_data_item_queue_utilization_item = cls(
            allocated_pct=allocated_pct,
            default_queue=default_queue,
            excess_weight=excess_weight,
            sla_class=sla_class,
            utilization_kbps=utilization_kbps,
            utilization_pct=utilization_pct,
        )

        post_v2_monitoring_circuits_utilization_response_200_data_item_queue_utilization_item.additional_properties = d
        return post_v2_monitoring_circuits_utilization_response_200_data_item_queue_utilization_item

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
