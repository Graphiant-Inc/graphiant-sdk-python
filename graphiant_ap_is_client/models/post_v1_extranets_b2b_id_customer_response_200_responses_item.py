from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem")


@_attrs_define
class PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem:
    """
    Attributes:
        admin_email (Union[Unset, str]):  Example: TYPE_STRING.
        consumer_bw_site (Union[Unset, str]):  Example: TYPE_UINT32.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        maximum_site_count (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    admin_email: Union[Unset, str] = UNSET
    consumer_bw_site: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    maximum_site_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_email = self.admin_email

        consumer_bw_site = self.consumer_bw_site

        enterprise_id = self.enterprise_id

        id = self.id

        maximum_site_count = self.maximum_site_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_email is not UNSET:
            field_dict["adminEmail"] = admin_email
        if consumer_bw_site is not UNSET:
            field_dict["consumerBwSite"] = consumer_bw_site
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if maximum_site_count is not UNSET:
            field_dict["maximumSiteCount"] = maximum_site_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_email = d.pop("adminEmail", UNSET)

        consumer_bw_site = d.pop("consumerBwSite", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        id = d.pop("id", UNSET)

        maximum_site_count = d.pop("maximumSiteCount", UNSET)

        post_v1_extranets_b2b_id_customer_response_200_responses_item = cls(
            admin_email=admin_email,
            consumer_bw_site=consumer_bw_site,
            enterprise_id=enterprise_id,
            id=id,
            maximum_site_count=maximum_site_count,
        )

        post_v1_extranets_b2b_id_customer_response_200_responses_item.additional_properties = d
        return post_v1_extranets_b2b_id_customer_response_200_responses_item

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
