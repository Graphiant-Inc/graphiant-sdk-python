from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_portal_private_sync_body_inventory_item import PostV1PortalPrivateSyncBodyInventoryItem


T = TypeVar("T", bound="PostV1PortalPrivateSyncBody")


@_attrs_define
class PostV1PortalPrivateSyncBody:
    """
    Attributes:
        gcs_name (Union[Unset, str]):  Example: TYPE_STRING.
        inventory (Union[Unset, list['PostV1PortalPrivateSyncBodyInventoryItem']]):
        is_full_sync (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    gcs_name: Union[Unset, str] = UNSET
    inventory: Union[Unset, list["PostV1PortalPrivateSyncBodyInventoryItem"]] = UNSET
    is_full_sync: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gcs_name = self.gcs_name

        inventory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)

        is_full_sync = self.is_full_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gcs_name is not UNSET:
            field_dict["gcsName"] = gcs_name
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if is_full_sync is not UNSET:
            field_dict["isFullSync"] = is_full_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_portal_private_sync_body_inventory_item import PostV1PortalPrivateSyncBodyInventoryItem

        d = src_dict.copy()
        gcs_name = d.pop("gcsName", UNSET)

        inventory = []
        _inventory = d.pop("inventory", UNSET)
        for inventory_item_data in _inventory or []:
            inventory_item = PostV1PortalPrivateSyncBodyInventoryItem.from_dict(inventory_item_data)

            inventory.append(inventory_item)

        is_full_sync = d.pop("isFullSync", UNSET)

        post_v1_portal_private_sync_body = cls(
            gcs_name=gcs_name,
            inventory=inventory,
            is_full_sync=is_full_sync,
        )

        post_v1_portal_private_sync_body.additional_properties = d
        return post_v1_portal_private_sync_body

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
