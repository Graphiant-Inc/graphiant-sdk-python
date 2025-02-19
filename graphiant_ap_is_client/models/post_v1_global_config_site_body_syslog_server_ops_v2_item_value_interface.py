from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalConfigSiteBodySyslogServerOpsV2ItemValueInterface")


@_attrs_define
class PostV1GlobalConfigSiteBodySyslogServerOpsV2ItemValueInterface:
    """
    Attributes:
        interface (Union[Unset, str]):  Example: TYPE_STRING.
    """

    interface: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        interface = d.pop("interface", UNSET)

        post_v1_global_config_site_body_syslog_server_ops_v2_item_value_interface = cls(
            interface=interface,
        )

        post_v1_global_config_site_body_syslog_server_ops_v2_item_value_interface.additional_properties = d
        return post_v1_global_config_site_body_syslog_server_ops_v2_item_value_interface

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
