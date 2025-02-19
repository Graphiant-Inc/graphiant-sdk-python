from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_id_customer_body_invites_item import PostV1ExtranetsB2BIdCustomerBodyInvitesItem


T = TypeVar("T", bound="PostV1ExtranetsB2BIdCustomerBody")


@_attrs_define
class PostV1ExtranetsB2BIdCustomerBody:
    """
    Attributes:
        invites (Union[Unset, list['PostV1ExtranetsB2BIdCustomerBodyInvitesItem']]):
    """

    invites: Union[Unset, list["PostV1ExtranetsB2BIdCustomerBodyInvitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invites, Unset):
            invites = []
            for invites_item_data in self.invites:
                invites_item = invites_item_data.to_dict()
                invites.append(invites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invites is not UNSET:
            field_dict["invites"] = invites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_id_customer_body_invites_item import (
            PostV1ExtranetsB2BIdCustomerBodyInvitesItem,
        )

        d = src_dict.copy()
        invites = []
        _invites = d.pop("invites", UNSET)
        for invites_item_data in _invites or []:
            invites_item = PostV1ExtranetsB2BIdCustomerBodyInvitesItem.from_dict(invites_item_data)

            invites.append(invites_item)

        post_v1_extranets_b2b_id_customer_body = cls(
            invites=invites,
        )

        post_v1_extranets_b2b_id_customer_body.additional_properties = d
        return post_v1_extranets_b2b_id_customer_body

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
