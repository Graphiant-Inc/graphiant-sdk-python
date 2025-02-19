from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1EnterprisesBody")


@_attrs_define
class PatchV1EnterprisesBody:
    """
    Attributes:
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        company_name (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        impersonation_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        portal_banner (Union[Unset, str]):  Example: TYPE_STRING.
    """

    admin_email: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    impersonation_enabled: Union[Unset, str] = UNSET
    portal_banner: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_email = self.admin_email

        company_name = self.company_name

        enterprise_id = self.enterprise_id

        impersonation_enabled = self.impersonation_enabled

        portal_banner = self.portal_banner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if impersonation_enabled is not UNSET:
            field_dict["impersonationEnabled"] = impersonation_enabled
        if portal_banner is not UNSET:
            field_dict["portalBanner"] = portal_banner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_email = d.pop("adminEmail", UNSET)

        company_name = d.pop("companyName", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        impersonation_enabled = d.pop("impersonationEnabled", UNSET)

        portal_banner = d.pop("portalBanner", UNSET)

        patch_v1_enterprises_body = cls(
            admin_email=admin_email,
            company_name=company_name,
            enterprise_id=enterprise_id,
            impersonation_enabled=impersonation_enabled,
            portal_banner=portal_banner,
        )

        patch_v1_enterprises_body.additional_properties = d
        return patch_v1_enterprises_body

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
