from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticTracerouteResponse200ResultRouteInfo")


@_attrs_define
class PostV1DiagnosticTracerouteResponse200ResultRouteInfo:
    """
    Attributes:
        nexthop_address (Union[Unset, str]):  Example: 1213:1::6451.
        outgoing_interface (Union[Unset, str]):  Example: Ethernet0/1.
        prefix (Union[Unset, str]):  Example: 1213:1::6451.
    """

    nexthop_address: Union[Unset, str] = UNSET
    outgoing_interface: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nexthop_address = self.nexthop_address

        outgoing_interface = self.outgoing_interface

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nexthop_address is not UNSET:
            field_dict["nexthopAddress"] = nexthop_address
        if outgoing_interface is not UNSET:
            field_dict["outgoingInterface"] = outgoing_interface
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        nexthop_address = d.pop("nexthopAddress", UNSET)

        outgoing_interface = d.pop("outgoingInterface", UNSET)

        prefix = d.pop("prefix", UNSET)

        post_v1_diagnostic_traceroute_response_200_result_route_info = cls(
            nexthop_address=nexthop_address,
            outgoing_interface=outgoing_interface,
            prefix=prefix,
        )

        post_v1_diagnostic_traceroute_response_200_result_route_info.additional_properties = d
        return post_v1_diagnostic_traceroute_response_200_result_route_info

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
