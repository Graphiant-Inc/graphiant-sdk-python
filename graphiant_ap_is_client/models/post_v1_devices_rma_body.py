from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesRmaBody")


@_attrs_define
class PostV1DevicesRmaBody:
    """
    Attributes:
        current_device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        new_device_id (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    current_device_id: Union[Unset, str] = UNSET
    new_device_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_device_id = self.current_device_id

        new_device_id = self.new_device_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_device_id is not UNSET:
            field_dict["currentDeviceId"] = current_device_id
        if new_device_id is not UNSET:
            field_dict["newDeviceId"] = new_device_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        current_device_id = d.pop("currentDeviceId", UNSET)

        new_device_id = d.pop("newDeviceId", UNSET)

        post_v1_devices_rma_body = cls(
            current_device_id=current_device_id,
            new_device_id=new_device_id,
        )

        post_v1_devices_rma_body.additional_properties = d
        return post_v1_devices_rma_body

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
