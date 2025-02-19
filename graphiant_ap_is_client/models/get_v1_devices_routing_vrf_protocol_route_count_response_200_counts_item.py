from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_routing_vrf_protocol_route_count_response_200_counts_item_route_count import (
        GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount,
    )


T = TypeVar("T", bound="GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItem")


@_attrs_define
class GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItem:
    """
    Attributes:
        protocol (Union[Unset, str]):  Example: OSPF.
        route_count (Union[Unset, GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount]):
    """

    protocol: Union[Unset, str] = UNSET
    route_count: Union[Unset, "GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol = self.protocol

        route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.route_count, Unset):
            route_count = self.route_count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if route_count is not UNSET:
            field_dict["routeCount"] = route_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_routing_vrf_protocol_route_count_response_200_counts_item_route_count import (
            GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount,
        )

        d = src_dict.copy()
        protocol = d.pop("protocol", UNSET)

        _route_count = d.pop("routeCount", UNSET)
        route_count: Union[Unset, GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount]
        if isinstance(_route_count, Unset):
            route_count = UNSET
        else:
            route_count = GetV1DevicesRoutingVrfProtocolRouteCountResponse200CountsItemRouteCount.from_dict(
                _route_count
            )

        get_v1_devices_routing_vrf_protocol_route_count_response_200_counts_item = cls(
            protocol=protocol,
            route_count=route_count,
        )

        get_v1_devices_routing_vrf_protocol_route_count_response_200_counts_item.additional_properties = d
        return get_v1_devices_routing_vrf_protocol_route_count_response_200_counts_item

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
