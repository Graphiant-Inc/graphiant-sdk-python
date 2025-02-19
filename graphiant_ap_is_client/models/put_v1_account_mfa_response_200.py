from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1AccountMfaResponse200")


@_attrs_define
class PutV1AccountMfaResponse200:
    """
    Attributes:
        confirmed (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        qr_code (Union[Unset, str]):  Example: TYPE_STRING.
    """

    confirmed: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    qr_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmed = self.confirmed

        id = self.id

        qr_code = self.qr_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if id is not UNSET:
            field_dict["id"] = id
        if qr_code is not UNSET:
            field_dict["qrCode"] = qr_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        confirmed = d.pop("confirmed", UNSET)

        id = d.pop("id", UNSET)

        qr_code = d.pop("qrCode", UNSET)

        put_v1_account_mfa_response_200 = cls(
            confirmed=confirmed,
            id=id,
            qr_code=qr_code,
        )

        put_v1_account_mfa_response_200.additional_properties = d
        return put_v1_account_mfa_response_200

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
