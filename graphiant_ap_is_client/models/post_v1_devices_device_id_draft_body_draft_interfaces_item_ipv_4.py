from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4_dhcp_relay import (
        PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4_vrrp_group import (
        PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4:
    """
    Attributes:
        address (Union[Unset, str]):  Example: TYPE_STRING.
        dhcp_client (Union[Unset, str]):  Example: TYPE_BOOL.
        dhcp_relay (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay]):
        dhcp_server (Union[Unset, str]):  Example: TYPE_BOOL.
        origin (Union[Unset, str]):  Example: TYPE_ENUM.
        vrrp_group (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup]):
    """

    address: Union[Unset, str] = UNSET
    dhcp_client: Union[Unset, str] = UNSET
    dhcp_relay: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay"] = UNSET
    dhcp_server: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    vrrp_group: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        dhcp_client = self.dhcp_client

        dhcp_relay: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dhcp_relay, Unset):
            dhcp_relay = self.dhcp_relay.to_dict()

        dhcp_server = self.dhcp_server

        origin = self.origin

        vrrp_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vrrp_group, Unset):
            vrrp_group = self.vrrp_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if dhcp_client is not UNSET:
            field_dict["dhcpClient"] = dhcp_client
        if dhcp_relay is not UNSET:
            field_dict["dhcpRelay"] = dhcp_relay
        if dhcp_server is not UNSET:
            field_dict["dhcpServer"] = dhcp_server
        if origin is not UNSET:
            field_dict["origin"] = origin
        if vrrp_group is not UNSET:
            field_dict["vrrpGroup"] = vrrp_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4_dhcp_relay import (
            PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4_vrrp_group import (
            PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        dhcp_client = d.pop("dhcpClient", UNSET)

        _dhcp_relay = d.pop("dhcpRelay", UNSET)
        dhcp_relay: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay]
        if isinstance(_dhcp_relay, Unset):
            dhcp_relay = UNSET
        else:
            dhcp_relay = PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4DhcpRelay.from_dict(_dhcp_relay)

        dhcp_server = d.pop("dhcpServer", UNSET)

        origin = d.pop("origin", UNSET)

        _vrrp_group = d.pop("vrrpGroup", UNSET)
        vrrp_group: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup]
        if isinstance(_vrrp_group, Unset):
            vrrp_group = UNSET
        else:
            vrrp_group = PostV1DevicesDeviceIdDraftBodyDraftInterfacesItemIpv4VrrpGroup.from_dict(_vrrp_group)

        post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4 = cls(
            address=address,
            dhcp_client=dhcp_client,
            dhcp_relay=dhcp_relay,
            dhcp_server=dhcp_server,
            origin=origin,
            vrrp_group=vrrp_group,
        )

        post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_interfaces_item_ipv_4

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
