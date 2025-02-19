from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsResponse200PolicyTargetSegmentsItemBgpMultipath")


@_attrs_define
class PostV1ExtranetsResponse200PolicyTargetSegmentsItemBgpMultipath:
    """
    Attributes:
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    enabled: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        post_v1_extranets_response_200_policy_target_segments_item_bgp_multipath = cls(
            enabled=enabled,
            vrf_id=vrf_id,
        )

        post_v1_extranets_response_200_policy_target_segments_item_bgp_multipath.additional_properties = d
        return post_v1_extranets_response_200_policy_target_segments_item_bgp_multipath

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
