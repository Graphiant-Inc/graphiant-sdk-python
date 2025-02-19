from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1GlobalConfigBodyIpfixExportersItemValueExporter")


@_attrs_define
class PatchV1GlobalConfigBodyIpfixExportersItemValueExporter:
    """
    Attributes:
        destination_address (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_global_sync (Union[Unset, str]):  Example: TYPE_BOOL.
        monitored_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        name (Union[Unset, str]):  Example: TYPE_STRING.
        sample_mode (Union[Unset, str]):  Example: TYPE_ENUM.
        sample_rate (Union[Unset, str]):  Example: TYPE_UINT32.
        source_interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    destination_address: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    is_global_sync: Union[Unset, str] = UNSET
    monitored_segments: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    sample_mode: Union[Unset, str] = UNSET
    sample_rate: Union[Unset, str] = UNSET
    source_interface_name: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_address = self.destination_address

        destination_port = self.destination_port

        global_id = self.global_id

        is_global_sync = self.is_global_sync

        monitored_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.monitored_segments, Unset):
            monitored_segments = self.monitored_segments

        name = self.name

        sample_mode = self.sample_mode

        sample_rate = self.sample_rate

        source_interface_name = self.source_interface_name

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if is_global_sync is not UNSET:
            field_dict["isGlobalSync"] = is_global_sync
        if monitored_segments is not UNSET:
            field_dict["monitoredSegments"] = monitored_segments
        if name is not UNSET:
            field_dict["name"] = name
        if sample_mode is not UNSET:
            field_dict["sampleMode"] = sample_mode
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if source_interface_name is not UNSET:
            field_dict["sourceInterfaceName"] = source_interface_name
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_address = d.pop("destinationAddress", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        global_id = d.pop("globalId", UNSET)

        is_global_sync = d.pop("isGlobalSync", UNSET)

        monitored_segments = cast(list[str], d.pop("monitoredSegments", UNSET))

        name = d.pop("name", UNSET)

        sample_mode = d.pop("sampleMode", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        source_interface_name = d.pop("sourceInterfaceName", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        patch_v1_global_config_body_ipfix_exporters_item_value_exporter = cls(
            destination_address=destination_address,
            destination_port=destination_port,
            global_id=global_id,
            is_global_sync=is_global_sync,
            monitored_segments=monitored_segments,
            name=name,
            sample_mode=sample_mode,
            sample_rate=sample_rate,
            source_interface_name=source_interface_name,
            vrf_id=vrf_id,
        )

        patch_v1_global_config_body_ipfix_exporters_item_value_exporter.additional_properties = d
        return patch_v1_global_config_body_ipfix_exporters_item_value_exporter

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
