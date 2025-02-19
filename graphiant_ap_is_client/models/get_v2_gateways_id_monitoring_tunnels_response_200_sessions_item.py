from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession,
    )
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel,
    )


T = TypeVar("T", bound="GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem")


@_attrs_define
class GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem:
    """
    Attributes:
        bgp_session (Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession]):
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        tunnel (Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel]):
    """

    bgp_session: Union[Unset, "GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession"] = UNSET
    interface_name: Union[Unset, str] = UNSET
    tunnel: Union[Unset, "GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_session, Unset):
            bgp_session = self.bgp_session.to_dict()

        interface_name = self.interface_name

        tunnel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tunnel, Unset):
            tunnel = self.tunnel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_session is not UNSET:
            field_dict["bgpSession"] = bgp_session
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_bgp_session import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession,
        )
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item_tunnel import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel,
        )

        d = src_dict.copy()
        _bgp_session = d.pop("bgpSession", UNSET)
        bgp_session: Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession]
        if isinstance(_bgp_session, Unset):
            bgp_session = UNSET
        else:
            bgp_session = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemBgpSession.from_dict(_bgp_session)

        interface_name = d.pop("interfaceName", UNSET)

        _tunnel = d.pop("tunnel", UNSET)
        tunnel: Union[Unset, GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel]
        if isinstance(_tunnel, Unset):
            tunnel = UNSET
        else:
            tunnel = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItemTunnel.from_dict(_tunnel)

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item = cls(
            bgp_session=bgp_session,
            interface_name=interface_name,
            tunnel=tunnel,
        )

        get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item.additional_properties = d
        return get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item

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
