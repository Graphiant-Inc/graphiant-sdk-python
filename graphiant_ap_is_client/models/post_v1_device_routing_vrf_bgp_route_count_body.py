from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DeviceRoutingVrfBgpRouteCountBody")


@_attrs_define
class PostV1DeviceRoutingVrfBgpRouteCountBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: 1000000.
        vrf_name (Union[Unset, list[str]]):  Example: ['management'].
    """

    device_id: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        vrf_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vrf_name, Unset):
            vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        vrf_name = cast(list[str], d.pop("vrfName", UNSET))

        post_v1_device_routing_vrf_bgp_route_count_body = cls(
            device_id=device_id,
            vrf_name=vrf_name,
        )

        post_v1_device_routing_vrf_bgp_route_count_body.additional_properties = d
        return post_v1_device_routing_vrf_bgp_route_count_body

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
