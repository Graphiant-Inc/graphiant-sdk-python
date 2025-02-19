from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AccountMfaConfirmationBody")


@_attrs_define
class PostV1AccountMfaConfirmationBody:
    """
    Attributes:
        code (Union[Unset, str]):  Example: TYPE_STRING.
        confirmed (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    code: Union[Unset, str] = UNSET
    confirmed: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        confirmed = self.confirmed

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        confirmed = d.pop("confirmed", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        post_v1_account_mfa_confirmation_body = cls(
            code=code,
            confirmed=confirmed,
            id=id,
            type_=type_,
        )

        post_v1_account_mfa_confirmation_body.additional_properties = d
        return post_v1_account_mfa_confirmation_body

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
