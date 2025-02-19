from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticPacketcaptureStartBodyTarget")


@_attrs_define
class PostV1DiagnosticPacketcaptureStartBodyTarget:
    """
    Attributes:
        interface (Union[Unset, str]):  Example: ethernet1/0.
        vrf_name (Union[Unset, str]):  Example: isp-red.
    """

    interface: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        interface = d.pop("interface", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        post_v1_diagnostic_packetcapture_start_body_target = cls(
            interface=interface,
            vrf_name=vrf_name,
        )

        post_v1_diagnostic_packetcapture_start_body_target.additional_properties = d
        return post_v1_diagnostic_packetcapture_start_body_target

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
