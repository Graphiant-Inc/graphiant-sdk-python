from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalSnmpsResponse200SnmpsItemVacmGroupsItemGroupMembersItem")


@_attrs_define
class PostV1GlobalSnmpsResponse200SnmpsItemVacmGroupsItemGroupMembersItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        security_model (Union[Unset, str]):  Example: TYPE_ENUM.
        security_name (Union[Unset, str]):  Example: TYPE_STRING.
        snmp_community (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    id: Union[Unset, str] = UNSET
    security_model: Union[Unset, str] = UNSET
    security_name: Union[Unset, str] = UNSET
    snmp_community: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        security_model = self.security_model

        security_name = self.security_name

        snmp_community = self.snmp_community

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if security_model is not UNSET:
            field_dict["securityModel"] = security_model
        if security_name is not UNSET:
            field_dict["securityName"] = security_name
        if snmp_community is not UNSET:
            field_dict["snmpCommunity"] = snmp_community
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        security_model = d.pop("securityModel", UNSET)

        security_name = d.pop("securityName", UNSET)

        snmp_community = d.pop("snmpCommunity", UNSET)

        type_ = d.pop("type", UNSET)

        post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_group_members_item = cls(
            id=id,
            security_model=security_model,
            security_name=security_name,
            snmp_community=snmp_community,
            type_=type_,
        )

        post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_group_members_item.additional_properties = d
        return post_v1_global_snmps_response_200_snmps_item_vacm_groups_item_group_members_item

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
