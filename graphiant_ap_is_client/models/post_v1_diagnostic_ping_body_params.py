from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticPingBodyParams")


@_attrs_define
class PostV1DiagnosticPingBodyParams:
    """
    Attributes:
        dest_address (Union[Unset, str]):  Example: 172.1.1.1.
        hop_stats_count (Union[Unset, str]):  Example: 10.
        interface (Union[Unset, str]):  Example: ethernet1/0.
        payload_size (Union[Unset, str]):  Example: 64.
        port (Union[Unset, str]):  Example: 443.
        probe_count (Union[Unset, str]):  Example: 4.
        src_address (Union[Unset, str]):  Example: 10.1.1.1.
        tos (Union[Unset, str]):  Example: 0 - 7.
        vrf_name (Union[Unset, str]):  Example: finance.
    """

    dest_address: Union[Unset, str] = UNSET
    hop_stats_count: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    payload_size: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    probe_count: Union[Unset, str] = UNSET
    src_address: Union[Unset, str] = UNSET
    tos: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest_address = self.dest_address

        hop_stats_count = self.hop_stats_count

        interface = self.interface

        payload_size = self.payload_size

        port = self.port

        probe_count = self.probe_count

        src_address = self.src_address

        tos = self.tos

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest_address is not UNSET:
            field_dict["destAddress"] = dest_address
        if hop_stats_count is not UNSET:
            field_dict["hopStatsCount"] = hop_stats_count
        if interface is not UNSET:
            field_dict["interface"] = interface
        if payload_size is not UNSET:
            field_dict["payloadSize"] = payload_size
        if port is not UNSET:
            field_dict["port"] = port
        if probe_count is not UNSET:
            field_dict["probeCount"] = probe_count
        if src_address is not UNSET:
            field_dict["srcAddress"] = src_address
        if tos is not UNSET:
            field_dict["tos"] = tos
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dest_address = d.pop("destAddress", UNSET)

        hop_stats_count = d.pop("hopStatsCount", UNSET)

        interface = d.pop("interface", UNSET)

        payload_size = d.pop("payloadSize", UNSET)

        port = d.pop("port", UNSET)

        probe_count = d.pop("probeCount", UNSET)

        src_address = d.pop("srcAddress", UNSET)

        tos = d.pop("tos", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        post_v1_diagnostic_ping_body_params = cls(
            dest_address=dest_address,
            hop_stats_count=hop_stats_count,
            interface=interface,
            payload_size=payload_size,
            port=port,
            probe_count=probe_count,
            src_address=src_address,
            tos=tos,
            vrf_name=vrf_name,
        )

        post_v1_diagnostic_ping_body_params.additional_properties = d
        return post_v1_diagnostic_ping_body_params

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
