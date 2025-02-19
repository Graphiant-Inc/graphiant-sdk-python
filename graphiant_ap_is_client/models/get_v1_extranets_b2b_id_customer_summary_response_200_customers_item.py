from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_id_customer_summary_response_200_customers_item_updated_at import (
        GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem")


@_attrs_define
class GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem:
    """
    Attributes:
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        updated_at (Union[Unset, GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt]):
    """

    admin_email: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    updated_at: Union[Unset, "GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_email = self.admin_email

        enterprise_id = self.enterprise_id

        id = self.id

        name = self.name

        status = self.status

        updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_id_customer_summary_response_200_customers_item_updated_at import (
            GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt,
        )

        d = src_dict.copy()
        admin_email = d.pop("adminEmail", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItemUpdatedAt.from_dict(_updated_at)

        get_v1_extranets_b2b_id_customer_summary_response_200_customers_item = cls(
            admin_email=admin_email,
            enterprise_id=enterprise_id,
            id=id,
            name=name,
            status=status,
            updated_at=updated_at,
        )

        get_v1_extranets_b2b_id_customer_summary_response_200_customers_item.additional_properties = d
        return get_v1_extranets_b2b_id_customer_summary_response_200_customers_item

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
