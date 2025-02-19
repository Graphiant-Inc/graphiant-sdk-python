from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprises_response_200_enterprises_item_customers_item_value_counts import (
        GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts,
    )


T = TypeVar("T", bound="GetV1EnterprisesResponse200EnterprisesItemCustomersItemValue")


@_attrs_define
class GetV1EnterprisesResponse200EnterprisesItemCustomersItemValue:
    """
    Attributes:
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        company_name (Union[Unset, str]):  Example: TYPE_STRING.
        counts (Union[Unset, GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts]):
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        impersonation_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    admin_email: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    counts: Union[Unset, "GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts"] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    impersonation_enabled: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_email = self.admin_email

        company_name = self.company_name

        counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        enterprise_id = self.enterprise_id

        impersonation_enabled = self.impersonation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if counts is not UNSET:
            field_dict["counts"] = counts
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if impersonation_enabled is not UNSET:
            field_dict["impersonationEnabled"] = impersonation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprises_response_200_enterprises_item_customers_item_value_counts import (
            GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts,
        )

        d = src_dict.copy()
        admin_email = d.pop("adminEmail", UNSET)

        company_name = d.pop("companyName", UNSET)

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = GetV1EnterprisesResponse200EnterprisesItemCustomersItemValueCounts.from_dict(_counts)

        enterprise_id = d.pop("enterpriseId", UNSET)

        impersonation_enabled = d.pop("impersonationEnabled", UNSET)

        get_v1_enterprises_response_200_enterprises_item_customers_item_value = cls(
            admin_email=admin_email,
            company_name=company_name,
            counts=counts,
            enterprise_id=enterprise_id,
            impersonation_enabled=impersonation_enabled,
        )

        get_v1_enterprises_response_200_enterprises_item_customers_item_value.additional_properties = d
        return get_v1_enterprises_response_200_enterprises_item_customers_item_value

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
