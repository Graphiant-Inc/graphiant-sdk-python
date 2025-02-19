from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_packetcapture_start_body_filter_destination import (
        PostV1DiagnosticPacketcaptureStartBodyFilterDestination,
    )
    from ..models.post_v1_diagnostic_packetcapture_start_body_filter_source import (
        PostV1DiagnosticPacketcaptureStartBodyFilterSource,
    )


T = TypeVar("T", bound="PostV1DiagnosticPacketcaptureStartBodyFilter")


@_attrs_define
class PostV1DiagnosticPacketcaptureStartBodyFilter:
    """
    Attributes:
        destination (Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilterDestination]):
        dscp (Union[Unset, str]):  Example: 80.
        protocol (Union[Unset, str]):  Example: Tcp.
        source (Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilterSource]):
    """

    destination: Union[Unset, "PostV1DiagnosticPacketcaptureStartBodyFilterDestination"] = UNSET
    dscp: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    source: Union[Unset, "PostV1DiagnosticPacketcaptureStartBodyFilterSource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dscp = self.dscp

        protocol = self.protocol

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dscp is not UNSET:
            field_dict["dscp"] = dscp
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_packetcapture_start_body_filter_destination import (
            PostV1DiagnosticPacketcaptureStartBodyFilterDestination,
        )
        from ..models.post_v1_diagnostic_packetcapture_start_body_filter_source import (
            PostV1DiagnosticPacketcaptureStartBodyFilterSource,
        )

        d = src_dict.copy()
        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilterDestination]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = PostV1DiagnosticPacketcaptureStartBodyFilterDestination.from_dict(_destination)

        dscp = d.pop("dscp", UNSET)

        protocol = d.pop("protocol", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilterSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PostV1DiagnosticPacketcaptureStartBodyFilterSource.from_dict(_source)

        post_v1_diagnostic_packetcapture_start_body_filter = cls(
            destination=destination,
            dscp=dscp,
            protocol=protocol,
            source=source,
        )

        post_v1_diagnostic_packetcapture_start_body_filter.additional_properties = d
        return post_v1_diagnostic_packetcapture_start_body_filter

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
