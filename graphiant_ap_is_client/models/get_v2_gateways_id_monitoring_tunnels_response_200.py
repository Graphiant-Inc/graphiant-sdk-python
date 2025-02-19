from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item import (
        GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem,
    )


T = TypeVar("T", bound="GetV2GatewaysIdMonitoringTunnelsResponse200")


@_attrs_define
class GetV2GatewaysIdMonitoringTunnelsResponse200:
    """
    Attributes:
        destination_address (Union[Unset, str]):  Example: TYPE_STRING.
        num_tunnels (Union[Unset, str]):  Example: TYPE_UINT32.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        sessions (Union[Unset, list['GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem']]):
    """

    destination_address: Union[Unset, str] = UNSET
    num_tunnels: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    sessions: Union[Unset, list["GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_address = self.destination_address

        num_tunnels = self.num_tunnels

        region_name = self.region_name

        sessions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()
                sessions.append(sessions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if num_tunnels is not UNSET:
            field_dict["numTunnels"] = num_tunnels
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if sessions is not UNSET:
            field_dict["sessions"] = sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_gateways_id_monitoring_tunnels_response_200_sessions_item import (
            GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem,
        )

        d = src_dict.copy()
        destination_address = d.pop("destinationAddress", UNSET)

        num_tunnels = d.pop("numTunnels", UNSET)

        region_name = d.pop("regionName", UNSET)

        sessions = []
        _sessions = d.pop("sessions", UNSET)
        for sessions_item_data in _sessions or []:
            sessions_item = GetV2GatewaysIdMonitoringTunnelsResponse200SessionsItem.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        get_v2_gateways_id_monitoring_tunnels_response_200 = cls(
            destination_address=destination_address,
            num_tunnels=num_tunnels,
            region_name=region_name,
            sessions=sessions,
        )

        get_v2_gateways_id_monitoring_tunnels_response_200.additional_properties = d
        return get_v2_gateways_id_monitoring_tunnels_response_200

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
