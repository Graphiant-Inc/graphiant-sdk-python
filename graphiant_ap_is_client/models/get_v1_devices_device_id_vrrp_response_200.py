from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_vrrp_response_200_vrrp_entry_item import (
        GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdVrrpResponse200")


@_attrs_define
class GetV1DevicesDeviceIdVrrpResponse200:
    """
    Attributes:
        vrrp_entry (Union[Unset, list['GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem']]):
    """

    vrrp_entry: Union[Unset, list["GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vrrp_entry: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrrp_entry, Unset):
            vrrp_entry = []
            for vrrp_entry_item_data in self.vrrp_entry:
                vrrp_entry_item = vrrp_entry_item_data.to_dict()
                vrrp_entry.append(vrrp_entry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vrrp_entry is not UNSET:
            field_dict["vrrpEntry"] = vrrp_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_vrrp_response_200_vrrp_entry_item import (
            GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem,
        )

        d = src_dict.copy()
        vrrp_entry = []
        _vrrp_entry = d.pop("vrrpEntry", UNSET)
        for vrrp_entry_item_data in _vrrp_entry or []:
            vrrp_entry_item = GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem.from_dict(vrrp_entry_item_data)

            vrrp_entry.append(vrrp_entry_item)

        get_v1_devices_device_id_vrrp_response_200 = cls(
            vrrp_entry=vrrp_entry,
        )

        get_v1_devices_device_id_vrrp_response_200.additional_properties = d
        return get_v1_devices_device_id_vrrp_response_200

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
