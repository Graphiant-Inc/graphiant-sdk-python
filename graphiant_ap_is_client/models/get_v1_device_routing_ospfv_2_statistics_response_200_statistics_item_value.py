from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2StatisticsResponse200StatisticsItemValue")


@_attrs_define
class GetV1DeviceRoutingOspfv2StatisticsResponse200StatisticsItemValue:
    """
    Attributes:
        discontinuity_time (Union[Unset, str]):  Example: TYPE_STRING.
        route_count (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    discontinuity_time: Union[Unset, str] = UNSET
    route_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discontinuity_time = self.discontinuity_time

        route_count = self.route_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discontinuity_time is not UNSET:
            field_dict["discontinuityTime"] = discontinuity_time
        if route_count is not UNSET:
            field_dict["routeCount"] = route_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        discontinuity_time = d.pop("discontinuityTime", UNSET)

        route_count = d.pop("routeCount", UNSET)

        get_v1_device_routing_ospfv_2_statistics_response_200_statistics_item_value = cls(
            discontinuity_time=discontinuity_time,
            route_count=route_count,
        )

        get_v1_device_routing_ospfv_2_statistics_response_200_statistics_item_value.additional_properties = d
        return get_v1_device_routing_ospfv_2_statistics_response_200_statistics_item_value

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
