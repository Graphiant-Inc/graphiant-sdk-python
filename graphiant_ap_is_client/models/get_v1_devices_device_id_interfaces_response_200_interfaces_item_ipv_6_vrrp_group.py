from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group_group_members_item import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupGroupMembersItem,
    )
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group_tracked_interfaces_item import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupTrackedInterfacesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroup")


@_attrs_define
class GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroup:
    """
    Attributes:
        accept_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        allow_inter_operability (Union[Unset, str]):  Example: TYPE_BOOL.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        effective_priority (Union[Unset, str]):  Example: TYPE_INT32.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        group_members (Union[Unset,
            list['GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupGroupMembersItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        preempt (Union[Unset, str]):  Example: TYPE_BOOL.
        priority (Union[Unset, str]):  Example: TYPE_INT32.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        tracked_interfaces (Union[Unset,
            list['GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupTrackedInterfacesItem']]):
        virtual_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        virtual_mac_address (Union[Unset, str]):  Example: TYPE_STRING.
    """

    accept_mode: Union[Unset, str] = UNSET
    allow_inter_operability: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    effective_priority: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    group_members: Union[
        Unset, list["GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupGroupMembersItem"]
    ] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preempt: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    tracked_interfaces: Union[
        Unset, list["GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupTrackedInterfacesItem"]
    ] = UNSET
    virtual_ip_address: Union[Unset, str] = UNSET
    virtual_mac_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept_mode = self.accept_mode

        allow_inter_operability = self.allow_inter_operability

        description = self.description

        effective_priority = self.effective_priority

        enabled = self.enabled

        group_members: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.group_members, Unset):
            group_members = []
            for group_members_item_data in self.group_members:
                group_members_item = group_members_item_data.to_dict()
                group_members.append(group_members_item)

        id = self.id

        name = self.name

        preempt = self.preempt

        priority = self.priority

        state = self.state

        tracked_interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_interfaces, Unset):
            tracked_interfaces = []
            for tracked_interfaces_item_data in self.tracked_interfaces:
                tracked_interfaces_item = tracked_interfaces_item_data.to_dict()
                tracked_interfaces.append(tracked_interfaces_item)

        virtual_ip_address = self.virtual_ip_address

        virtual_mac_address = self.virtual_mac_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept_mode is not UNSET:
            field_dict["acceptMode"] = accept_mode
        if allow_inter_operability is not UNSET:
            field_dict["allowInterOperability"] = allow_inter_operability
        if description is not UNSET:
            field_dict["description"] = description
        if effective_priority is not UNSET:
            field_dict["effectivePriority"] = effective_priority
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if group_members is not UNSET:
            field_dict["groupMembers"] = group_members
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if preempt is not UNSET:
            field_dict["preempt"] = preempt
        if priority is not UNSET:
            field_dict["priority"] = priority
        if state is not UNSET:
            field_dict["state"] = state
        if tracked_interfaces is not UNSET:
            field_dict["trackedInterfaces"] = tracked_interfaces
        if virtual_ip_address is not UNSET:
            field_dict["virtualIpAddress"] = virtual_ip_address
        if virtual_mac_address is not UNSET:
            field_dict["virtualMacAddress"] = virtual_mac_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group_group_members_item import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupGroupMembersItem,
        )
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group_tracked_interfaces_item import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupTrackedInterfacesItem,
        )

        d = src_dict.copy()
        accept_mode = d.pop("acceptMode", UNSET)

        allow_inter_operability = d.pop("allowInterOperability", UNSET)

        description = d.pop("description", UNSET)

        effective_priority = d.pop("effectivePriority", UNSET)

        enabled = d.pop("enabled", UNSET)

        group_members = []
        _group_members = d.pop("groupMembers", UNSET)
        for group_members_item_data in _group_members or []:
            group_members_item = (
                GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupGroupMembersItem.from_dict(
                    group_members_item_data
                )
            )

            group_members.append(group_members_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        preempt = d.pop("preempt", UNSET)

        priority = d.pop("priority", UNSET)

        state = d.pop("state", UNSET)

        tracked_interfaces = []
        _tracked_interfaces = d.pop("trackedInterfaces", UNSET)
        for tracked_interfaces_item_data in _tracked_interfaces or []:
            tracked_interfaces_item = (
                GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemIpv6VrrpGroupTrackedInterfacesItem.from_dict(
                    tracked_interfaces_item_data
                )
            )

            tracked_interfaces.append(tracked_interfaces_item)

        virtual_ip_address = d.pop("virtualIpAddress", UNSET)

        virtual_mac_address = d.pop("virtualMacAddress", UNSET)

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group = cls(
            accept_mode=accept_mode,
            allow_inter_operability=allow_inter_operability,
            description=description,
            effective_priority=effective_priority,
            enabled=enabled,
            group_members=group_members,
            id=id,
            name=name,
            preempt=preempt,
            priority=priority,
            state=state,
            tracked_interfaces=tracked_interfaces,
            virtual_ip_address=virtual_ip_address,
            virtual_mac_address=virtual_mac_address,
        )

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group.additional_properties = d
        return get_v1_devices_device_id_interfaces_response_200_interfaces_item_ipv_6_vrrp_group

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
