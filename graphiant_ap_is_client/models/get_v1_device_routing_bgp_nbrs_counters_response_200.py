from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_bgp_nbrs_counters_response_200_counters_item import (
        GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrsCountersResponse200")


@_attrs_define
class GetV1DeviceRoutingBgpNbrsCountersResponse200:
    """
    Attributes:
        counters (Union[Unset, list['GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem']]):
    """

    counters: Union[Unset, list["GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counters, Unset):
            counters = []
            for counters_item_data in self.counters:
                counters_item = counters_item_data.to_dict()
                counters.append(counters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counters is not UNSET:
            field_dict["counters"] = counters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_bgp_nbrs_counters_response_200_counters_item import (
            GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem,
        )

        d = src_dict.copy()
        counters = []
        _counters = d.pop("counters", UNSET)
        for counters_item_data in _counters or []:
            counters_item = GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem.from_dict(counters_item_data)

            counters.append(counters_item)

        get_v1_device_routing_bgp_nbrs_counters_response_200 = cls(
            counters=counters,
        )

        get_v1_device_routing_bgp_nbrs_counters_response_200.additional_properties = d
        return get_v1_device_routing_bgp_nbrs_counters_response_200

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
