from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_inventory_body_hardware_inventory_list_item import (
        PostV1DevicesInventoryBodyHardwareInventoryListItem,
    )


T = TypeVar("T", bound="PostV1DevicesInventoryBody")


@_attrs_define
class PostV1DevicesInventoryBody:
    """
    Attributes:
        hardware_inventory_list (Union[Unset, list['PostV1DevicesInventoryBodyHardwareInventoryListItem']]):
    """

    hardware_inventory_list: Union[Unset, list["PostV1DevicesInventoryBodyHardwareInventoryListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_inventory_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hardware_inventory_list, Unset):
            hardware_inventory_list = []
            for hardware_inventory_list_item_data in self.hardware_inventory_list:
                hardware_inventory_list_item = hardware_inventory_list_item_data.to_dict()
                hardware_inventory_list.append(hardware_inventory_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hardware_inventory_list is not UNSET:
            field_dict["hardwareInventoryList"] = hardware_inventory_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_inventory_body_hardware_inventory_list_item import (
            PostV1DevicesInventoryBodyHardwareInventoryListItem,
        )

        d = src_dict.copy()
        hardware_inventory_list = []
        _hardware_inventory_list = d.pop("hardwareInventoryList", UNSET)
        for hardware_inventory_list_item_data in _hardware_inventory_list or []:
            hardware_inventory_list_item = PostV1DevicesInventoryBodyHardwareInventoryListItem.from_dict(
                hardware_inventory_list_item_data
            )

            hardware_inventory_list.append(hardware_inventory_list_item)

        post_v1_devices_inventory_body = cls(
            hardware_inventory_list=hardware_inventory_list,
        )

        post_v1_devices_inventory_body.additional_properties = d
        return post_v1_devices_inventory_body

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
