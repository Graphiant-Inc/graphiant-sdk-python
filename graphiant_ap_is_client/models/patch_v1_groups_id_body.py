from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_groups_id_body_permissions import PatchV1GroupsIdBodyPermissions


T = TypeVar("T", bound="PatchV1GroupsIdBody")


@_attrs_define
class PatchV1GroupsIdBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        display_name (Union[Unset, str]):  Example: TYPE_STRING.
        group_type (Union[Unset, str]):  Example: TYPE_ENUM.
        permissions (Union[Unset, PatchV1GroupsIdBodyPermissions]):
        time_window_end (Union[Unset, str]):  Example: TYPE_INT64.
        time_window_start (Union[Unset, str]):  Example: TYPE_INT64.
    """

    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    group_type: Union[Unset, str] = UNSET
    permissions: Union[Unset, "PatchV1GroupsIdBodyPermissions"] = UNSET
    time_window_end: Union[Unset, str] = UNSET
    time_window_start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        group_type = self.group_type

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
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if group_type is not UNSET:
            field_dict["groupType"] = group_type
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if time_window_end is not UNSET:
            field_dict["timeWindowEnd"] = time_window_end
        if time_window_start is not UNSET:
            field_dict["timeWindowStart"] = time_window_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_groups_id_body_permissions import PatchV1GroupsIdBodyPermissions

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        group_type = d.pop("groupType", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PatchV1GroupsIdBodyPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PatchV1GroupsIdBodyPermissions.from_dict(_permissions)

        time_window_end = d.pop("timeWindowEnd", UNSET)

        time_window_start = d.pop("timeWindowStart", UNSET)

        patch_v1_groups_id_body = cls(
            description=description,
            display_name=display_name,
            group_type=group_type,
            permissions=permissions,
            time_window_end=time_window_end,
            time_window_start=time_window_start,
        )

        patch_v1_groups_id_body.additional_properties = d
        return patch_v1_groups_id_body

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
