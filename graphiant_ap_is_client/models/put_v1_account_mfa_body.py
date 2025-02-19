from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1AccountMfaBody")


@_attrs_define
class PutV1AccountMfaBody:
    """
    Attributes:
        phone_number (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    phone_number: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        phone_number = d.pop("phoneNumber", UNSET)

        type_ = d.pop("type", UNSET)

        put_v1_account_mfa_body = cls(
            phone_number=phone_number,
            type_=type_,
        )

        put_v1_account_mfa_body.additional_properties = d
        return put_v1_account_mfa_body

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
