from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AccountMfaConfirmationResponse200")


@_attrs_define
class PostV1AccountMfaConfirmationResponse200:
    """
    Attributes:
        affected_users (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    affected_users: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_users, Unset):
            affected_users = self.affected_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_users is not UNSET:
            field_dict["affectedUsers"] = affected_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        affected_users = cast(list[str], d.pop("affectedUsers", UNSET))

        post_v1_account_mfa_confirmation_response_200 = cls(
            affected_users=affected_users,
        )

        post_v1_account_mfa_confirmation_response_200.additional_properties = d
        return post_v1_account_mfa_confirmation_response_200

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
