from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress")


@_attrs_define
class PutV1DiagnosticClearArpDeviceIdBodyEntryItemAddress:
    """
    Attributes:
        address (Union[Unset, list[str]]):  Example: ['1.1.1.1'].
    """

    address: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, list[str]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address = cast(list[str], d.pop("address", UNSET))

        put_v1_diagnostic_clear_arp_device_id_body_entry_item_address = cls(
            address=address,
        )

        put_v1_diagnostic_clear_arp_device_id_body_entry_item_address.additional_properties = d
        return put_v1_diagnostic_clear_arp_device_id_body_entry_item_address

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
