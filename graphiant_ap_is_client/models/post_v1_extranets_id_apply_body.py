from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsIdApplyBody")


@_attrs_define
class PostV1ExtranetsIdApplyBody:
    """
    Attributes:
        target_devices (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    target_devices: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.target_devices, Unset):
            target_devices = self.target_devices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_devices is not UNSET:
            field_dict["targetDevices"] = target_devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        target_devices = cast(list[str], d.pop("targetDevices", UNSET))

        post_v1_extranets_id_apply_body = cls(
            target_devices=target_devices,
        )

        post_v1_extranets_id_apply_body.additional_properties = d
        return post_v1_extranets_id_apply_body

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
