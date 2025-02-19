from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel_uptime import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime,
    )
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel_vpn_profile import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile,
    )


T = TypeVar("T", bound="GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel")


@_attrs_define
class GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel:
    """
    Attributes:
        destination_ip (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        error_string (Union[Unset, str]):  Example: TYPE_STRING.
        source_ip (Union[Unset, str]):  Example: TYPE_STRING.
        source_port (Union[Unset, str]):  Example: TYPE_UINT32.
        up (Union[Unset, str]):  Example: TYPE_BOOL.
        uptime (Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime]):
        vpn_profile (Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile]):
    """

    destination_ip: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    error_string: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    source_port: Union[Unset, str] = UNSET
    up: Union[Unset, str] = UNSET
    uptime: Union[Unset, "GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime"] = UNSET
    vpn_profile: Union[Unset, "GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_ip = self.destination_ip

        destination_port = self.destination_port

        error_string = self.error_string

        source_ip = self.source_ip

        source_port = self.source_port

        up = self.up

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        vpn_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vpn_profile, Unset):
            vpn_profile = self.vpn_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_ip is not UNSET:
            field_dict["destinationIp"] = destination_ip
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if error_string is not UNSET:
            field_dict["errorString"] = error_string
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if source_port is not UNSET:
            field_dict["sourcePort"] = source_port
        if up is not UNSET:
            field_dict["up"] = up
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if vpn_profile is not UNSET:
            field_dict["vpnProfile"] = vpn_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel_uptime import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime,
        )
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel_vpn_profile import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile,
        )

        d = src_dict.copy()
        destination_ip = d.pop("destinationIp", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        error_string = d.pop("errorString", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        source_port = d.pop("sourcePort", UNSET)

        up = d.pop("up", UNSET)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelUptime.from_dict(_uptime)

        _vpn_profile = d.pop("vpnProfile", UNSET)
        vpn_profile: Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile]
        if isinstance(_vpn_profile, Unset):
            vpn_profile = UNSET
        else:
            vpn_profile = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnelVpnProfile.from_dict(
                _vpn_profile
            )

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel = cls(
            destination_ip=destination_ip,
            destination_port=destination_port,
            error_string=error_string,
            source_ip=source_ip,
            source_port=source_port,
            up=up,
            uptime=uptime,
            vpn_profile=vpn_profile,
        )

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel.additional_properties = d
        return get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel

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
