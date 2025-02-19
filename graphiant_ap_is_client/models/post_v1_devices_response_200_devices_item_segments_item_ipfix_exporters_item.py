from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesResponse200DevicesItemSegmentsItemIpfixExportersItem")


@_attrs_define
class PostV1DevicesResponse200DevicesItemSegmentsItemIpfixExportersItem:
    """
    Attributes:
        destination_address (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        monitored_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        name (Union[Unset, str]):  Example: TYPE_STRING.
        sample_mode (Union[Unset, str]):  Example: TYPE_STRING.
        sample_rate (Union[Unset, str]):  Example: TYPE_INT64.
        source_address (Union[Unset, str]):  Example: TYPE_STRING.
        source_interface (Union[Unset, str]):  Example: TYPE_STRING.
        source_segment (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    destination_address: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    monitored_segments: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    sample_mode: Union[Unset, str] = UNSET
    sample_rate: Union[Unset, str] = UNSET
    source_address: Union[Unset, str] = UNSET
    source_interface: Union[Unset, str] = UNSET
    source_segment: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_address = self.destination_address

        destination_port = self.destination_port

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        monitored_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.monitored_segments, Unset):
            monitored_segments = self.monitored_segments

        name = self.name

        sample_mode = self.sample_mode

        sample_rate = self.sample_rate

        source_address = self.source_address

        source_interface = self.source_interface

        source_segment = self.source_segment

        status = self.status

        vrf_id = self.vrf_id

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if monitored_segments is not UNSET:
            field_dict["monitoredSegments"] = monitored_segments
        if name is not UNSET:
            field_dict["name"] = name
        if sample_mode is not UNSET:
            field_dict["sampleMode"] = sample_mode
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if source_address is not UNSET:
            field_dict["sourceAddress"] = source_address
        if source_interface is not UNSET:
            field_dict["sourceInterface"] = source_interface
        if source_segment is not UNSET:
            field_dict["sourceSegment"] = source_segment
        if status is not UNSET:
            field_dict["status"] = status
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_address = d.pop("destinationAddress", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        monitored_segments = cast(list[str], d.pop("monitoredSegments", UNSET))

        name = d.pop("name", UNSET)

        sample_mode = d.pop("sampleMode", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        source_address = d.pop("sourceAddress", UNSET)

        source_interface = d.pop("sourceInterface", UNSET)

        source_segment = d.pop("sourceSegment", UNSET)

        status = d.pop("status", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        post_v1_devices_response_200_devices_item_segments_item_ipfix_exporters_item = cls(
            destination_address=destination_address,
            destination_port=destination_port,
            error_message=error_message,
            global_id=global_id,
            id=id,
            monitored_segments=monitored_segments,
            name=name,
            sample_mode=sample_mode,
            sample_rate=sample_rate,
            source_address=source_address,
            source_interface=source_interface,
            source_segment=source_segment,
            status=status,
            vrf_id=vrf_id,
            vrf_name=vrf_name,
        )

        post_v1_devices_response_200_devices_item_segments_item_ipfix_exporters_item.additional_properties = d
        return post_v1_devices_response_200_devices_item_segments_item_ipfix_exporters_item

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
