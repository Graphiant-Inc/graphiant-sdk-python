from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsSourceSegmentsResponse200VrfsItemDhcpSubnetsItemNameservers")


@_attrs_define
class PostV1ExtranetsSourceSegmentsResponse200VrfsItemDhcpSubnetsItemNameservers:
    """
    Attributes:
        primary (Union[Unset, str]):  Example: TYPE_STRING.
        secondary (Union[Unset, str]):  Example: TYPE_STRING.
    """

    primary: Union[Unset, str] = UNSET
    secondary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary = self.primary

        secondary = self.secondary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary
        if secondary is not UNSET:
            field_dict["secondary"] = secondary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        primary = d.pop("primary", UNSET)

        secondary = d.pop("secondary", UNSET)

        post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_nameservers = cls(
            primary=primary,
            secondary=secondary,
        )

        post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_nameservers.additional_properties = d
        return post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_nameservers

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
