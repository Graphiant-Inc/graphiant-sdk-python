from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem")


@_attrs_define
class GetV1DevicesDeviceIdVrrpResponse200VrrpEntryItem:
    """
    Attributes:
        address_family (Union[Unset, str]):  Example: IPv4 or IPv6.
        advertisement_rcvd (Union[Unset, str]):  Example: TYPE_UINT64.
        advertisement_sent (Union[Unset, str]):  Example: TYPE_UINT64.
        effective_priority (Union[Unset, str]):  Example: TYPE_UINT32.
        group_id (Union[Unset, str]):  Example: TYPE_UINT32.
        is_owner (Union[Unset, str]):  Example: TYPE_BOOL.
        master_transition (Union[Unset, str]):  Example: TYPE_UINT32.
        new_master_reason (Union[Unset, str]):  Example: UNSET = 0.
        priority_zero_pkts_rcvd (Union[Unset, str]):  Example: TYPE_UINT64.
        priority_zero_pkts_sent (Union[Unset, str]):  Example: TYPE_UINT64.
        state (Union[Unset, str]):  Example: UNSET = 0.
    """

    address_family: Union[Unset, str] = UNSET
    advertisement_rcvd: Union[Unset, str] = UNSET
    advertisement_sent: Union[Unset, str] = UNSET
    effective_priority: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    is_owner: Union[Unset, str] = UNSET
    master_transition: Union[Unset, str] = UNSET
    new_master_reason: Union[Unset, str] = UNSET
    priority_zero_pkts_rcvd: Union[Unset, str] = UNSET
    priority_zero_pkts_sent: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_family = self.address_family

        advertisement_rcvd = self.advertisement_rcvd

        advertisement_sent = self.advertisement_sent

        effective_priority = self.effective_priority

        group_id = self.group_id

        is_owner = self.is_owner

        master_transition = self.master_transition

        new_master_reason = self.new_master_reason

        priority_zero_pkts_rcvd = self.priority_zero_pkts_rcvd

        priority_zero_pkts_sent = self.priority_zero_pkts_sent

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_family is not UNSET:
            field_dict["addressFamily"] = address_family
        if advertisement_rcvd is not UNSET:
            field_dict["advertisementRcvd"] = advertisement_rcvd
        if advertisement_sent is not UNSET:
            field_dict["advertisementSent"] = advertisement_sent
        if effective_priority is not UNSET:
            field_dict["effectivePriority"] = effective_priority
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner
        if master_transition is not UNSET:
            field_dict["masterTransition"] = master_transition
        if new_master_reason is not UNSET:
            field_dict["newMasterReason"] = new_master_reason
        if priority_zero_pkts_rcvd is not UNSET:
            field_dict["priorityZeroPktsRcvd"] = priority_zero_pkts_rcvd
        if priority_zero_pkts_sent is not UNSET:
            field_dict["priorityZeroPktsSent"] = priority_zero_pkts_sent
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_family = d.pop("addressFamily", UNSET)

        advertisement_rcvd = d.pop("advertisementRcvd", UNSET)

        advertisement_sent = d.pop("advertisementSent", UNSET)

        effective_priority = d.pop("effectivePriority", UNSET)

        group_id = d.pop("groupId", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        master_transition = d.pop("masterTransition", UNSET)

        new_master_reason = d.pop("newMasterReason", UNSET)

        priority_zero_pkts_rcvd = d.pop("priorityZeroPktsRcvd", UNSET)

        priority_zero_pkts_sent = d.pop("priorityZeroPktsSent", UNSET)

        state = d.pop("state", UNSET)

        get_v1_devices_device_id_vrrp_response_200_vrrp_entry_item = cls(
            address_family=address_family,
            advertisement_rcvd=advertisement_rcvd,
            advertisement_sent=advertisement_sent,
            effective_priority=effective_priority,
            group_id=group_id,
            is_owner=is_owner,
            master_transition=master_transition,
            new_master_reason=new_master_reason,
            priority_zero_pkts_rcvd=priority_zero_pkts_rcvd,
            priority_zero_pkts_sent=priority_zero_pkts_sent,
            state=state,
        )

        get_v1_devices_device_id_vrrp_response_200_vrrp_entry_item.additional_properties = d
        return get_v1_devices_device_id_vrrp_response_200_vrrp_entry_item

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
