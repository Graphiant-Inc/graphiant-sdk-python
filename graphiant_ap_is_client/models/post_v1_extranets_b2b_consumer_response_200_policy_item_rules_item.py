from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerResponse200PolicyItemRulesItem")


@_attrs_define
class PostV1ExtranetsB2BConsumerResponse200PolicyItemRulesItem:
    """
    Attributes:
        outside_nat_prefix (Union[Unset, str]):  Example: TYPE_STRING.
        service_prefix (Union[Unset, str]):  Example: TYPE_STRING.
    """

    outside_nat_prefix: Union[Unset, str] = UNSET
    service_prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outside_nat_prefix = self.outside_nat_prefix

        service_prefix = self.service_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outside_nat_prefix is not UNSET:
            field_dict["outsideNatPrefix"] = outside_nat_prefix
        if service_prefix is not UNSET:
            field_dict["servicePrefix"] = service_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        outside_nat_prefix = d.pop("outsideNatPrefix", UNSET)

        service_prefix = d.pop("servicePrefix", UNSET)

        post_v1_extranets_b2b_consumer_response_200_policy_item_rules_item = cls(
            outside_nat_prefix=outside_nat_prefix,
            service_prefix=service_prefix,
        )

        post_v1_extranets_b2b_consumer_response_200_policy_item_rules_item.additional_properties = d
        return post_v1_extranets_b2b_consumer_response_200_policy_item_rules_item

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
