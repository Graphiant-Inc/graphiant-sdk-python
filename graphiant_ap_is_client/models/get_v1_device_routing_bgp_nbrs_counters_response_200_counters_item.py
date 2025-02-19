from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem")


@_attrs_define
class GetV1DeviceRoutingBgpNbrsCountersResponse200CountersItem:
    """
    Attributes:
        graceful_restart (Union[Unset, str]):  Example: TYPE_UINT32.
        local_as_number (Union[Unset, str]):  Example: TYPE_UINT32.
        local_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        local_router_id (Union[Unset, str]):  Example: TYPE_STRING.
        peer_router_id (Union[Unset, str]):  Example: TYPE_STRING.
        up_time (Union[Unset, str]):  Example: TYPE_STRING.
    """

    graceful_restart: Union[Unset, str] = UNSET
    local_as_number: Union[Unset, str] = UNSET
    local_ip_address: Union[Unset, str] = UNSET
    local_router_id: Union[Unset, str] = UNSET
    peer_router_id: Union[Unset, str] = UNSET
    up_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graceful_restart = self.graceful_restart

        local_as_number = self.local_as_number

        local_ip_address = self.local_ip_address

        local_router_id = self.local_router_id

        peer_router_id = self.peer_router_id

        up_time = self.up_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if graceful_restart is not UNSET:
            field_dict["gracefulRestart"] = graceful_restart
        if local_as_number is not UNSET:
            field_dict["localAsNumber"] = local_as_number
        if local_ip_address is not UNSET:
            field_dict["localIpAddress"] = local_ip_address
        if local_router_id is not UNSET:
            field_dict["localRouterId"] = local_router_id
        if peer_router_id is not UNSET:
            field_dict["peerRouterId"] = peer_router_id
        if up_time is not UNSET:
            field_dict["upTime"] = up_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        graceful_restart = d.pop("gracefulRestart", UNSET)

        local_as_number = d.pop("localAsNumber", UNSET)

        local_ip_address = d.pop("localIpAddress", UNSET)

        local_router_id = d.pop("localRouterId", UNSET)

        peer_router_id = d.pop("peerRouterId", UNSET)

        up_time = d.pop("upTime", UNSET)

        get_v1_device_routing_bgp_nbrs_counters_response_200_counters_item = cls(
            graceful_restart=graceful_restart,
            local_as_number=local_as_number,
            local_ip_address=local_ip_address,
            local_router_id=local_router_id,
            peer_router_id=peer_router_id,
            up_time=up_time,
        )

        get_v1_device_routing_bgp_nbrs_counters_response_200_counters_item.additional_properties = d
        return get_v1_device_routing_bgp_nbrs_counters_response_200_counters_item

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
