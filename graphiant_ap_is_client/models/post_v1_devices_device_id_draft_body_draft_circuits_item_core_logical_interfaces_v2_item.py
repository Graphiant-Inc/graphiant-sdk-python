from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item:
    """
    Attributes:
        admin_status (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        index (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        oper_status (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    admin_status: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    oper_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_status = self.admin_status

        id = self.id

        index = self.index

        name = self.name

        oper_status = self.oper_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_status is not UNSET:
            field_dict["adminStatus"] = admin_status
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if oper_status is not UNSET:
            field_dict["operStatus"] = oper_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_status = d.pop("adminStatus", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        oper_status = d.pop("operStatus", UNSET)

        post_v1_devices_device_id_draft_body_draft_circuits_item_core_logical_interfaces_v2_item = cls(
            admin_status=admin_status,
            id=id,
            index=index,
            name=name,
            oper_status=oper_status,
        )

        post_v1_devices_device_id_draft_body_draft_circuits_item_core_logical_interfaces_v2_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_circuits_item_core_logical_interfaces_v2_item

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
