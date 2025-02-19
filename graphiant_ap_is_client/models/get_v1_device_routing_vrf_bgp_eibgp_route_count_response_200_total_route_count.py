from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount")


@_attrs_define
class GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount:
    """
    Attributes:
        ipv4 (Union[Unset, str]):  Example: 32.
        ipv6 (Union[Unset, str]):  Example: 6532.
    """

    ipv4: Union[Unset, str] = UNSET
    ipv6: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv4 = self.ipv4

        ipv6 = self.ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipv4 = d.pop("ipv4", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_total_route_count = cls(
            ipv4=ipv4,
            ipv6=ipv6,
        )

        get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_total_route_count.additional_properties = d
        return get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_total_route_count

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
