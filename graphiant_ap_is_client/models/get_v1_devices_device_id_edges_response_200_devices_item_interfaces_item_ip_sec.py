from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec_established_time import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec:
    """
    Attributes:
        anti_replay_window_size (Union[Unset, str]):  Example: TYPE_UINT32.
        dh_group (Union[Unset, str]):  Example: TYPE_ENUM.
        dpd_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        encryption_alg (Union[Unset, str]):  Example: TYPE_ENUM.
        esn (Union[Unset, str]):  Example: TYPE_BOOL.
        established_time (Union[Unset,
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime]):
        ike_integrity (Union[Unset, str]):  Example: TYPE_ENUM.
        ipsec_encryption_alg (Union[Unset, str]):  Example: TYPE_ENUM.
        ipsec_integrity (Union[Unset, str]):  Example: TYPE_ENUM.
        label (Union[Unset, str]):  Example: TYPE_ENUM.
        local_address (Union[Unset, str]):  Example: TYPE_STRING.
        local_circuit (Union[Unset, str]):  Example: TYPE_STRING.
        local_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        local_ikesa_spi (Union[Unset, str]):  Example: TYPE_UINT64.
        local_port (Union[Unset, str]):  Example: TYPE_UINT32.
        negotiated_algo (Union[Unset, str]):  Example: TYPE_STRING.
        oper_state (Union[Unset, str]):  Example: TYPE_BOOL.
        perfect_forward_secrecy (Union[Unset, str]):  Example: TYPE_STRING.
        preshared_key (Union[Unset, str]):  Example: TYPE_STRING.
        protocol (Union[Unset, str]):  Example: TYPE_STRING.
        reauth_interval (Union[Unset, str]):  Example: TYPE_INT64.
        rekey_interval (Union[Unset, str]):  Example: TYPE_INT64.
        remote_address (Union[Unset, str]):  Example: TYPE_STRING.
        remote_ike_peer_identity (Union[Unset, str]):  Example: TYPE_STRING.
        remote_ikesa_spi (Union[Unset, str]):  Example: TYPE_UINT64.
        remote_port (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    anti_replay_window_size: Union[Unset, str] = UNSET
    dh_group: Union[Unset, str] = UNSET
    dpd_interval: Union[Unset, str] = UNSET
    encryption_alg: Union[Unset, str] = UNSET
    esn: Union[Unset, str] = UNSET
    established_time: Union[
        Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime"
    ] = UNSET
    ike_integrity: Union[Unset, str] = UNSET
    ipsec_encryption_alg: Union[Unset, str] = UNSET
    ipsec_integrity: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    local_address: Union[Unset, str] = UNSET
    local_circuit: Union[Unset, str] = UNSET
    local_ike_peer_identity: Union[Unset, str] = UNSET
    local_ikesa_spi: Union[Unset, str] = UNSET
    local_port: Union[Unset, str] = UNSET
    negotiated_algo: Union[Unset, str] = UNSET
    oper_state: Union[Unset, str] = UNSET
    perfect_forward_secrecy: Union[Unset, str] = UNSET
    preshared_key: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    reauth_interval: Union[Unset, str] = UNSET
    rekey_interval: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    remote_ike_peer_identity: Union[Unset, str] = UNSET
    remote_ikesa_spi: Union[Unset, str] = UNSET
    remote_port: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anti_replay_window_size = self.anti_replay_window_size

        dh_group = self.dh_group

        dpd_interval = self.dpd_interval

        encryption_alg = self.encryption_alg

        esn = self.esn

        established_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.established_time, Unset):
            established_time = self.established_time.to_dict()

        ike_integrity = self.ike_integrity

        ipsec_encryption_alg = self.ipsec_encryption_alg

        ipsec_integrity = self.ipsec_integrity

        label = self.label

        local_address = self.local_address

        local_circuit = self.local_circuit

        local_ike_peer_identity = self.local_ike_peer_identity

        local_ikesa_spi = self.local_ikesa_spi

        local_port = self.local_port

        negotiated_algo = self.negotiated_algo

        oper_state = self.oper_state

        perfect_forward_secrecy = self.perfect_forward_secrecy

        preshared_key = self.preshared_key

        protocol = self.protocol

        reauth_interval = self.reauth_interval

        rekey_interval = self.rekey_interval

        remote_address = self.remote_address

        remote_ike_peer_identity = self.remote_ike_peer_identity

        remote_ikesa_spi = self.remote_ikesa_spi

        remote_port = self.remote_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anti_replay_window_size is not UNSET:
            field_dict["antiReplayWindowSize"] = anti_replay_window_size
        if dh_group is not UNSET:
            field_dict["dhGroup"] = dh_group
        if dpd_interval is not UNSET:
            field_dict["dpdInterval"] = dpd_interval
        if encryption_alg is not UNSET:
            field_dict["encryptionAlg"] = encryption_alg
        if esn is not UNSET:
            field_dict["esn"] = esn
        if established_time is not UNSET:
            field_dict["establishedTime"] = established_time
        if ike_integrity is not UNSET:
            field_dict["ikeIntegrity"] = ike_integrity
        if ipsec_encryption_alg is not UNSET:
            field_dict["ipsecEncryptionAlg"] = ipsec_encryption_alg
        if ipsec_integrity is not UNSET:
            field_dict["ipsecIntegrity"] = ipsec_integrity
        if label is not UNSET:
            field_dict["label"] = label
        if local_address is not UNSET:
            field_dict["localAddress"] = local_address
        if local_circuit is not UNSET:
            field_dict["localCircuit"] = local_circuit
        if local_ike_peer_identity is not UNSET:
            field_dict["localIkePeerIdentity"] = local_ike_peer_identity
        if local_ikesa_spi is not UNSET:
            field_dict["localIkesaSpi"] = local_ikesa_spi
        if local_port is not UNSET:
            field_dict["localPort"] = local_port
        if negotiated_algo is not UNSET:
            field_dict["negotiatedAlgo"] = negotiated_algo
        if oper_state is not UNSET:
            field_dict["operState"] = oper_state
        if perfect_forward_secrecy is not UNSET:
            field_dict["perfectForwardSecrecy"] = perfect_forward_secrecy
        if preshared_key is not UNSET:
            field_dict["presharedKey"] = preshared_key
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if reauth_interval is not UNSET:
            field_dict["reauthInterval"] = reauth_interval
        if rekey_interval is not UNSET:
            field_dict["rekeyInterval"] = rekey_interval
        if remote_address is not UNSET:
            field_dict["remoteAddress"] = remote_address
        if remote_ike_peer_identity is not UNSET:
            field_dict["remoteIkePeerIdentity"] = remote_ike_peer_identity
        if remote_ikesa_spi is not UNSET:
            field_dict["remoteIkesaSpi"] = remote_ikesa_spi
        if remote_port is not UNSET:
            field_dict["remotePort"] = remote_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec_established_time import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime,
        )

        d = src_dict.copy()
        anti_replay_window_size = d.pop("antiReplayWindowSize", UNSET)

        dh_group = d.pop("dhGroup", UNSET)

        dpd_interval = d.pop("dpdInterval", UNSET)

        encryption_alg = d.pop("encryptionAlg", UNSET)

        esn = d.pop("esn", UNSET)

        _established_time = d.pop("establishedTime", UNSET)
        established_time: Union[
            Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime
        ]
        if isinstance(_established_time, Unset):
            established_time = UNSET
        else:
            established_time = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSecEstablishedTime.from_dict(
                    _established_time
                )
            )

        ike_integrity = d.pop("ikeIntegrity", UNSET)

        ipsec_encryption_alg = d.pop("ipsecEncryptionAlg", UNSET)

        ipsec_integrity = d.pop("ipsecIntegrity", UNSET)

        label = d.pop("label", UNSET)

        local_address = d.pop("localAddress", UNSET)

        local_circuit = d.pop("localCircuit", UNSET)

        local_ike_peer_identity = d.pop("localIkePeerIdentity", UNSET)

        local_ikesa_spi = d.pop("localIkesaSpi", UNSET)

        local_port = d.pop("localPort", UNSET)

        negotiated_algo = d.pop("negotiatedAlgo", UNSET)

        oper_state = d.pop("operState", UNSET)

        perfect_forward_secrecy = d.pop("perfectForwardSecrecy", UNSET)

        preshared_key = d.pop("presharedKey", UNSET)

        protocol = d.pop("protocol", UNSET)

        reauth_interval = d.pop("reauthInterval", UNSET)

        rekey_interval = d.pop("rekeyInterval", UNSET)

        remote_address = d.pop("remoteAddress", UNSET)

        remote_ike_peer_identity = d.pop("remoteIkePeerIdentity", UNSET)

        remote_ikesa_spi = d.pop("remoteIkesaSpi", UNSET)

        remote_port = d.pop("remotePort", UNSET)

        get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec = cls(
            anti_replay_window_size=anti_replay_window_size,
            dh_group=dh_group,
            dpd_interval=dpd_interval,
            encryption_alg=encryption_alg,
            esn=esn,
            established_time=established_time,
            ike_integrity=ike_integrity,
            ipsec_encryption_alg=ipsec_encryption_alg,
            ipsec_integrity=ipsec_integrity,
            label=label,
            local_address=local_address,
            local_circuit=local_circuit,
            local_ike_peer_identity=local_ike_peer_identity,
            local_ikesa_spi=local_ikesa_spi,
            local_port=local_port,
            negotiated_algo=negotiated_algo,
            oper_state=oper_state,
            perfect_forward_secrecy=perfect_forward_secrecy,
            preshared_key=preshared_key,
            protocol=protocol,
            reauth_interval=reauth_interval,
            rekey_interval=rekey_interval,
            remote_address=remote_address,
            remote_ike_peer_identity=remote_ike_peer_identity,
            remote_ikesa_spi=remote_ikesa_spi,
            remote_port=remote_port,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec

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
