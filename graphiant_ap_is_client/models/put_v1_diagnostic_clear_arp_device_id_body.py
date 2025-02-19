from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_diagnostic_clear_arp_device_id_body_entry_item import (
        PutV1DiagnosticClearArpDeviceIdBodyEntryItem,
    )


T = TypeVar("T", bound="PutV1DiagnosticClearArpDeviceIdBody")


@_attrs_define
class PutV1DiagnosticClearArpDeviceIdBody:
    """
    Attributes:
        entry (Union[Unset, list['PutV1DiagnosticClearArpDeviceIdBodyEntryItem']]):
    """

    entry: Union[Unset, list["PutV1DiagnosticClearArpDeviceIdBodyEntryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = []
            for entry_item_data in self.entry:
                entry_item = entry_item_data.to_dict()
                entry.append(entry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_diagnostic_clear_arp_device_id_body_entry_item import (
            PutV1DiagnosticClearArpDeviceIdBodyEntryItem,
        )

        d = src_dict.copy()
        entry = []
        _entry = d.pop("entry", UNSET)
        for entry_item_data in _entry or []:
            entry_item = PutV1DiagnosticClearArpDeviceIdBodyEntryItem.from_dict(entry_item_data)

            entry.append(entry_item)

        put_v1_diagnostic_clear_arp_device_id_body = cls(
            entry=entry,
        )

        put_v1_diagnostic_clear_arp_device_id_body.additional_properties = d
        return put_v1_diagnostic_clear_arp_device_id_body

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
