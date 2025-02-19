from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1GlobalConfigBodySyslogServersItemValueTarget")


@_attrs_define
class PatchV1GlobalConfigBodySyslogServersItemValueTarget:
    """
    Attributes:
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        host (Union[Unset, str]):  Example: TYPE_STRING.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        is_global_sync (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        port (Union[Unset, str]):  Example: TYPE_UINT32.
        severity (Union[Unset, str]):  Example: TYPE_ENUM.
        transport (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    enabled: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    is_global_sync: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    transport: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        global_id = self.global_id

        host = self.host

        interface_name = self.interface_name

        is_global_sync = self.is_global_sync

        name = self.name

        port = self.port

        severity = self.severity

        transport = self.transport

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if host is not UNSET:
            field_dict["host"] = host
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if is_global_sync is not UNSET:
            field_dict["isGlobalSync"] = is_global_sync
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if severity is not UNSET:
            field_dict["severity"] = severity
        if transport is not UNSET:
            field_dict["transport"] = transport
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        global_id = d.pop("globalId", UNSET)

        host = d.pop("host", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        is_global_sync = d.pop("isGlobalSync", UNSET)

        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        severity = d.pop("severity", UNSET)

        transport = d.pop("transport", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        patch_v1_global_config_body_syslog_servers_item_value_target = cls(
            enabled=enabled,
            global_id=global_id,
            host=host,
            interface_name=interface_name,
            is_global_sync=is_global_sync,
            name=name,
            port=port,
            severity=severity,
            transport=transport,
            vrf_id=vrf_id,
        )

        patch_v1_global_config_body_syslog_servers_item_value_target.additional_properties = d
        return patch_v1_global_config_body_syslog_servers_item_value_target

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
