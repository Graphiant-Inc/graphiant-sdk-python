from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1EnterprisesBody")


@_attrs_define
class PutV1EnterprisesBody:
    """
    Attributes:
        account_type (Union[Unset, str]):  Example: TYPE_ENUM.
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        admin_first_name (Union[Unset, str]):  Example: TYPE_STRING.
        admin_last_name (Union[Unset, str]):  Example: TYPE_STRING.
        admin_time_zone (Union[Unset, str]):  Example: TYPE_STRING.
        company_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    account_type: Union[Unset, str] = UNSET
    admin_email: Union[Unset, str] = UNSET
    admin_first_name: Union[Unset, str] = UNSET
    admin_last_name: Union[Unset, str] = UNSET
    admin_time_zone: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type = self.account_type

        admin_email = self.admin_email

        admin_first_name = self.admin_first_name

        admin_last_name = self.admin_last_name

        admin_time_zone = self.admin_time_zone

        company_name = self.company_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if admin_first_name is not UNSET:
            field_dict["adminFirstName"] = admin_first_name
        if admin_last_name is not UNSET:
            field_dict["adminLastName"] = admin_last_name
        if admin_time_zone is not UNSET:
            field_dict["adminTimeZone"] = admin_time_zone
        if company_name is not UNSET:
            field_dict["companyName"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        account_type = d.pop("accountType", UNSET)

        admin_email = d.pop("adminEmail", UNSET)

        admin_first_name = d.pop("adminFirstName", UNSET)

        admin_last_name = d.pop("adminLastName", UNSET)

        admin_time_zone = d.pop("adminTimeZone", UNSET)

        company_name = d.pop("companyName", UNSET)

        put_v1_enterprises_body = cls(
            account_type=account_type,
            admin_email=admin_email,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_time_zone=admin_time_zone,
            company_name=company_name,
        )

        put_v1_enterprises_body.additional_properties = d
        return put_v1_enterprises_body

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
