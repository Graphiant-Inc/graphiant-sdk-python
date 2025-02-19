from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_interfaces_item_value_interface import (
        PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValue:
    """
    Attributes:
        interface (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface]):
    """

    interface: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_interfaces_item_value_interface import (
            PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface,
        )

        d = src_dict.copy()
        _interface = d.pop("interface", UNSET)
        interface: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface]
        if isinstance(_interface, Unset):
            interface = UNSET
        else:
            interface = PutV1DevicesDeviceIdConfigBodyEdgeInterfacesItemValueInterface.from_dict(_interface)

        put_v1_devices_device_id_config_body_edge_interfaces_item_value = cls(
            interface=interface,
        )

        put_v1_devices_device_id_config_body_edge_interfaces_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_interfaces_item_value

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
