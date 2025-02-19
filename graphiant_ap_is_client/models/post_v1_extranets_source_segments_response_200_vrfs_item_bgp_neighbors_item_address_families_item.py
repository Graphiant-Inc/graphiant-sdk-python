from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtranetsSourceSegmentsResponse200VrfsItemBgpNeighborsItemAddressFamiliesItem")


@_attrs_define
class PostV1ExtranetsSourceSegmentsResponse200VrfsItemBgpNeighborsItemAddressFamiliesItem:
    """
    Attributes:
        address_family (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        inbound_policy (Union[Unset, str]):  Example: TYPE_STRING.
        outbound_policy (Union[Unset, str]):  Example: TYPE_STRING.
    """

    address_family: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    inbound_policy: Union[Unset, str] = UNSET
    outbound_policy: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_family = self.address_family

        id = self.id

        inbound_policy = self.inbound_policy

        outbound_policy = self.outbound_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_family is not UNSET:
            field_dict["addressFamily"] = address_family
        if id is not UNSET:
            field_dict["id"] = id
        if inbound_policy is not UNSET:
            field_dict["inboundPolicy"] = inbound_policy
        if outbound_policy is not UNSET:
            field_dict["outboundPolicy"] = outbound_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_family = d.pop("addressFamily", UNSET)

        id = d.pop("id", UNSET)

        inbound_policy = d.pop("inboundPolicy", UNSET)

        outbound_policy = d.pop("outboundPolicy", UNSET)

        post_v1_extranets_source_segments_response_200_vrfs_item_bgp_neighbors_item_address_families_item = cls(
            address_family=address_family,
            id=id,
            inbound_policy=inbound_policy,
            outbound_policy=outbound_policy,
        )

        post_v1_extranets_source_segments_response_200_vrfs_item_bgp_neighbors_item_address_families_item.additional_properties = d
        return post_v1_extranets_source_segments_response_200_vrfs_item_bgp_neighbors_item_address_families_item

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
