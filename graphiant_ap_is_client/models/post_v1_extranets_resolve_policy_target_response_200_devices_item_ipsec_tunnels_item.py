from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_bgp import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp,
    )
    from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_static import (
        PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic,
    )


T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItem")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItem:
    """
    Attributes:
        bgp (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp]):
        destination_address (Union[Unset, str]):  Example: TYPE_STRING.
        ike_initiator (Union[Unset, str]):  Example: TYPE_BOOL.
        ipsec_label (Union[Unset, str]):  Example: TYPE_ENUM.
        lan (Union[Unset, str]):  Example: TYPE_STRING.
        local_address_v4 (Union[Unset, str]):  Example: TYPE_STRING.
        local_address_v6 (Union[Unset, str]):  Example: TYPE_STRING.
        local_circuit (Union[Unset, str]):  Example: TYPE_STRING.
        local_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        mtu (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        preshared_key (Union[Unset, str]):  Example: TYPE_STRING.
        remote_address_v4 (Union[Unset, str]):  Example: TYPE_STRING.
        remote_address_v6 (Union[Unset, str]):  Example: TYPE_STRING.
        remote_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        static (Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic]):
        tcp_mss (Union[Unset, str]):  Example: TYPE_UINT32.
        vpn_profile (Union[Unset, str]):  Example: TYPE_STRING.
    """

    bgp: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp"] = UNSET
    destination_address: Union[Unset, str] = UNSET
    ike_initiator: Union[Unset, str] = UNSET
    ipsec_label: Union[Unset, str] = UNSET
    lan: Union[Unset, str] = UNSET
    local_address_v4: Union[Unset, str] = UNSET
    local_address_v6: Union[Unset, str] = UNSET
    local_circuit: Union[Unset, str] = UNSET
    local_ike_peer_identity: Union[Unset, str] = UNSET
    mtu: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preshared_key: Union[Unset, str] = UNSET
    remote_address_v4: Union[Unset, str] = UNSET
    remote_address_v6: Union[Unset, str] = UNSET
    remote_ike_peer_identity: Union[Unset, str] = UNSET
    static: Union[Unset, "PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic"] = UNSET
    tcp_mss: Union[Unset, str] = UNSET
    vpn_profile: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp, Unset):
            bgp = self.bgp.to_dict()

        destination_address = self.destination_address

        ike_initiator = self.ike_initiator

        ipsec_label = self.ipsec_label

        lan = self.lan

        local_address_v4 = self.local_address_v4

        local_address_v6 = self.local_address_v6

        local_circuit = self.local_circuit

        local_ike_peer_identity = self.local_ike_peer_identity

        mtu = self.mtu

        name = self.name

        preshared_key = self.preshared_key

        remote_address_v4 = self.remote_address_v4

        remote_address_v6 = self.remote_address_v6

        remote_ike_peer_identity = self.remote_ike_peer_identity

        static: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static, Unset):
            static = self.static.to_dict()

        tcp_mss = self.tcp_mss

        vpn_profile = self.vpn_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp is not UNSET:
            field_dict["bgp"] = bgp
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if ike_initiator is not UNSET:
            field_dict["ikeInitiator"] = ike_initiator
        if ipsec_label is not UNSET:
            field_dict["ipsecLabel"] = ipsec_label
        if lan is not UNSET:
            field_dict["lan"] = lan
        if local_address_v4 is not UNSET:
            field_dict["localAddressV4"] = local_address_v4
        if local_address_v6 is not UNSET:
            field_dict["localAddressV6"] = local_address_v6
        if local_circuit is not UNSET:
            field_dict["localCircuit"] = local_circuit
        if local_ike_peer_identity is not UNSET:
            field_dict["localIkePeerIdentity"] = local_ike_peer_identity
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name is not UNSET:
            field_dict["name"] = name
        if preshared_key is not UNSET:
            field_dict["presharedKey"] = preshared_key
        if remote_address_v4 is not UNSET:
            field_dict["remoteAddressV4"] = remote_address_v4
        if remote_address_v6 is not UNSET:
            field_dict["remoteAddressV6"] = remote_address_v6
        if remote_ike_peer_identity is not UNSET:
            field_dict["remoteIkePeerIdentity"] = remote_ike_peer_identity
        if static is not UNSET:
            field_dict["static"] = static
        if tcp_mss is not UNSET:
            field_dict["tcpMss"] = tcp_mss
        if vpn_profile is not UNSET:
            field_dict["vpnProfile"] = vpn_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_bgp import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp,
        )
        from ..models.post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_static import (
            PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic,
        )

        d = src_dict.copy()
        _bgp = d.pop("bgp", UNSET)
        bgp: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp]
        if isinstance(_bgp, Unset):
            bgp = UNSET
        else:
            bgp = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemBgp.from_dict(_bgp)

        destination_address = d.pop("destinationAddress", UNSET)

        ike_initiator = d.pop("ikeInitiator", UNSET)

        ipsec_label = d.pop("ipsecLabel", UNSET)

        lan = d.pop("lan", UNSET)

        local_address_v4 = d.pop("localAddressV4", UNSET)

        local_address_v6 = d.pop("localAddressV6", UNSET)

        local_circuit = d.pop("localCircuit", UNSET)

        local_ike_peer_identity = d.pop("localIkePeerIdentity", UNSET)

        mtu = d.pop("mtu", UNSET)

        name = d.pop("name", UNSET)

        preshared_key = d.pop("presharedKey", UNSET)

        remote_address_v4 = d.pop("remoteAddressV4", UNSET)

        remote_address_v6 = d.pop("remoteAddressV6", UNSET)

        remote_ike_peer_identity = d.pop("remoteIkePeerIdentity", UNSET)

        _static = d.pop("static", UNSET)
        static: Union[Unset, PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic]
        if isinstance(_static, Unset):
            static = UNSET
        else:
            static = PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic.from_dict(_static)

        tcp_mss = d.pop("tcpMss", UNSET)

        vpn_profile = d.pop("vpnProfile", UNSET)

        post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item = cls(
            bgp=bgp,
            destination_address=destination_address,
            ike_initiator=ike_initiator,
            ipsec_label=ipsec_label,
            lan=lan,
            local_address_v4=local_address_v4,
            local_address_v6=local_address_v6,
            local_circuit=local_circuit,
            local_ike_peer_identity=local_ike_peer_identity,
            mtu=mtu,
            name=name,
            preshared_key=preshared_key,
            remote_address_v4=remote_address_v4,
            remote_address_v6=remote_address_v6,
            remote_ike_peer_identity=remote_ike_peer_identity,
            static=static,
            tcp_mss=tcp_mss,
            vpn_profile=vpn_profile,
        )

        post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item.additional_properties = d
        return post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item

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
