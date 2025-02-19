from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_groups_body_permissions import PutV1GroupsBodyPermissions


T = TypeVar("T", bound="PutV1GroupsBody")


@_attrs_define
class PutV1GroupsBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        group_id (Union[Unset, str]):  Example: TYPE_STRING.
        group_type (Union[Unset, str]):  Example: TYPE_ENUM.
        manages_enterprises (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        permissions (Union[Unset, PutV1GroupsBodyPermissions]):
        time_window_end (Union[Unset, str]):  Example: TYPE_INT64.
        time_window_start (Union[Unset, str]):  Example: TYPE_INT64.
    """

    description: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    group_type: Union[Unset, str] = UNSET
    manages_enterprises: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    permissions: Union[Unset, "PutV1GroupsBodyPermissions"] = UNSET
    time_window_end: Union[Unset, str] = UNSET
    time_window_start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        group_id = self.group_id

        group_type = self.group_type

        manages_enterprises = self.manages_enterprises

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
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_type is not UNSET:
            field_dict["groupType"] = group_type
        if manages_enterprises is not UNSET:
            field_dict["managesEnterprises"] = manages_enterprises
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
        from ..models.put_v1_groups_body_permissions import PutV1GroupsBodyPermissions

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        group_id = d.pop("groupId", UNSET)

        group_type = d.pop("groupType", UNSET)

        manages_enterprises = d.pop("managesEnterprises", UNSET)

        name = d.pop("name", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PutV1GroupsBodyPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PutV1GroupsBodyPermissions.from_dict(_permissions)

        time_window_end = d.pop("timeWindowEnd", UNSET)

        time_window_start = d.pop("timeWindowStart", UNSET)

        put_v1_groups_body = cls(
            description=description,
            group_id=group_id,
            group_type=group_type,
            manages_enterprises=manages_enterprises,
            name=name,
            permissions=permissions,
            time_window_end=time_window_end,
            time_window_start=time_window_start,
        )

        put_v1_groups_body.additional_properties = d
        return put_v1_groups_body

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
