from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesInventoryResponse200DataItem")


@_attrs_define
class PostV1DevicesInventoryResponse200DataItem:
    """
    Attributes:
        device_serial (Union[Unset, str]):  Example: TYPE_STRING.
        uuid (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_serial: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_serial = self.device_serial

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_serial is not UNSET:
            field_dict["deviceSerial"] = device_serial
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_serial = d.pop("deviceSerial", UNSET)

        uuid = d.pop("uuid", UNSET)

        post_v1_devices_inventory_response_200_data_item = cls(
            device_serial=device_serial,
            uuid=uuid,
        )

        post_v1_devices_inventory_response_200_data_item.additional_properties = d
        return post_v1_devices_inventory_response_200_data_item

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
