from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyConfigurationMetadata")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyConfigurationMetadata:
    """
    Attributes:
        commit_confirm (Union[Unset, str]):  Example: TYPE_BOOL.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    commit_confirm: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_confirm = self.commit_confirm

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_confirm is not UNSET:
            field_dict["commitConfirm"] = commit_confirm
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        commit_confirm = d.pop("commitConfirm", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        put_v1_devices_device_id_config_body_configuration_metadata = cls(
            commit_confirm=commit_confirm,
            description=description,
            name=name,
        )

        put_v1_devices_device_id_config_body_configuration_metadata.additional_properties = d
        return put_v1_devices_device_id_config_body_configuration_metadata

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
