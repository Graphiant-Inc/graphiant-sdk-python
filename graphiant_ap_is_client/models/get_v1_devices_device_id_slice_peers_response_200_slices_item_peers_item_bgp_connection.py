from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection_time_since_last_oper_change import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection")


@_attrs_define
class GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection:
    """
    Attributes:
        local_address (Union[Unset, str]):  Example: TYPE_STRING.
        oper_status (Union[Unset, str]):  Example: TYPE_BOOL.
        remote_address (Union[Unset, str]):  Example: TYPE_STRING.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        time_since_last_oper_change (Union[Unset,
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange]):
        up (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    local_address: Union[Unset, str] = UNSET
    oper_status: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    time_since_last_oper_change: Union[
        Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange"
    ] = UNSET
    up: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_address = self.local_address

        oper_status = self.oper_status

        remote_address = self.remote_address

        state = self.state

        time_since_last_oper_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_since_last_oper_change, Unset):
            time_since_last_oper_change = self.time_since_last_oper_change.to_dict()

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_address is not UNSET:
            field_dict["localAddress"] = local_address
        if oper_status is not UNSET:
            field_dict["operStatus"] = oper_status
        if remote_address is not UNSET:
            field_dict["remoteAddress"] = remote_address
        if state is not UNSET:
            field_dict["state"] = state
        if time_since_last_oper_change is not UNSET:
            field_dict["timeSinceLastOperChange"] = time_since_last_oper_change
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection_time_since_last_oper_change import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange,
        )

        d = src_dict.copy()
        local_address = d.pop("localAddress", UNSET)

        oper_status = d.pop("operStatus", UNSET)

        remote_address = d.pop("remoteAddress", UNSET)

        state = d.pop("state", UNSET)

        _time_since_last_oper_change = d.pop("timeSinceLastOperChange", UNSET)
        time_since_last_oper_change: Union[
            Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange
        ]
        if isinstance(_time_since_last_oper_change, Unset):
            time_since_last_oper_change = UNSET
        else:
            time_since_last_oper_change = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnectionTimeSinceLastOperChange.from_dict(
                _time_since_last_oper_change
            )

        up = d.pop("up", UNSET)

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection = cls(
            local_address=local_address,
            oper_status=oper_status,
            remote_address=remote_address,
            state=state,
            time_since_last_oper_change=time_since_last_oper_change,
            up=up,
        )

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection.additional_properties = d
        return get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection

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
