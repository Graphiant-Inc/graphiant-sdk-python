from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_arp_response_200_arp_entry_item import (
        GetV1DevicesDeviceIdArpResponse200ArpEntryItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdArpResponse200")


@_attrs_define
class GetV1DevicesDeviceIdArpResponse200:
    """
    Attributes:
        arp_entry (Union[Unset, list['GetV1DevicesDeviceIdArpResponse200ArpEntryItem']]):
    """

    arp_entry: Union[Unset, list["GetV1DevicesDeviceIdArpResponse200ArpEntryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arp_entry: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.arp_entry, Unset):
            arp_entry = []
            for arp_entry_item_data in self.arp_entry:
                arp_entry_item = arp_entry_item_data.to_dict()
                arp_entry.append(arp_entry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arp_entry is not UNSET:
            field_dict["arpEntry"] = arp_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_arp_response_200_arp_entry_item import (
            GetV1DevicesDeviceIdArpResponse200ArpEntryItem,
        )

        d = src_dict.copy()
        arp_entry = []
        _arp_entry = d.pop("arpEntry", UNSET)
        for arp_entry_item_data in _arp_entry or []:
            arp_entry_item = GetV1DevicesDeviceIdArpResponse200ArpEntryItem.from_dict(arp_entry_item_data)

            arp_entry.append(arp_entry_item)

        get_v1_devices_device_id_arp_response_200 = cls(
            arp_entry=arp_entry,
        )

        get_v1_devices_device_id_arp_response_200.additional_properties = d
        return get_v1_devices_device_id_arp_response_200

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
