from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalSnmpsResponse200SnmpsItemVacmGroupsItemAccessesItem")


@_attrs_define
class PostV1GlobalSnmpsResponse200SnmpsItemVacmGroupsItemAccessesItem:
    """
    Attributes:
        context (Union[Unset, str]):  Example: TYPE_STRING.
        group_context_match (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        read_view (Union[Unset, str]):  Example: TYPE_STRING.
        security_level (Union[Unset, str]):  Example: TYPE_ENUM.
        write_view (Union[Unset, str]):  Example: TYPE_STRING.
    """

    context: Union[Unset, str] = UNSET
    group_context_match: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    read_view: Union[Unset, str] = UNSET
    security_level: Union[Unset, str] = UNSET
    write_view: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        group_context_match = self.group_context_match

        id = self.id

        name = self.name

        read_view = self.read_view

        security_level = self.security_level

        write_view = self.write_view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if group_context_match is not UNSET:
            field_dict["groupContextMatch"] = group_context_match
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if read_view is not UNSET:
            field_dict["readView"] = read_view
        if security_level is not UNSET:
            field_dict["securityLevel"] = security_level
        if write_view is not UNSET:
            field_dict["writeView"] = write_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("context", UNSET)

        group_context_match = d.pop("groupContextMatch", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        read_view = d.pop("readView", UNSET)

        security_level = d.pop("securityLevel", UNSET)

        write_view = d.pop("writeView", UNSET)

        post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_accesses_item = cls(
            context=context,
            group_context_match=group_context_match,
            id=id,
            name=name,
            read_view=read_view,
            security_level=security_level,
            write_view=write_view,
        )

        post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_accesses_item.additional_properties = d
        return post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_accesses_item

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
