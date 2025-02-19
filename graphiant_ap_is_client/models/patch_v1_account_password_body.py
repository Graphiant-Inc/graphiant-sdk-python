from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1AccountPasswordBody")


@_attrs_define
class PatchV1AccountPasswordBody:
    """
    Attributes:
        old_password (Union[Unset, str]):  Example: TYPE_STRING.
        password (Union[Unset, str]):  Example: TYPE_STRING.
    """

    old_password: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_password = self.old_password

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        old_password = d.pop("oldPassword", UNSET)

        password = d.pop("password", UNSET)

        patch_v1_account_password_body = cls(
            old_password=old_password,
            password=password,
        )

        patch_v1_account_password_body.additional_properties = d
        return patch_v1_account_password_body

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
