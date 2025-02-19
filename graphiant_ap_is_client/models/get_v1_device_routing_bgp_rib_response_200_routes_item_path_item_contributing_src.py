from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingBgpRibResponse200RoutesItemPathItemContributingSrc")


@_attrs_define
class GetV1DeviceRoutingBgpRibResponse200RoutesItemPathItemContributingSrc:
    """
    Attributes:
        rd (Union[Unset, str]):  Example: 10:1231.
        vrf (Union[Unset, str]):  Example: graphiant-odp.
    """

    rd: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rd = self.rd

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rd is not UNSET:
            field_dict["rd"] = rd
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        rd = d.pop("rd", UNSET)

        vrf = d.pop("vrf", UNSET)

        get_v1_device_routing_bgp_rib_response_200_routes_item_path_item_contributing_src = cls(
            rd=rd,
            vrf=vrf,
        )

        get_v1_device_routing_bgp_rib_response_200_routes_item_path_item_contributing_src.additional_properties = d
        return get_v1_device_routing_bgp_rib_response_200_routes_item_path_item_contributing_src

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
