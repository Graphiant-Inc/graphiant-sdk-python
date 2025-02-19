from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_id_customer_response_200_responses_item import (
        PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BIdCustomerResponse200")


@_attrs_define
class PostV1ExtranetsB2BIdCustomerResponse200:
    """
    Attributes:
        responses (Union[Unset, list['PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem']]):
    """

    responses: Union[Unset, list["PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_id_customer_response_200_responses_item import (
            PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem,
        )

        d = src_dict.copy()
        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = PostV1ExtranetsB2BIdCustomerResponse200ResponsesItem.from_dict(responses_item_data)

            responses.append(responses_item)

        post_v1_extranets_b2b_id_customer_response_200 = cls(
            responses=responses,
        )

        post_v1_extranets_b2b_id_customer_response_200.additional_properties = d
        return post_v1_extranets_b2b_id_customer_response_200

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
