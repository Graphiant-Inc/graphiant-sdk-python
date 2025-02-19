from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_vrf_bgp_graphiant_eiroute_count_response_200_route_count import (
        GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200")


@_attrs_define
class GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200:
    """
    Attributes:
        route_count (Union[Unset, GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount]):
    """

    route_count: Union[Unset, "GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.route_count, Unset):
            route_count = self.route_count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if route_count is not UNSET:
            field_dict["routeCount"] = route_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_vrf_bgp_graphiant_eiroute_count_response_200_route_count import (
            GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount,
        )

        d = src_dict.copy()
        _route_count = d.pop("routeCount", UNSET)
        route_count: Union[Unset, GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount]
        if isinstance(_route_count, Unset):
            route_count = UNSET
        else:
            route_count = GetV1DeviceRoutingVrfBgpGraphiantEirouteCountResponse200RouteCount.from_dict(_route_count)

        get_v1_device_routing_vrf_bgp_graphiant_eiroute_count_response_200 = cls(
            route_count=route_count,
        )

        get_v1_device_routing_vrf_bgp_graphiant_eiroute_count_response_200.additional_properties = d
        return get_v1_device_routing_vrf_bgp_graphiant_eiroute_count_response_200

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
