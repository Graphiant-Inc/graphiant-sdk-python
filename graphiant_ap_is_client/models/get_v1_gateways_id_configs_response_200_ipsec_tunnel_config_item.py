from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem")


@_attrs_define
class GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem:
    """
    Attributes:
        bgp_graphiant_asn (Union[Unset, str]):  Example: TYPE_UINT32.
        bgp_local_asn (Union[Unset, str]):  Example: TYPE_UINT32.
        bgp_neighbor_hold_time (Union[Unset, str]):  Example: TYPE_UINT32.
        bgp_neighbor_ipv_4 (Union[Unset, str]):  Example: TYPE_STRING.
        bgp_neighbor_ipv_6 (Union[Unset, str]):  Example: TYPE_STRING.
        dpd_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        dpd_retries (Union[Unset, str]):  Example: TYPE_UINT32.
        graphiant_destination_ip (Union[Unset, str]):  Example: TYPE_STRING.
        graphiant_ike_id (Union[Unset, str]):  Example: TYPE_STRING.
        graphiant_outer_tunnel_ip (Union[Unset, str]):  Example: TYPE_STRING.
        graphiant_tunnel_ip (Union[Unset, str]):  Example: TYPE_STRING.
        graphiant_tunnel_ipv_6 (Union[Unset, str]):  Example: TYPE_STRING.
        ike_authentication_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ike_authentication_method (Union[Unset, str]):  Example: TYPE_STRING.
        ike_dh_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ike_encryption_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ike_lifetime (Union[Unset, str]):  Example: TYPE_STRING.
        ike_preshared_key (Union[Unset, str]):  Example: TYPE_STRING.
        ike_version (Union[Unset, str]):  Example: TYPE_INT32.
        ipsec_authentication_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_encryption_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_extended_sequence_number (Union[Unset, str]):  Example: TYPE_BOOL.
        ipsec_lifetime (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_mode (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_pfs_algorithm (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_protocol (Union[Unset, str]):  Example: TYPE_STRING.
        local_ike_id (Union[Unset, str]):  Example: TYPE_STRING.
        local_outer_tunnel_ip (Union[Unset, str]):  Example: TYPE_STRING.
        local_tunnel_ip (Union[Unset, str]):  Example: TYPE_STRING.
        local_tunnel_ipv_6 (Union[Unset, str]):  Example: TYPE_STRING.
        tcp_mss (Union[Unset, str]):  Example: TYPE_UINT32.
        tunnel_mtu (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    bgp_graphiant_asn: Union[Unset, str] = UNSET
    bgp_local_asn: Union[Unset, str] = UNSET
    bgp_neighbor_hold_time: Union[Unset, str] = UNSET
    bgp_neighbor_ipv_4: Union[Unset, str] = UNSET
    bgp_neighbor_ipv_6: Union[Unset, str] = UNSET
    dpd_interval: Union[Unset, str] = UNSET
    dpd_retries: Union[Unset, str] = UNSET
    graphiant_destination_ip: Union[Unset, str] = UNSET
    graphiant_ike_id: Union[Unset, str] = UNSET
    graphiant_outer_tunnel_ip: Union[Unset, str] = UNSET
    graphiant_tunnel_ip: Union[Unset, str] = UNSET
    graphiant_tunnel_ipv_6: Union[Unset, str] = UNSET
    ike_authentication_algorithm: Union[Unset, str] = UNSET
    ike_authentication_method: Union[Unset, str] = UNSET
    ike_dh_algorithm: Union[Unset, str] = UNSET
    ike_encryption_algorithm: Union[Unset, str] = UNSET
    ike_lifetime: Union[Unset, str] = UNSET
    ike_preshared_key: Union[Unset, str] = UNSET
    ike_version: Union[Unset, str] = UNSET
    ipsec_authentication_algorithm: Union[Unset, str] = UNSET
    ipsec_encryption_algorithm: Union[Unset, str] = UNSET
    ipsec_extended_sequence_number: Union[Unset, str] = UNSET
    ipsec_lifetime: Union[Unset, str] = UNSET
    ipsec_mode: Union[Unset, str] = UNSET
    ipsec_pfs_algorithm: Union[Unset, str] = UNSET
    ipsec_protocol: Union[Unset, str] = UNSET
    local_ike_id: Union[Unset, str] = UNSET
    local_outer_tunnel_ip: Union[Unset, str] = UNSET
    local_tunnel_ip: Union[Unset, str] = UNSET
    local_tunnel_ipv_6: Union[Unset, str] = UNSET
    tcp_mss: Union[Unset, str] = UNSET
    tunnel_mtu: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_graphiant_asn = self.bgp_graphiant_asn

        bgp_local_asn = self.bgp_local_asn

        bgp_neighbor_hold_time = self.bgp_neighbor_hold_time

        bgp_neighbor_ipv_4 = self.bgp_neighbor_ipv_4

        bgp_neighbor_ipv_6 = self.bgp_neighbor_ipv_6

        dpd_interval = self.dpd_interval

        dpd_retries = self.dpd_retries

        graphiant_destination_ip = self.graphiant_destination_ip

        graphiant_ike_id = self.graphiant_ike_id

        graphiant_outer_tunnel_ip = self.graphiant_outer_tunnel_ip

        graphiant_tunnel_ip = self.graphiant_tunnel_ip

        graphiant_tunnel_ipv_6 = self.graphiant_tunnel_ipv_6

        ike_authentication_algorithm = self.ike_authentication_algorithm

        ike_authentication_method = self.ike_authentication_method

        ike_dh_algorithm = self.ike_dh_algorithm

        ike_encryption_algorithm = self.ike_encryption_algorithm

        ike_lifetime = self.ike_lifetime

        ike_preshared_key = self.ike_preshared_key

        ike_version = self.ike_version

        ipsec_authentication_algorithm = self.ipsec_authentication_algorithm

        ipsec_encryption_algorithm = self.ipsec_encryption_algorithm

        ipsec_extended_sequence_number = self.ipsec_extended_sequence_number

        ipsec_lifetime = self.ipsec_lifetime

        ipsec_mode = self.ipsec_mode

        ipsec_pfs_algorithm = self.ipsec_pfs_algorithm

        ipsec_protocol = self.ipsec_protocol

        local_ike_id = self.local_ike_id

        local_outer_tunnel_ip = self.local_outer_tunnel_ip

        local_tunnel_ip = self.local_tunnel_ip

        local_tunnel_ipv_6 = self.local_tunnel_ipv_6

        tcp_mss = self.tcp_mss

        tunnel_mtu = self.tunnel_mtu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_graphiant_asn is not UNSET:
            field_dict["bgpGraphiantAsn"] = bgp_graphiant_asn
        if bgp_local_asn is not UNSET:
            field_dict["bgpLocalAsn"] = bgp_local_asn
        if bgp_neighbor_hold_time is not UNSET:
            field_dict["bgpNeighborHoldTime"] = bgp_neighbor_hold_time
        if bgp_neighbor_ipv_4 is not UNSET:
            field_dict["bgpNeighborIpv4"] = bgp_neighbor_ipv_4
        if bgp_neighbor_ipv_6 is not UNSET:
            field_dict["bgpNeighborIpv6"] = bgp_neighbor_ipv_6
        if dpd_interval is not UNSET:
            field_dict["dpdInterval"] = dpd_interval
        if dpd_retries is not UNSET:
            field_dict["dpdRetries"] = dpd_retries
        if graphiant_destination_ip is not UNSET:
            field_dict["graphiantDestinationIp"] = graphiant_destination_ip
        if graphiant_ike_id is not UNSET:
            field_dict["graphiantIkeId"] = graphiant_ike_id
        if graphiant_outer_tunnel_ip is not UNSET:
            field_dict["graphiantOuterTunnelIp"] = graphiant_outer_tunnel_ip
        if graphiant_tunnel_ip is not UNSET:
            field_dict["graphiantTunnelIp"] = graphiant_tunnel_ip
        if graphiant_tunnel_ipv_6 is not UNSET:
            field_dict["graphiantTunnelIpv6"] = graphiant_tunnel_ipv_6
        if ike_authentication_algorithm is not UNSET:
            field_dict["ikeAuthenticationAlgorithm"] = ike_authentication_algorithm
        if ike_authentication_method is not UNSET:
            field_dict["ikeAuthenticationMethod"] = ike_authentication_method
        if ike_dh_algorithm is not UNSET:
            field_dict["ikeDhAlgorithm"] = ike_dh_algorithm
        if ike_encryption_algorithm is not UNSET:
            field_dict["ikeEncryptionAlgorithm"] = ike_encryption_algorithm
        if ike_lifetime is not UNSET:
            field_dict["ikeLifetime"] = ike_lifetime
        if ike_preshared_key is not UNSET:
            field_dict["ikePresharedKey"] = ike_preshared_key
        if ike_version is not UNSET:
            field_dict["ikeVersion"] = ike_version
        if ipsec_authentication_algorithm is not UNSET:
            field_dict["ipsecAuthenticationAlgorithm"] = ipsec_authentication_algorithm
        if ipsec_encryption_algorithm is not UNSET:
            field_dict["ipsecEncryptionAlgorithm"] = ipsec_encryption_algorithm
        if ipsec_extended_sequence_number is not UNSET:
            field_dict["ipsecExtendedSequenceNumber"] = ipsec_extended_sequence_number
        if ipsec_lifetime is not UNSET:
            field_dict["ipsecLifetime"] = ipsec_lifetime
        if ipsec_mode is not UNSET:
            field_dict["ipsecMode"] = ipsec_mode
        if ipsec_pfs_algorithm is not UNSET:
            field_dict["ipsecPfsAlgorithm"] = ipsec_pfs_algorithm
        if ipsec_protocol is not UNSET:
            field_dict["ipsecProtocol"] = ipsec_protocol
        if local_ike_id is not UNSET:
            field_dict["localIkeId"] = local_ike_id
        if local_outer_tunnel_ip is not UNSET:
            field_dict["localOuterTunnelIp"] = local_outer_tunnel_ip
        if local_tunnel_ip is not UNSET:
            field_dict["localTunnelIp"] = local_tunnel_ip
        if local_tunnel_ipv_6 is not UNSET:
            field_dict["localTunnelIpv6"] = local_tunnel_ipv_6
        if tcp_mss is not UNSET:
            field_dict["tcpMss"] = tcp_mss
        if tunnel_mtu is not UNSET:
            field_dict["tunnelMtu"] = tunnel_mtu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bgp_graphiant_asn = d.pop("bgpGraphiantAsn", UNSET)

        bgp_local_asn = d.pop("bgpLocalAsn", UNSET)

        bgp_neighbor_hold_time = d.pop("bgpNeighborHoldTime", UNSET)

        bgp_neighbor_ipv_4 = d.pop("bgpNeighborIpv4", UNSET)

        bgp_neighbor_ipv_6 = d.pop("bgpNeighborIpv6", UNSET)

        dpd_interval = d.pop("dpdInterval", UNSET)

        dpd_retries = d.pop("dpdRetries", UNSET)

        graphiant_destination_ip = d.pop("graphiantDestinationIp", UNSET)

        graphiant_ike_id = d.pop("graphiantIkeId", UNSET)

        graphiant_outer_tunnel_ip = d.pop("graphiantOuterTunnelIp", UNSET)

        graphiant_tunnel_ip = d.pop("graphiantTunnelIp", UNSET)

        graphiant_tunnel_ipv_6 = d.pop("graphiantTunnelIpv6", UNSET)

        ike_authentication_algorithm = d.pop("ikeAuthenticationAlgorithm", UNSET)

        ike_authentication_method = d.pop("ikeAuthenticationMethod", UNSET)

        ike_dh_algorithm = d.pop("ikeDhAlgorithm", UNSET)

        ike_encryption_algorithm = d.pop("ikeEncryptionAlgorithm", UNSET)

        ike_lifetime = d.pop("ikeLifetime", UNSET)

        ike_preshared_key = d.pop("ikePresharedKey", UNSET)

        ike_version = d.pop("ikeVersion", UNSET)

        ipsec_authentication_algorithm = d.pop("ipsecAuthenticationAlgorithm", UNSET)

        ipsec_encryption_algorithm = d.pop("ipsecEncryptionAlgorithm", UNSET)

        ipsec_extended_sequence_number = d.pop("ipsecExtendedSequenceNumber", UNSET)

        ipsec_lifetime = d.pop("ipsecLifetime", UNSET)

        ipsec_mode = d.pop("ipsecMode", UNSET)

        ipsec_pfs_algorithm = d.pop("ipsecPfsAlgorithm", UNSET)

        ipsec_protocol = d.pop("ipsecProtocol", UNSET)

        local_ike_id = d.pop("localIkeId", UNSET)

        local_outer_tunnel_ip = d.pop("localOuterTunnelIp", UNSET)

        local_tunnel_ip = d.pop("localTunnelIp", UNSET)

        local_tunnel_ipv_6 = d.pop("localTunnelIpv6", UNSET)

        tcp_mss = d.pop("tcpMss", UNSET)

        tunnel_mtu = d.pop("tunnelMtu", UNSET)

        get_v1_gateways_id_configs_response_200_ipsec_tunnel_config_item = cls(
            bgp_graphiant_asn=bgp_graphiant_asn,
            bgp_local_asn=bgp_local_asn,
            bgp_neighbor_hold_time=bgp_neighbor_hold_time,
            bgp_neighbor_ipv_4=bgp_neighbor_ipv_4,
            bgp_neighbor_ipv_6=bgp_neighbor_ipv_6,
            dpd_interval=dpd_interval,
            dpd_retries=dpd_retries,
            graphiant_destination_ip=graphiant_destination_ip,
            graphiant_ike_id=graphiant_ike_id,
            graphiant_outer_tunnel_ip=graphiant_outer_tunnel_ip,
            graphiant_tunnel_ip=graphiant_tunnel_ip,
            graphiant_tunnel_ipv_6=graphiant_tunnel_ipv_6,
            ike_authentication_algorithm=ike_authentication_algorithm,
            ike_authentication_method=ike_authentication_method,
            ike_dh_algorithm=ike_dh_algorithm,
            ike_encryption_algorithm=ike_encryption_algorithm,
            ike_lifetime=ike_lifetime,
            ike_preshared_key=ike_preshared_key,
            ike_version=ike_version,
            ipsec_authentication_algorithm=ipsec_authentication_algorithm,
            ipsec_encryption_algorithm=ipsec_encryption_algorithm,
            ipsec_extended_sequence_number=ipsec_extended_sequence_number,
            ipsec_lifetime=ipsec_lifetime,
            ipsec_mode=ipsec_mode,
            ipsec_pfs_algorithm=ipsec_pfs_algorithm,
            ipsec_protocol=ipsec_protocol,
            local_ike_id=local_ike_id,
            local_outer_tunnel_ip=local_outer_tunnel_ip,
            local_tunnel_ip=local_tunnel_ip,
            local_tunnel_ipv_6=local_tunnel_ipv_6,
            tcp_mss=tcp_mss,
            tunnel_mtu=tunnel_mtu,
        )

        get_v1_gateways_id_configs_response_200_ipsec_tunnel_config_item.additional_properties = d
        return get_v1_gateways_id_configs_response_200_ipsec_tunnel_config_item

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
