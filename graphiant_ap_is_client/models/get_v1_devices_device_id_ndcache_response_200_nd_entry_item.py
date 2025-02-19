from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem")


@_attrs_define
class GetV1DevicesDeviceIdNdcacheResponse200NdEntryItem:
    """
    Attributes:
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        ipv_6_address (Union[Unset, str]):  Example: TYPE_STRING.
        mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    interface_name: Union[Unset, str] = UNSET
    ipv_6_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_name = self.interface_name

        ipv_6_address = self.ipv_6_address

        mac_address = self.mac_address

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if ipv_6_address is not UNSET:
            field_dict["ipv6Address"] = ipv_6_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        interface_name = d.pop("interfaceName", UNSET)

        ipv_6_address = d.pop("ipv6Address", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        name = d.pop("name", UNSET)

        get_v1_devices_device_id_ndcache_response_200_nd_entry_item = cls(
            interface_name=interface_name,
            ipv_6_address=ipv_6_address,
            mac_address=mac_address,
            name=name,
        )

        get_v1_devices_device_id_ndcache_response_200_nd_entry_item.additional_properties = d
        return get_v1_devices_device_id_ndcache_response_200_nd_entry_item

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
