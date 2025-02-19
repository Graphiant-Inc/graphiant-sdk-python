from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_accesses_item import (
        PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemAccessesItem,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_group_members_item import (
        PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemGroupMembersItem,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_views_item import (
        PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemViewsItem,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItem")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItem:
    """
    Attributes:
        accesses (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemAccessesItem']]):
        group_members (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemGroupMembersItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        views (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemViewsItem']]):
    """

    accesses: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemAccessesItem"]] = UNSET
    group_members: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemGroupMembersItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    views: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemViewsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.accesses, Unset):
            accesses = []
            for accesses_item_data in self.accesses:
                accesses_item = accesses_item_data.to_dict()
                accesses.append(accesses_item)

        group_members: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.group_members, Unset):
            group_members = []
            for group_members_item_data in self.group_members:
                group_members_item = group_members_item_data.to_dict()
                group_members.append(group_members_item)

        id = self.id

        name = self.name

        views: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()
                views.append(views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accesses is not UNSET:
            field_dict["accesses"] = accesses
        if group_members is not UNSET:
            field_dict["groupMembers"] = group_members
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_accesses_item import (
            PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemAccessesItem,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_group_members_item import (
            PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemGroupMembersItem,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item_views_item import (
            PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemViewsItem,
        )

        d = src_dict.copy()
        accesses = []
        _accesses = d.pop("accesses", UNSET)
        for accesses_item_data in _accesses or []:
            accesses_item = PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemAccessesItem.from_dict(
                accesses_item_data
            )

            accesses.append(accesses_item)

        group_members = []
        _group_members = d.pop("groupMembers", UNSET)
        for group_members_item_data in _group_members or []:
            group_members_item = PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemGroupMembersItem.from_dict(
                group_members_item_data
            )

            group_members.append(group_members_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        views = []
        _views = d.pop("views", UNSET)
        for views_item_data in _views or []:
            views_item = PostV1DevicesDeviceIdDraftBodyDraftSnmpVacmGroupsItemViewsItem.from_dict(views_item_data)

            views.append(views_item)

        post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item = cls(
            accesses=accesses,
            group_members=group_members,
            id=id,
            name=name,
            views=views,
        )

        post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_snmp_vacm_groups_item

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
