from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GroupsIdMembersResponse200UsersItem")


@_attrs_define
class GetV1GroupsIdMembersResponse200UsersItem:
    """
    Attributes:
        email (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        first_name (Union[Unset, str]):  Example: TYPE_STRING.
        last_name (Union[Unset, str]):  Example: TYPE_STRING.
        phone_number (Union[Unset, str]):  Example: TYPE_STRING.
        time_zone (Union[Unset, str]):  Example: TYPE_STRING.
        user_id (Union[Unset, str]):  Example: TYPE_STRING.
        verified (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    email: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    verified: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        enterprise_id = self.enterprise_id

        first_name = self.first_name

        last_name = self.last_name

        phone_number = self.phone_number

        time_zone = self.time_zone

        user_id = self.user_id

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        user_id = d.pop("userId", UNSET)

        verified = d.pop("verified", UNSET)

        get_v1_groups_id_members_response_200_users_item = cls(
            email=email,
            enterprise_id=enterprise_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            time_zone=time_zone,
            user_id=user_id,
            verified=verified,
        )

        get_v1_groups_id_members_response_200_users_item.additional_properties = d
        return get_v1_groups_id_members_response_200_users_item

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
