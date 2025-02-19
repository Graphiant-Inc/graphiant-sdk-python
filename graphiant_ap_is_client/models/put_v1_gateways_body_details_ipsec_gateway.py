from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_gateways_body_details_ipsec_gateway_routing import PutV1GatewaysBodyDetailsIpsecGatewayRouting
    from ..models.put_v1_gateways_body_details_ipsec_gateway_tunnel_1 import PutV1GatewaysBodyDetailsIpsecGatewayTunnel1
    from ..models.put_v1_gateways_body_details_ipsec_gateway_tunnel_2 import PutV1GatewaysBodyDetailsIpsecGatewayTunnel2


T = TypeVar("T", bound="PutV1GatewaysBodyDetailsIpsecGateway")


@_attrs_define
class PutV1GatewaysBodyDetailsIpsecGateway:
    """
    Attributes:
        destination_address (Union[Unset, str]):  Example: TYPE_STRING.
        ike_initiator (Union[Unset, str]):  Example: TYPE_BOOL.
        mtu (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        remote_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        routing (Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayRouting]):
        tcp_mss (Union[Unset, str]):  Example: TYPE_UINT32.
        tunnel1 (Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayTunnel1]):
        tunnel2 (Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayTunnel2]):
        vpn_profile (Union[Unset, str]):  Example: TYPE_STRING.
    """

    destination_address: Union[Unset, str] = UNSET
    ike_initiator: Union[Unset, str] = UNSET
    mtu: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remote_ike_peer_identity: Union[Unset, str] = UNSET
    routing: Union[Unset, "PutV1GatewaysBodyDetailsIpsecGatewayRouting"] = UNSET
    tcp_mss: Union[Unset, str] = UNSET
    tunnel1: Union[Unset, "PutV1GatewaysBodyDetailsIpsecGatewayTunnel1"] = UNSET
    tunnel2: Union[Unset, "PutV1GatewaysBodyDetailsIpsecGatewayTunnel2"] = UNSET
    vpn_profile: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_address = self.destination_address

        ike_initiator = self.ike_initiator

        mtu = self.mtu

        name = self.name

        remote_ike_peer_identity = self.remote_ike_peer_identity

        routing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.to_dict()

        tcp_mss = self.tcp_mss

        tunnel1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tunnel1, Unset):
            tunnel1 = self.tunnel1.to_dict()

        tunnel2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tunnel2, Unset):
            tunnel2 = self.tunnel2.to_dict()

        vpn_profile = self.vpn_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if ike_initiator is not UNSET:
            field_dict["ikeInitiator"] = ike_initiator
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name is not UNSET:
            field_dict["name"] = name
        if remote_ike_peer_identity is not UNSET:
            field_dict["remoteIkePeerIdentity"] = remote_ike_peer_identity
        if routing is not UNSET:
            field_dict["routing"] = routing
        if tcp_mss is not UNSET:
            field_dict["tcpMss"] = tcp_mss
        if tunnel1 is not UNSET:
            field_dict["tunnel1"] = tunnel1
        if tunnel2 is not UNSET:
            field_dict["tunnel2"] = tunnel2
        if vpn_profile is not UNSET:
            field_dict["vpnProfile"] = vpn_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_gateways_body_details_ipsec_gateway_routing import (
            PutV1GatewaysBodyDetailsIpsecGatewayRouting,
        )
        from ..models.put_v1_gateways_body_details_ipsec_gateway_tunnel_1 import (
            PutV1GatewaysBodyDetailsIpsecGatewayTunnel1,
        )
        from ..models.put_v1_gateways_body_details_ipsec_gateway_tunnel_2 import (
            PutV1GatewaysBodyDetailsIpsecGatewayTunnel2,
        )

        d = src_dict.copy()
        destination_address = d.pop("destinationAddress", UNSET)

        ike_initiator = d.pop("ikeInitiator", UNSET)

        mtu = d.pop("mtu", UNSET)

        name = d.pop("name", UNSET)

        remote_ike_peer_identity = d.pop("remoteIkePeerIdentity", UNSET)

        _routing = d.pop("routing", UNSET)
        routing: Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayRouting]
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = PutV1GatewaysBodyDetailsIpsecGatewayRouting.from_dict(_routing)

        tcp_mss = d.pop("tcpMss", UNSET)

        _tunnel1 = d.pop("tunnel1", UNSET)
        tunnel1: Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayTunnel1]
        if isinstance(_tunnel1, Unset):
            tunnel1 = UNSET
        else:
            tunnel1 = PutV1GatewaysBodyDetailsIpsecGatewayTunnel1.from_dict(_tunnel1)

        _tunnel2 = d.pop("tunnel2", UNSET)
        tunnel2: Union[Unset, PutV1GatewaysBodyDetailsIpsecGatewayTunnel2]
        if isinstance(_tunnel2, Unset):
            tunnel2 = UNSET
        else:
            tunnel2 = PutV1GatewaysBodyDetailsIpsecGatewayTunnel2.from_dict(_tunnel2)

        vpn_profile = d.pop("vpnProfile", UNSET)

        put_v1_gateways_body_details_ipsec_gateway = cls(
            destination_address=destination_address,
            ike_initiator=ike_initiator,
            mtu=mtu,
            name=name,
            remote_ike_peer_identity=remote_ike_peer_identity,
            routing=routing,
            tcp_mss=tcp_mss,
            tunnel1=tunnel1,
            tunnel2=tunnel2,
            vpn_profile=vpn_profile,
        )

        put_v1_gateways_body_details_ipsec_gateway.additional_properties = d
        return put_v1_gateways_body_details_ipsec_gateway

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
