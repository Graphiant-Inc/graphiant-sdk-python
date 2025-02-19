from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteV1GroupsIdResponse204")


@_attrs_define
class DeleteV1GroupsIdResponse204:
    """
    Attributes:
        affected_users (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        enterprise_group (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    affected_users: Union[Unset, list[str]] = UNSET
    enterprise_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_users, Unset):
            affected_users = self.affected_users

        enterprise_group = self.enterprise_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_users is not UNSET:
            field_dict["affectedUsers"] = affected_users
        if enterprise_group is not UNSET:
            field_dict["enterpriseGroup"] = enterprise_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        affected_users = cast(list[str], d.pop("affectedUsers", UNSET))

        enterprise_group = d.pop("enterpriseGroup", UNSET)

        delete_v1_groups_id_response_204 = cls(
            affected_users=affected_users,
            enterprise_group=enterprise_group,
        )

        delete_v1_groups_id_response_204.additional_properties = d
        return delete_v1_groups_id_response_204

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
