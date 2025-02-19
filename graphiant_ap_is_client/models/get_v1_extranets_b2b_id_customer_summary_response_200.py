from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_id_customer_summary_response_200_customers_item import (
        GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BIdCustomerSummaryResponse200")


@_attrs_define
class GetV1ExtranetsB2BIdCustomerSummaryResponse200:
    """
    Attributes:
        customers (Union[Unset, list['GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem']]):
    """

    customers: Union[Unset, list["GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customers is not UNSET:
            field_dict["customers"] = customers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_id_customer_summary_response_200_customers_item import (
            GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem,
        )

        d = src_dict.copy()
        customers = []
        _customers = d.pop("customers", UNSET)
        for customers_item_data in _customers or []:
            customers_item = GetV1ExtranetsB2BIdCustomerSummaryResponse200CustomersItem.from_dict(customers_item_data)

            customers.append(customers_item)

        get_v1_extranets_b2b_id_customer_summary_response_200 = cls(
            customers=customers,
        )

        get_v1_extranets_b2b_id_customer_summary_response_200.additional_properties = d
        return get_v1_extranets_b2b_id_customer_summary_response_200

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
