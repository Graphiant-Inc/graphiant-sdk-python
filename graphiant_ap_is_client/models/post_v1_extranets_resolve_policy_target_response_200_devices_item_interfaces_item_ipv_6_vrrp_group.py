from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemInterfacesItemIpv6VrrpGroup")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemInterfacesItemIpv6VrrpGroup:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        post_v1_extranets_resolve_policy_target_response_200_devices_item_interfaces_item_ipv_6_vrrp_group = cls()

        post_v1_extranets_resolve_policy_target_response_200_devices_item_interfaces_item_ipv_6_vrrp_group.additional_properties = d
        return post_v1_extranets_resolve_policy_target_response_200_devices_item_interfaces_item_ipv_6_vrrp_group

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
