from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_ipsec_tunnels_item_bgp_address_families_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgpAddressFamiliesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgp")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgp:
    """
    Attributes:
        address_families (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgpAddressFamiliesItem']]):
        hold_timer (Union[Unset, str]):  Example: TYPE_UINT32.
        keepalive_timer (Union[Unset, str]):  Example: TYPE_UINT32.
        md_5_password (Union[Unset, str]):  Example: TYPE_STRING.
        peer_asn (Union[Unset, str]):  Example: TYPE_UINT32.
        send_community (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    address_families: Union[
        Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgpAddressFamiliesItem"]
    ] = UNSET
    hold_timer: Union[Unset, str] = UNSET
    keepalive_timer: Union[Unset, str] = UNSET
    md_5_password: Union[Unset, str] = UNSET
    peer_asn: Union[Unset, str] = UNSET
    send_community: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_families: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.address_families, Unset):
            address_families = []
            for address_families_item_data in self.address_families:
                address_families_item = address_families_item_data.to_dict()
                address_families.append(address_families_item)

        hold_timer = self.hold_timer

        keepalive_timer = self.keepalive_timer

        md_5_password = self.md_5_password

        peer_asn = self.peer_asn

        send_community = self.send_community

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_families is not UNSET:
            field_dict["addressFamilies"] = address_families
        if hold_timer is not UNSET:
            field_dict["holdTimer"] = hold_timer
        if keepalive_timer is not UNSET:
            field_dict["keepaliveTimer"] = keepalive_timer
        if md_5_password is not UNSET:
            field_dict["md5Password"] = md_5_password
        if peer_asn is not UNSET:
            field_dict["peerAsn"] = peer_asn
        if send_community is not UNSET:
            field_dict["sendCommunity"] = send_community

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_ipsec_tunnels_item_bgp_address_families_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgpAddressFamiliesItem,
        )

        d = src_dict.copy()
        address_families = []
        _address_families = d.pop("addressFamilies", UNSET)
        for address_families_item_data in _address_families or []:
            address_families_item = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemIpsecTunnelsItemBgpAddressFamiliesItem.from_dict(
                    address_families_item_data
                )
            )

            address_families.append(address_families_item)

        hold_timer = d.pop("holdTimer", UNSET)

        keepalive_timer = d.pop("keepaliveTimer", UNSET)

        md_5_password = d.pop("md5Password", UNSET)

        peer_asn = d.pop("peerAsn", UNSET)

        send_community = d.pop("sendCommunity", UNSET)

        get_v1_devices_device_id_edges_response_200_devices_item_ipsec_tunnels_item_bgp = cls(
            address_families=address_families,
            hold_timer=hold_timer,
            keepalive_timer=keepalive_timer,
            md_5_password=md_5_password,
            peer_asn=peer_asn,
            send_community=send_community,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_ipsec_tunnels_item_bgp.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_ipsec_tunnels_item_bgp

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
