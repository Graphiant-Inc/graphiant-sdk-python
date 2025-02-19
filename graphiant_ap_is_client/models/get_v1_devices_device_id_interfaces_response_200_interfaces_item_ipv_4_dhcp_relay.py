from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv4DhcpRelay")


@_attrs_define
class GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv4DhcpRelay:
    """
    Attributes:
        dhcpv_4_relays (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        dhcpv_6_relays (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    dhcpv_4_relays: Union[Unset, list[str]] = UNSET
    dhcpv_6_relays: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dhcpv_4_relays: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dhcpv_4_relays, Unset):
            dhcpv_4_relays = self.dhcpv_4_relays

        dhcpv_6_relays: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dhcpv_6_relays, Unset):
            dhcpv_6_relays = self.dhcpv_6_relays

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcpv_4_relays is not UNSET:
            field_dict["dhcpv4Relays"] = dhcpv_4_relays
        if dhcpv_6_relays is not UNSET:
            field_dict["dhcpv6Relays"] = dhcpv_6_relays
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dhcpv_4_relays = cast(list[str], d.pop("dhcpv4Relays", UNSET))

        dhcpv_6_relays = cast(list[str], d.pop("dhcpv6Relays", UNSET))

        id = d.pop("id", UNSET)

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_4_dhcp_relay = cls(
            dhcpv_4_relays=dhcpv_4_relays,
            dhcpv_6_relays=dhcpv_6_relays,
            id=id,
        )

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_4_dhcp_relay.additional_properties = d
        return get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_4_dhcp_relay

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
