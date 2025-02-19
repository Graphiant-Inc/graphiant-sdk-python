from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemSegmentsItemSyslogTargetsItem")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemSegmentsItemSyslogTargetsItem:
    """
    Attributes:
        destination_host (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        severity (Union[Unset, str]):  Example: TYPE_ENUM.
        source_interface (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        transport (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    destination_host: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    source_interface: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    transport: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_host = self.destination_host

        destination_port = self.destination_port

        enabled = self.enabled

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        name = self.name

        severity = self.severity

        source_interface = self.source_interface

        status = self.status

        transport = self.transport

        vrf_id = self.vrf_id

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_host is not UNSET:
            field_dict["destinationHost"] = destination_host
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if source_interface is not UNSET:
            field_dict["sourceInterface"] = source_interface
        if status is not UNSET:
            field_dict["status"] = status
        if transport is not UNSET:
            field_dict["transport"] = transport
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_host = d.pop("destinationHost", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        enabled = d.pop("enabled", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        severity = d.pop("severity", UNSET)

        source_interface = d.pop("sourceInterface", UNSET)

        status = d.pop("status", UNSET)

        transport = d.pop("transport", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_segments_item_syslog_targets_item = cls(
            destination_host=destination_host,
            destination_port=destination_port,
            enabled=enabled,
            error_message=error_message,
            global_id=global_id,
            id=id,
            name=name,
            severity=severity,
            source_interface=source_interface,
            status=status,
            transport=transport,
            vrf_id=vrf_id,
            vrf_name=vrf_name,
        )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_segments_item_syslog_targets_item.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200_devices_item_segments_item_syslog_targets_item

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
