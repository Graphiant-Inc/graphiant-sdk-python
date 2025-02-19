from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item import (
        GetV1EdgesHardwareUnassignedResponse200InventoryItem,
    )


T = TypeVar("T", bound="GetV1EdgesHardwareUnassignedResponse200")


@_attrs_define
class GetV1EdgesHardwareUnassignedResponse200:
    """
    Attributes:
        inventory (Union[Unset, list['GetV1EdgesHardwareUnassignedResponse200InventoryItem']]):
        is_new_count (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    inventory: Union[Unset, list["GetV1EdgesHardwareUnassignedResponse200InventoryItem"]] = UNSET
    is_new_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)

        is_new_count = self.is_new_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if is_new_count is not UNSET:
            field_dict["isNewCount"] = is_new_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item import (
            GetV1EdgesHardwareUnassignedResponse200InventoryItem,
        )

        d = src_dict.copy()
        inventory = []
        _inventory = d.pop("inventory", UNSET)
        for inventory_item_data in _inventory or []:
            inventory_item = GetV1EdgesHardwareUnassignedResponse200InventoryItem.from_dict(inventory_item_data)

            inventory.append(inventory_item)

        is_new_count = d.pop("isNewCount", UNSET)

        get_v1_edges_hardware_unassigned_response_200 = cls(
            inventory=inventory,
            is_new_count=is_new_count,
        )

        get_v1_edges_hardware_unassigned_response_200.additional_properties = d
        return get_v1_edges_hardware_unassigned_response_200

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
