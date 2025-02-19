from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_diagnostic_clear_arp_device_id_body_entry_item_address import (
        PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress,
    )


T = TypeVar("T", bound="PutV1DiagnosticClearArpDeviceIdBodyEntryItem")


@_attrs_define
class PutV1DiagnosticClearArpDeviceIdBodyEntryItem:
    """
    Attributes:
        address (Union[Unset, PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress]):
        all_entry (Union[Unset, str]):  Example: true.
        interface_name (Union[Unset, str]):  Example: GigabitEthernet0/2.
    """

    address: Union[Unset, "PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress"] = UNSET
    all_entry: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        all_entry = self.all_entry

        interface_name = self.interface_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if all_entry is not UNSET:
            field_dict["allEntry"] = all_entry
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_diagnostic_clear_arp_device_id_body_entry_item_address import (
            PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress.from_dict(_address)

        all_entry = d.pop("allEntry", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        put_v1_diagnostic_clear_arp_device_id_body_entry_item = cls(
            address=address,
            all_entry=all_entry,
            interface_name=interface_name,
        )

        put_v1_diagnostic_clear_arp_device_id_body_entry_item.additional_properties = d
        return put_v1_diagnostic_clear_arp_device_id_body_entry_item

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
