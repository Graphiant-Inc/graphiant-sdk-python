from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingVrfBgpGraphiantRouteCountResponse200CountsItem")


@_attrs_define
class GetV1DeviceRoutingVrfBgpGraphiantRouteCountResponse200CountsItem:
    """
    Attributes:
        route_count (Union[Unset, str]):  Example: 1234.
        vrf_name (Union[Unset, str]):  Example: management.
    """

    route_count: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        route_count = self.route_count

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if route_count is not UNSET:
            field_dict["routeCount"] = route_count
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        route_count = d.pop("routeCount", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        get_v1_device_routing_vrf_bgp_graphiant_route_count_response_200_counts_item = cls(
            route_count=route_count,
            vrf_name=vrf_name,
        )

        get_v1_device_routing_vrf_bgp_graphiant_route_count_response_200_counts_item.additional_properties = d
        return get_v1_device_routing_vrf_bgp_graphiant_route_count_response_200_counts_item

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
