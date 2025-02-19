from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsSourceSegmentsResponse200VrfsItemDhcpSubnetsItemStaticLeasesItem")


@_attrs_define
class PostV1ExtranetsSourceSegmentsResponse200VrfsItemDhcpSubnetsItemStaticLeasesItem:
    """
    Attributes:
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        vrf (Union[Unset, str]):  Example: TYPE_STRING.
    """

    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        id = self.id

        ip_address = self.ip_address

        mac_address = self.mac_address

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        vrf = d.pop("vrf", UNSET)

        post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_static_leases_item = cls(
            hostname=hostname,
            id=id,
            ip_address=ip_address,
            mac_address=mac_address,
            vrf=vrf,
        )

        post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_static_leases_item.additional_properties = d
        return post_v1_extranets_source_segments_response_200_vrfs_item_dhcp_subnets_item_static_leases_item

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
