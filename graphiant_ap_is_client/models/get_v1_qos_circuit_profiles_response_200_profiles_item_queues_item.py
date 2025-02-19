from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1QosCircuitProfilesResponse200ProfilesItemQueuesItem")


@_attrs_define
class GetV1QosCircuitProfilesResponse200ProfilesItemQueuesItem:
    """
    Attributes:
        bandwidth_percent (Union[Unset, str]):  Example: TYPE_UINT32.
        default_queue (Union[Unset, str]):  Example: TYPE_BOOL.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    bandwidth_percent: Union[Unset, str] = UNSET
    default_queue: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bandwidth_percent = self.bandwidth_percent

        default_queue = self.default_queue

        sla_class = self.sla_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bandwidth_percent is not UNSET:
            field_dict["bandwidthPercent"] = bandwidth_percent
        if default_queue is not UNSET:
            field_dict["defaultQueue"] = default_queue
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bandwidth_percent = d.pop("bandwidthPercent", UNSET)

        default_queue = d.pop("defaultQueue", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        get_v1_qos_circuit_profiles_response_200_profiles_item_queues_item = cls(
            bandwidth_percent=bandwidth_percent,
            default_queue=default_queue,
            sla_class=sla_class,
        )

        get_v1_qos_circuit_profiles_response_200_profiles_item_queues_item.additional_properties = d
        return get_v1_qos_circuit_profiles_response_200_profiles_item_queues_item

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
