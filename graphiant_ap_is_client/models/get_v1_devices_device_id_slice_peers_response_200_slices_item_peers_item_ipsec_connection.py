from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_established_time import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime,
    )
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_local_interface import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface,
    )
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_rekey_time import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime,
    )
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_tunnel_interface import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection")


@_attrs_define
class GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection:
    """
    Attributes:
        anti_replay_w_size (Union[Unset, str]):  Example: TYPE_INT32.
        established_time (Union[Unset,
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime]):
        local_circuit (Union[Unset, str]):  Example: TYPE_STRING.
        local_interface (Union[Unset,
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface]):
        local_port (Union[Unset, str]):  Example: TYPE_INT32.
        local_spi (Union[Unset, str]):  Example: TYPE_INT64.
        negotiated_algorithms (Union[Unset, str]):  Example: TYPE_STRING.
        oper_state (Union[Unset, str]):  Example: TYPE_BOOL.
        peer_address (Union[Unset, str]):  Example: TYPE_STRING.
        protocol (Union[Unset, str]):  Example: TYPE_STRING.
        rekey_time (Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime]):
        remote_port (Union[Unset, str]):  Example: TYPE_INT32.
        remote_spi (Union[Unset, str]):  Example: TYPE_INT64.
        source_address (Union[Unset, str]):  Example: TYPE_STRING.
        tunnel_interface (Union[Unset,
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface]):
    """

    anti_replay_w_size: Union[Unset, str] = UNSET
    established_time: Union[
        Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime"
    ] = UNSET
    local_circuit: Union[Unset, str] = UNSET
    local_interface: Union[
        Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface"
    ] = UNSET
    local_port: Union[Unset, str] = UNSET
    local_spi: Union[Unset, str] = UNSET
    negotiated_algorithms: Union[Unset, str] = UNSET
    oper_state: Union[Unset, str] = UNSET
    peer_address: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    rekey_time: Union[Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime"] = (
        UNSET
    )
    remote_port: Union[Unset, str] = UNSET
    remote_spi: Union[Unset, str] = UNSET
    source_address: Union[Unset, str] = UNSET
    tunnel_interface: Union[
        Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anti_replay_w_size = self.anti_replay_w_size

        established_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.established_time, Unset):
            established_time = self.established_time.to_dict()

        local_circuit = self.local_circuit

        local_interface: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_interface, Unset):
            local_interface = self.local_interface.to_dict()

        local_port = self.local_port

        local_spi = self.local_spi

        negotiated_algorithms = self.negotiated_algorithms

        oper_state = self.oper_state

        peer_address = self.peer_address

        protocol = self.protocol

        rekey_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rekey_time, Unset):
            rekey_time = self.rekey_time.to_dict()

        remote_port = self.remote_port

        remote_spi = self.remote_spi

        source_address = self.source_address

        tunnel_interface: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tunnel_interface, Unset):
            tunnel_interface = self.tunnel_interface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anti_replay_w_size is not UNSET:
            field_dict["antiReplayWSize"] = anti_replay_w_size
        if established_time is not UNSET:
            field_dict["establishedTime"] = established_time
        if local_circuit is not UNSET:
            field_dict["localCircuit"] = local_circuit
        if local_interface is not UNSET:
            field_dict["localInterface"] = local_interface
        if local_port is not UNSET:
            field_dict["localPort"] = local_port
        if local_spi is not UNSET:
            field_dict["localSpi"] = local_spi
        if negotiated_algorithms is not UNSET:
            field_dict["negotiatedAlgorithms"] = negotiated_algorithms
        if oper_state is not UNSET:
            field_dict["operState"] = oper_state
        if peer_address is not UNSET:
            field_dict["peerAddress"] = peer_address
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if rekey_time is not UNSET:
            field_dict["rekeyTime"] = rekey_time
        if remote_port is not UNSET:
            field_dict["remotePort"] = remote_port
        if remote_spi is not UNSET:
            field_dict["remoteSpi"] = remote_spi
        if source_address is not UNSET:
            field_dict["sourceAddress"] = source_address
        if tunnel_interface is not UNSET:
            field_dict["tunnelInterface"] = tunnel_interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_established_time import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime,
        )
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_local_interface import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface,
        )
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_rekey_time import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime,
        )
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection_tunnel_interface import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface,
        )

        d = src_dict.copy()
        anti_replay_w_size = d.pop("antiReplayWSize", UNSET)

        _established_time = d.pop("establishedTime", UNSET)
        established_time: Union[
            Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime
        ]
        if isinstance(_established_time, Unset):
            established_time = UNSET
        else:
            established_time = (
                GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionEstablishedTime.from_dict(
                    _established_time
                )
            )

        local_circuit = d.pop("localCircuit", UNSET)

        _local_interface = d.pop("localInterface", UNSET)
        local_interface: Union[
            Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface
        ]
        if isinstance(_local_interface, Unset):
            local_interface = UNSET
        else:
            local_interface = (
                GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionLocalInterface.from_dict(
                    _local_interface
                )
            )

        local_port = d.pop("localPort", UNSET)

        local_spi = d.pop("localSpi", UNSET)

        negotiated_algorithms = d.pop("negotiatedAlgorithms", UNSET)

        oper_state = d.pop("operState", UNSET)

        peer_address = d.pop("peerAddress", UNSET)

        protocol = d.pop("protocol", UNSET)

        _rekey_time = d.pop("rekeyTime", UNSET)
        rekey_time: Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime]
        if isinstance(_rekey_time, Unset):
            rekey_time = UNSET
        else:
            rekey_time = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionRekeyTime.from_dict(
                _rekey_time
            )

        remote_port = d.pop("remotePort", UNSET)

        remote_spi = d.pop("remoteSpi", UNSET)

        source_address = d.pop("sourceAddress", UNSET)

        _tunnel_interface = d.pop("tunnelInterface", UNSET)
        tunnel_interface: Union[
            Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface
        ]
        if isinstance(_tunnel_interface, Unset):
            tunnel_interface = UNSET
        else:
            tunnel_interface = (
                GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnectionTunnelInterface.from_dict(
                    _tunnel_interface
                )
            )

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection = cls(
            anti_replay_w_size=anti_replay_w_size,
            established_time=established_time,
            local_circuit=local_circuit,
            local_interface=local_interface,
            local_port=local_port,
            local_spi=local_spi,
            negotiated_algorithms=negotiated_algorithms,
            oper_state=oper_state,
            peer_address=peer_address,
            protocol=protocol,
            rekey_time=rekey_time,
            remote_port=remote_port,
            remote_spi=remote_spi,
            source_address=source_address,
            tunnel_interface=tunnel_interface,
        )

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection.additional_properties = d
        return get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection

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
