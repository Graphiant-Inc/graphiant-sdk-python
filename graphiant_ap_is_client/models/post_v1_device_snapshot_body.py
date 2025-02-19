from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DeviceSnapshotBody")


@_attrs_define
class PostV1DeviceSnapshotBody:
    """
    Attributes:
        category (Union[Unset, str]):  Example: TYPE_ENUM.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        golden (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    category: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    golden: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        device_id = self.device_id

        golden = self.golden

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if golden is not UNSET:
            field_dict["golden"] = golden
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        device_id = d.pop("deviceId", UNSET)

        golden = d.pop("golden", UNSET)

        name = d.pop("name", UNSET)

        post_v1_device_snapshot_body = cls(
            category=category,
            device_id=device_id,
            golden=golden,
            name=name,
        )

        post_v1_device_snapshot_body.additional_properties = d
        return post_v1_device_snapshot_body

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
