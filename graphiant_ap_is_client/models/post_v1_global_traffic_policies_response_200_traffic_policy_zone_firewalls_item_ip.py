from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItemIp")


@_attrs_define
class PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItemIp:
    """
    Attributes:
        block_land_attacks (Union[Unset, str]):  Example: TYPE_BOOL.
        session_limit (Union[Unset, str]):  Example: TYPE_UINT32.
        urpf (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    block_land_attacks: Union[Unset, str] = UNSET
    session_limit: Union[Unset, str] = UNSET
    urpf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_land_attacks = self.block_land_attacks

        session_limit = self.session_limit

        urpf = self.urpf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_land_attacks is not UNSET:
            field_dict["blockLandAttacks"] = block_land_attacks
        if session_limit is not UNSET:
            field_dict["sessionLimit"] = session_limit
        if urpf is not UNSET:
            field_dict["urpf"] = urpf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        block_land_attacks = d.pop("blockLandAttacks", UNSET)

        session_limit = d.pop("sessionLimit", UNSET)

        urpf = d.pop("urpf", UNSET)

        post_v1_global_traffic_policies_response_200_traffic_policy_zone_firewalls_item_ip = cls(
            block_land_attacks=block_land_attacks,
            session_limit=session_limit,
            urpf=urpf,
        )

        post_v1_global_traffic_policies_response_200_traffic_policy_zone_firewalls_item_ip.additional_properties = d
        return post_v1_global_traffic_policies_response_200_traffic_policy_zone_firewalls_item_ip

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
