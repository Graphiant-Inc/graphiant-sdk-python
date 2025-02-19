from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic")


@_attrs_define
class PostV1ExtranetsResolvePolicyTargetResponse200DevicesItemIpsecTunnelsItemStatic:
    """
    Attributes:
        destination_prefix (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    destination_prefix: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_prefix: Union[Unset, list[str]] = UNSET
        if not isinstance(self.destination_prefix, Unset):
            destination_prefix = self.destination_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_prefix is not UNSET:
            field_dict["destinationPrefix"] = destination_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_prefix = cast(list[str], d.pop("destinationPrefix", UNSET))

        post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_static = cls(
            destination_prefix=destination_prefix,
        )

        post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_static.additional_properties = d
        return post_v1_extranets_resolve_policy_target_response_200_devices_item_ipsec_tunnels_item_static

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
