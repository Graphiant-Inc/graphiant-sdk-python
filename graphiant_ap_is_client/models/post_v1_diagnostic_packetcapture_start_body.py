from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_packetcapture_start_body_filter import PostV1DiagnosticPacketcaptureStartBodyFilter
    from ..models.post_v1_diagnostic_packetcapture_start_body_target import PostV1DiagnosticPacketcaptureStartBodyTarget


T = TypeVar("T", bound="PostV1DiagnosticPacketcaptureStartBody")


@_attrs_define
class PostV1DiagnosticPacketcaptureStartBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: 30000000555.
        duration (Union[Unset, str]):  Example: 30.
        filter_ (Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilter]):
        max_packet_counter (Union[Unset, str]):  Example: 300.
        target (Union[Unset, PostV1DiagnosticPacketcaptureStartBodyTarget]):
    """

    device_id: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    filter_: Union[Unset, "PostV1DiagnosticPacketcaptureStartBodyFilter"] = UNSET
    max_packet_counter: Union[Unset, str] = UNSET
    target: Union[Unset, "PostV1DiagnosticPacketcaptureStartBodyTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        duration = self.duration

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        max_packet_counter = self.max_packet_counter

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if max_packet_counter is not UNSET:
            field_dict["maxPacketCounter"] = max_packet_counter
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_packetcapture_start_body_filter import (
            PostV1DiagnosticPacketcaptureStartBodyFilter,
        )
        from ..models.post_v1_diagnostic_packetcapture_start_body_target import (
            PostV1DiagnosticPacketcaptureStartBodyTarget,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        duration = d.pop("duration", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV1DiagnosticPacketcaptureStartBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV1DiagnosticPacketcaptureStartBodyFilter.from_dict(_filter_)

        max_packet_counter = d.pop("maxPacketCounter", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PostV1DiagnosticPacketcaptureStartBodyTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PostV1DiagnosticPacketcaptureStartBodyTarget.from_dict(_target)

        post_v1_diagnostic_packetcapture_start_body = cls(
            device_id=device_id,
            duration=duration,
            filter_=filter_,
            max_packet_counter=max_packet_counter,
            target=target,
        )

        post_v1_diagnostic_packetcapture_start_body.additional_properties = d
        return post_v1_diagnostic_packetcapture_start_body

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
