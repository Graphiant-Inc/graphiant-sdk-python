from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_ipfix_device_response_200_exporters_item import (
        GetV1GlobalIpfixDeviceResponse200ExportersItem,
    )


T = TypeVar("T", bound="GetV1GlobalIpfixDeviceResponse200")


@_attrs_define
class GetV1GlobalIpfixDeviceResponse200:
    """
    Attributes:
        exporters (Union[Unset, list['GetV1GlobalIpfixDeviceResponse200ExportersItem']]):
    """

    exporters: Union[Unset, list["GetV1GlobalIpfixDeviceResponse200ExportersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exporters, Unset):
            exporters = []
            for exporters_item_data in self.exporters:
                exporters_item = exporters_item_data.to_dict()
                exporters.append(exporters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exporters is not UNSET:
            field_dict["exporters"] = exporters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_ipfix_device_response_200_exporters_item import (
            GetV1GlobalIpfixDeviceResponse200ExportersItem,
        )

        d = src_dict.copy()
        exporters = []
        _exporters = d.pop("exporters", UNSET)
        for exporters_item_data in _exporters or []:
            exporters_item = GetV1GlobalIpfixDeviceResponse200ExportersItem.from_dict(exporters_item_data)

            exporters.append(exporters_item)

        get_v1_global_ipfix_device_response_200 = cls(
            exporters=exporters,
        )

        get_v1_global_ipfix_device_response_200.additional_properties = d
        return get_v1_global_ipfix_device_response_200

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
