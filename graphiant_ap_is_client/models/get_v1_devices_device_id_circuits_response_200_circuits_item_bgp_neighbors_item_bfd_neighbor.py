from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor_last_updated import (
        GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated,
    )
    from ..models.get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor_time_in_state import (
        GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighbor")


@_attrs_define
class GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighbor:
    """
    Attributes:
        desired_minimum_tx_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        if_index (Union[Unset, str]):  Example: TYPE_UINT32.
        interface (Union[Unset, str]):  Example: TYPE_STRING.
        last_updated (Union[Unset,
            GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated]):
        local_diag (Union[Unset, str]):  Example: TYPE_ENUM.
        peer_address (Union[Unset, str]):  Example: TYPE_STRING.
        remote_diag (Union[Unset, str]):  Example: TYPE_ENUM.
        required_minimum_rx_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        segment_name (Union[Unset, str]):  Example: TYPE_STRING.
        source_address (Union[Unset, str]):  Example: TYPE_STRING.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        time_in_state (Union[Unset,
            GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState]):
        up (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    desired_minimum_tx_interval: Union[Unset, str] = UNSET
    if_index: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    last_updated: Union[
        Unset, "GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated"
    ] = UNSET
    local_diag: Union[Unset, str] = UNSET
    peer_address: Union[Unset, str] = UNSET
    remote_diag: Union[Unset, str] = UNSET
    required_minimum_rx_interval: Union[Unset, str] = UNSET
    segment_name: Union[Unset, str] = UNSET
    source_address: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    time_in_state: Union[
        Unset, "GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState"
    ] = UNSET
    up: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired_minimum_tx_interval = self.desired_minimum_tx_interval

        if_index = self.if_index

        interface = self.interface

        last_updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.to_dict()

        local_diag = self.local_diag

        peer_address = self.peer_address

        remote_diag = self.remote_diag

        required_minimum_rx_interval = self.required_minimum_rx_interval

        segment_name = self.segment_name

        source_address = self.source_address

        state = self.state

        time_in_state: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_in_state, Unset):
            time_in_state = self.time_in_state.to_dict()

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_minimum_tx_interval is not UNSET:
            field_dict["desiredMinimumTxInterval"] = desired_minimum_tx_interval
        if if_index is not UNSET:
            field_dict["ifIndex"] = if_index
        if interface is not UNSET:
            field_dict["interface"] = interface
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if local_diag is not UNSET:
            field_dict["localDiag"] = local_diag
        if peer_address is not UNSET:
            field_dict["peerAddress"] = peer_address
        if remote_diag is not UNSET:
            field_dict["remoteDiag"] = remote_diag
        if required_minimum_rx_interval is not UNSET:
            field_dict["requiredMinimumRxInterval"] = required_minimum_rx_interval
        if segment_name is not UNSET:
            field_dict["segmentName"] = segment_name
        if source_address is not UNSET:
            field_dict["sourceAddress"] = source_address
        if state is not UNSET:
            field_dict["state"] = state
        if time_in_state is not UNSET:
            field_dict["timeInState"] = time_in_state
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor_last_updated import (
            GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated,
        )
        from ..models.get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor_time_in_state import (
            GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState,
        )

        d = src_dict.copy()
        desired_minimum_tx_interval = d.pop("desiredMinimumTxInterval", UNSET)

        if_index = d.pop("ifIndex", UNSET)

        interface = d.pop("interface", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[
            Unset, GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated
        ]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = (
                GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborLastUpdated.from_dict(
                    _last_updated
                )
            )

        local_diag = d.pop("localDiag", UNSET)

        peer_address = d.pop("peerAddress", UNSET)

        remote_diag = d.pop("remoteDiag", UNSET)

        required_minimum_rx_interval = d.pop("requiredMinimumRxInterval", UNSET)

        segment_name = d.pop("segmentName", UNSET)

        source_address = d.pop("sourceAddress", UNSET)

        state = d.pop("state", UNSET)

        _time_in_state = d.pop("timeInState", UNSET)
        time_in_state: Union[
            Unset, GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState
        ]
        if isinstance(_time_in_state, Unset):
            time_in_state = UNSET
        else:
            time_in_state = (
                GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfdNeighborTimeInState.from_dict(
                    _time_in_state
                )
            )

        up = d.pop("up", UNSET)

        get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor = cls(
            desired_minimum_tx_interval=desired_minimum_tx_interval,
            if_index=if_index,
            interface=interface,
            last_updated=last_updated,
            local_diag=local_diag,
            peer_address=peer_address,
            remote_diag=remote_diag,
            required_minimum_rx_interval=required_minimum_rx_interval,
            segment_name=segment_name,
            source_address=source_address,
            state=state,
            time_in_state=time_in_state,
            up=up,
        )

        get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor.additional_properties = d
        return get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd_neighbor

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
