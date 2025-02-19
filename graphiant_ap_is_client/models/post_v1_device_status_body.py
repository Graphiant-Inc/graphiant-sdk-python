from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DeviceStatusBody")


@_attrs_define
class PostV1DeviceStatusBody:
    """
    Attributes:
        device_ids (Union[Unset, list[str]]):  Example: ['TYPE_UINT64'].
        role (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_ids: Union[Unset, list[str]] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_ids is not UNSET:
            field_dict["deviceIds"] = device_ids
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_ids = cast(list[str], d.pop("deviceIds", UNSET))

        role = d.pop("role", UNSET)

        post_v1_device_status_body = cls(
            device_ids=device_ids,
            role=role,
        )

        post_v1_device_status_body.additional_properties = d
        return post_v1_device_status_body

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
