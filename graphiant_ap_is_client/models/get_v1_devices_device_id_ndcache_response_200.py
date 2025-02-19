from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_ndcache_response_200_nd_entry_item import (
        GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdNdcacheResponse200")


@_attrs_define
class GetV1DevicesDeviceIdNdcacheResponse200:
    """
    Attributes:
        nd_entry (Union[Unset, list['GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem']]):
    """

    nd_entry: Union[Unset, list["GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nd_entry: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nd_entry, Unset):
            nd_entry = []
            for nd_entry_item_data in self.nd_entry:
                nd_entry_item = nd_entry_item_data.to_dict()
                nd_entry.append(nd_entry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nd_entry is not UNSET:
            field_dict["ndEntry"] = nd_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_ndcache_response_200_nd_entry_item import (
            GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem,
        )

        d = src_dict.copy()
        nd_entry = []
        _nd_entry = d.pop("ndEntry", UNSET)
        for nd_entry_item_data in _nd_entry or []:
            nd_entry_item = GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem.from_dict(nd_entry_item_data)

            nd_entry.append(nd_entry_item)

        get_v1_devices_device_id_ndcache_response_200 = cls(
            nd_entry=nd_entry,
        )

        get_v1_devices_device_id_ndcache_response_200.additional_properties = d
        return get_v1_devices_device_id_ndcache_response_200

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
