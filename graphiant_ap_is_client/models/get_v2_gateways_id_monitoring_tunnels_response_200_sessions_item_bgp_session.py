from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session_uptime import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime,
    )


T = TypeVar("T", bound="GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession")


@_attrs_define
class GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession:
    """
    Attributes:
        local_ip (Union[Unset, str]):  Example: TYPE_STRING.
        remote_ip (Union[Unset, str]):  Example: TYPE_STRING.
        up (Union[Unset, str]):  Example: TYPE_BOOL.
        uptime (Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime]):
    """

    local_ip: Union[Unset, str] = UNSET
    remote_ip: Union[Unset, str] = UNSET
    up: Union[Unset, str] = UNSET
    uptime: Union[Unset, "GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_ip = self.local_ip

        remote_ip = self.remote_ip

        up = self.up

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if up is not UNSET:
            field_dict["up"] = up
        if uptime is not UNSET:
            field_dict["uptime"] = uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session_uptime import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime,
        )

        d = src_dict.copy()
        local_ip = d.pop("localIp", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        up = d.pop("up", UNSET)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSessionUptime.from_dict(_uptime)

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session = cls(
            local_ip=local_ip,
            remote_ip=remote_ip,
            up=up,
            uptime=uptime,
        )

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session.additional_properties = d
        return get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session

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
