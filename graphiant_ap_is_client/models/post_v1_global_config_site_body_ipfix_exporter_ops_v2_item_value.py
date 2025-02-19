from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_v2_item_value_interface import (
        PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface,
    )


T = TypeVar("T", bound="PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValue")


@_attrs_define
class PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValue:
    """
    Attributes:
        interface (Union[Unset, PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface]):
        operation (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    interface: Union[Unset, "PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface"] = UNSET
    operation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface.to_dict()

        operation = self.operation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_config_site_body_ipfix_exporter_ops_v2_item_value_interface import (
            PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface,
        )

        d = src_dict.copy()
        _interface = d.pop("interface", UNSET)
        interface: Union[Unset, PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface]
        if isinstance(_interface, Unset):
            interface = UNSET
        else:
            interface = PostV1GlobalConfigSiteBodyIpfixExporterOpsV2ItemValueInterface.from_dict(_interface)

        operation = d.pop("operation", UNSET)

        post_v1_global_config_site_body_ipfix_exporter_ops_v2_item_value = cls(
            interface=interface,
            operation=operation,
        )

        post_v1_global_config_site_body_ipfix_exporter_ops_v2_item_value.additional_properties = d
        return post_v1_global_config_site_body_ipfix_exporter_ops_v2_item_value

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
