from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_ipfix_exporters_item_value_exporter import (
        PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValue:
    """
    Attributes:
        exporter (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter]):
    """

    exporter: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exporter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exporter, Unset):
            exporter = self.exporter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exporter is not UNSET:
            field_dict["exporter"] = exporter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_ipfix_exporters_item_value_exporter import (
            PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter,
        )

        d = src_dict.copy()
        _exporter = d.pop("exporter", UNSET)
        exporter: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter]
        if isinstance(_exporter, Unset):
            exporter = UNSET
        else:
            exporter = PutV1DevicesDeviceIdConfigBodyEdgeIpfixExportersItemValueExporter.from_dict(_exporter)

        put_v1_devices_device_id_config_body_edge_ipfix_exporters_item_value = cls(
            exporter=exporter,
        )

        put_v1_devices_device_id_config_body_edge_ipfix_exporters_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_ipfix_exporters_item_value

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
