from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesResponse200DevicesItemTrafficPolicyZonePairsItem")


@_attrs_define
class PostV1DevicesResponse200DevicesItemTrafficPolicyZonePairsItem:
    """
    Attributes:
        inside (Union[Unset, str]):  Example: TYPE_STRING.
        outside (Union[Unset, str]):  Example: TYPE_STRING.
        ruleset (Union[Unset, str]):  Example: TYPE_STRING.
        tcp_protection (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    inside: Union[Unset, str] = UNSET
    outside: Union[Unset, str] = UNSET
    ruleset: Union[Unset, str] = UNSET
    tcp_protection: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inside = self.inside

        outside = self.outside

        ruleset = self.ruleset

        tcp_protection = self.tcp_protection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inside is not UNSET:
            field_dict["inside"] = inside
        if outside is not UNSET:
            field_dict["outside"] = outside
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset
        if tcp_protection is not UNSET:
            field_dict["tcpProtection"] = tcp_protection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        inside = d.pop("inside", UNSET)

        outside = d.pop("outside", UNSET)

        ruleset = d.pop("ruleset", UNSET)

        tcp_protection = d.pop("tcpProtection", UNSET)

        post_v1_devices_response_200_devices_item_traffic_policy_zone_pairs_item = cls(
            inside=inside,
            outside=outside,
            ruleset=ruleset,
            tcp_protection=tcp_protection,
        )

        post_v1_devices_response_200_devices_item_traffic_policy_zone_pairs_item.additional_properties = d
        return post_v1_devices_response_200_devices_item_traffic_policy_zone_pairs_item

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
