from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticPacketcaptureStartBodyFilterSource")


@_attrs_define
class PostV1DiagnosticPacketcaptureStartBodyFilterSource:
    """
    Attributes:
        port (Union[Unset, str]):  Example: 80.
        prefix (Union[Unset, str]):  Example: 1.1.1.0/24.
    """

    port: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        port = d.pop("port", UNSET)

        prefix = d.pop("prefix", UNSET)

        post_v1_diagnostic_packetcapture_start_body_filter_source = cls(
            port=port,
            prefix=prefix,
        )

        post_v1_diagnostic_packetcapture_start_body_filter_source.additional_properties = d
        return post_v1_diagnostic_packetcapture_start_body_filter_source

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
