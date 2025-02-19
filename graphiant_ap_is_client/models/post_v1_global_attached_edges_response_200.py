from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_attached_edges_response_200_statuses_item import (
        PostV1GlobalAttachedEdgesResponse200StatusesItem,
    )


T = TypeVar("T", bound="PostV1GlobalAttachedEdgesResponse200")


@_attrs_define
class PostV1GlobalAttachedEdgesResponse200:
    """
    Attributes:
        statuses (Union[Unset, list['PostV1GlobalAttachedEdgesResponse200StatusesItem']]):
    """

    statuses: Union[Unset, list["PostV1GlobalAttachedEdgesResponse200StatusesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statuses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_attached_edges_response_200_statuses_item import (
            PostV1GlobalAttachedEdgesResponse200StatusesItem,
        )

        d = src_dict.copy()
        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = PostV1GlobalAttachedEdgesResponse200StatusesItem.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        post_v1_global_attached_edges_response_200 = cls(
            statuses=statuses,
        )

        post_v1_global_attached_edges_response_200.additional_properties = d
        return post_v1_global_attached_edges_response_200

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
