from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprises_managed_response_200_enterprises_item_counts import (
        GetV1EnterprisesManagedResponse200EnterprisesItemCounts,
    )
    from ..models.get_v1_enterprises_managed_response_200_enterprises_item_customers_item import (
        GetV1EnterprisesManagedResponse200EnterprisesItemCustomersItem,
    )
    from ..models.get_v1_enterprises_managed_response_200_enterprises_item_eula_agreement_date import (
        GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate,
    )


T = TypeVar("T", bound="GetV1EnterprisesManagedResponse200EnterprisesItem")


@_attrs_define
class GetV1EnterprisesManagedResponse200EnterprisesItem:
    """
    Attributes:
        accept_eula (Union[Unset, str]):  Example: TYPE_BOOL.
        account_type (Union[Unset, str]):  Example: TYPE_ENUM.
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        company_name (Union[Unset, str]):  Example: TYPE_STRING.
        counts (Union[Unset, GetV1EnterprisesManagedResponse200EnterprisesItemCounts]):
        customers (Union[Unset, list['GetV1EnterprisesManagedResponse200EnterprisesItemCustomersItem']]):
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        eula_agreement_date (Union[Unset, GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate]):
        impersonation_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        parent_company_name (Union[Unset, str]):  Example: TYPE_STRING.
        parent_enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        portal_banner (Union[Unset, str]):  Example: TYPE_STRING.
    """

    accept_eula: Union[Unset, str] = UNSET
    account_type: Union[Unset, str] = UNSET
    admin_email: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    counts: Union[Unset, "GetV1EnterprisesManagedResponse200EnterprisesItemCounts"] = UNSET
    customers: Union[Unset, list["GetV1EnterprisesManagedResponse200EnterprisesItemCustomersItem"]] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    eula_agreement_date: Union[Unset, "GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate"] = UNSET
    impersonation_enabled: Union[Unset, str] = UNSET
    parent_company_name: Union[Unset, str] = UNSET
    parent_enterprise_id: Union[Unset, str] = UNSET
    portal_banner: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept_eula = self.accept_eula

        account_type = self.account_type

        admin_email = self.admin_email

        company_name = self.company_name

        counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        customers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        enterprise_id = self.enterprise_id

        eula_agreement_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.eula_agreement_date, Unset):
            eula_agreement_date = self.eula_agreement_date.to_dict()

        impersonation_enabled = self.impersonation_enabled

        parent_company_name = self.parent_company_name

        parent_enterprise_id = self.parent_enterprise_id

        portal_banner = self.portal_banner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept_eula is not UNSET:
            field_dict["acceptEula"] = accept_eula
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if counts is not UNSET:
            field_dict["counts"] = counts
        if customers is not UNSET:
            field_dict["customers"] = customers
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if eula_agreement_date is not UNSET:
            field_dict["eulaAgreementDate"] = eula_agreement_date
        if impersonation_enabled is not UNSET:
            field_dict["impersonationEnabled"] = impersonation_enabled
        if parent_company_name is not UNSET:
            field_dict["parentCompanyName"] = parent_company_name
        if parent_enterprise_id is not UNSET:
            field_dict["parentEnterpriseId"] = parent_enterprise_id
        if portal_banner is not UNSET:
            field_dict["portalBanner"] = portal_banner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprises_managed_response_200_enterprises_item_counts import (
            GetV1EnterprisesManagedResponse200EnterprisesItemCounts,
        )
        from ..models.get_v1_enterprises_managed_response_200_enterprises_item_customers_item import (
            GetV1EnterprisesManagedResponse200EnterprisesItemCustomersItem,
        )
        from ..models.get_v1_enterprises_managed_response_200_enterprises_item_eula_agreement_date import (
            GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate,
        )

        d = src_dict.copy()
        accept_eula = d.pop("acceptEula", UNSET)

        account_type = d.pop("accountType", UNSET)

        admin_email = d.pop("adminEmail", UNSET)

        company_name = d.pop("companyName", UNSET)

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, GetV1EnterprisesManagedResponse200EnterprisesItemCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = GetV1EnterprisesManagedResponse200EnterprisesItemCounts.from_dict(_counts)

        customers = []
        _customers = d.pop("customers", UNSET)
        for customers_item_data in _customers or []:
            customers_item = GetV1EnterprisesManagedResponse200EnterprisesItemCustomersItem.from_dict(
                customers_item_data
            )

            customers.append(customers_item)

        enterprise_id = d.pop("enterpriseId", UNSET)

        _eula_agreement_date = d.pop("eulaAgreementDate", UNSET)
        eula_agreement_date: Union[Unset, GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate]
        if isinstance(_eula_agreement_date, Unset):
            eula_agreement_date = UNSET
        else:
            eula_agreement_date = GetV1EnterprisesManagedResponse200EnterprisesItemEulaAgreementDate.from_dict(
                _eula_agreement_date
            )

        impersonation_enabled = d.pop("impersonationEnabled", UNSET)

        parent_company_name = d.pop("parentCompanyName", UNSET)

        parent_enterprise_id = d.pop("parentEnterpriseId", UNSET)

        portal_banner = d.pop("portalBanner", UNSET)

        get_v1_enterprises_managed_response_200_enterprises_item = cls(
            accept_eula=accept_eula,
            account_type=account_type,
            admin_email=admin_email,
            company_name=company_name,
            counts=counts,
            customers=customers,
            enterprise_id=enterprise_id,
            eula_agreement_date=eula_agreement_date,
            impersonation_enabled=impersonation_enabled,
            parent_company_name=parent_company_name,
            parent_enterprise_id=parent_enterprise_id,
            portal_banner=portal_banner,
        )

        get_v1_enterprises_managed_response_200_enterprises_item.additional_properties = d
        return get_v1_enterprises_managed_response_200_enterprises_item

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
