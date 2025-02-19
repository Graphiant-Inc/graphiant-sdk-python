from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesInventoryRequestReturnBody")


@_attrs_define
class PostV1DevicesInventoryRequestReturnBody:
    """
    Attributes:
        device_serials (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    device_serials: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_serials: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_serials, Unset):
            device_serials = self.device_serials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_serials is not UNSET:
            field_dict["deviceSerials"] = device_serials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_serials = cast(list[str], d.pop("deviceSerials", UNSET))

        post_v1_devices_inventory_request_return_body = cls(
            device_serials=device_serials,
        )

        post_v1_devices_inventory_request_return_body.additional_properties = d
        return post_v1_devices_inventory_request_return_body

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
