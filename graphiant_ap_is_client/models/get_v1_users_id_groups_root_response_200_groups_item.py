from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_users_id_groups_root_response_200_groups_item_permissions import (
        GetV1UsersIdGroupsRootResponse200GroupsItemPermissions,
    )


T = TypeVar("T", bound="GetV1UsersIdGroupsRootResponse200GroupsItem")


@_attrs_define
class GetV1UsersIdGroupsRootResponse200GroupsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        group_type (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        permissions (Union[Unset, GetV1UsersIdGroupsRootResponse200GroupsItemPermissions]):
        time_window_end (Union[Unset, str]):  Example: TYPE_INT64.
        time_window_start (Union[Unset, str]):  Example: TYPE_INT64.
    """

    description: Union[Unset, str] = UNSET
    enterprise_ids: Union[Unset, list[str]] = UNSET
    group_type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    permissions: Union[Unset, "GetV1UsersIdGroupsRootResponse200GroupsItemPermissions"] = UNSET
    time_window_end: Union[Unset, str] = UNSET
    time_window_start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enterprise_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enterprise_ids, Unset):
            enterprise_ids = self.enterprise_ids

        group_type = self.group_type

        id = self.id

        name = self.name

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        time_window_end = self.time_window_end

        time_window_start = self.time_window_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enterprise_ids is not UNSET:
            field_dict["enterpriseIds"] = enterprise_ids
        if group_type is not UNSET:
            field_dict["groupType"] = group_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if time_window_end is not UNSET:
            field_dict["timeWindowEnd"] = time_window_end
        if time_window_start is not UNSET:
            field_dict["timeWindowStart"] = time_window_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_users_id_groups_root_response_200_groups_item_permissions import (
            GetV1UsersIdGroupsRootResponse200GroupsItemPermissions,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        enterprise_ids = cast(list[str], d.pop("enterpriseIds", UNSET))

        group_type = d.pop("groupType", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, GetV1UsersIdGroupsRootResponse200GroupsItemPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GetV1UsersIdGroupsRootResponse200GroupsItemPermissions.from_dict(_permissions)

        time_window_end = d.pop("timeWindowEnd", UNSET)

        time_window_start = d.pop("timeWindowStart", UNSET)

        get_v1_users_id_groups_root_response_200_groups_item = cls(
            description=description,
            enterprise_ids=enterprise_ids,
            group_type=group_type,
            id=id,
            name=name,
            permissions=permissions,
            time_window_end=time_window_end,
            time_window_start=time_window_start,
        )

        get_v1_users_id_groups_root_response_200_groups_item.additional_properties = d
        return get_v1_users_id_groups_root_response_200_groups_item

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
