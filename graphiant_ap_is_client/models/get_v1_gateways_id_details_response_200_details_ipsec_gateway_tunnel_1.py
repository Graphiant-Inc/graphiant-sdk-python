from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayTunnel1")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayTunnel1:
    """
    Attributes:
        inside_ipv_4_cidr (Union[Unset, str]):  Example: TYPE_STRING.
        inside_ipv_6_cidr (Union[Unset, str]):  Example: TYPE_STRING.
        local_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        psk (Union[Unset, str]):  Example: TYPE_STRING.
    """

    inside_ipv_4_cidr: Union[Unset, str] = UNSET
    inside_ipv_6_cidr: Union[Unset, str] = UNSET
    local_ike_peer_identity: Union[Unset, str] = UNSET
    psk: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inside_ipv_4_cidr = self.inside_ipv_4_cidr

        inside_ipv_6_cidr = self.inside_ipv_6_cidr

        local_ike_peer_identity = self.local_ike_peer_identity

        psk = self.psk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inside_ipv_4_cidr is not UNSET:
            field_dict["insideIpv4Cidr"] = inside_ipv_4_cidr
        if inside_ipv_6_cidr is not UNSET:
            field_dict["insideIpv6Cidr"] = inside_ipv_6_cidr
        if local_ike_peer_identity is not UNSET:
            field_dict["localIkePeerIdentity"] = local_ike_peer_identity
        if psk is not UNSET:
            field_dict["psk"] = psk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        inside_ipv_4_cidr = d.pop("insideIpv4Cidr", UNSET)

        inside_ipv_6_cidr = d.pop("insideIpv6Cidr", UNSET)

        local_ike_peer_identity = d.pop("localIkePeerIdentity", UNSET)

        psk = d.pop("psk", UNSET)

        get_v1_gateways_id_details_response_200_details_ipsec_gateway_tunnel_1 = cls(
            inside_ipv_4_cidr=inside_ipv_4_cidr,
            inside_ipv_6_cidr=inside_ipv_6_cidr,
            local_ike_peer_identity=local_ike_peer_identity,
            psk=psk,
        )

        get_v1_gateways_id_details_response_200_details_ipsec_gateway_tunnel_1.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_ipsec_gateway_tunnel_1

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
