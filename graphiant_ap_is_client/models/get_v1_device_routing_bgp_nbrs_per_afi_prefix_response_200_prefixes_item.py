from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem")


@_attrs_define
class GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem:
    """
    Attributes:
        afi_safi_name (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_rcvd (Union[Unset, str]):  Example: TYPE_UINT32.
        prefix_sent (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    afi_safi_name: Union[Unset, str] = UNSET
    prefix_rcvd: Union[Unset, str] = UNSET
    prefix_sent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        afi_safi_name = self.afi_safi_name

        prefix_rcvd = self.prefix_rcvd

        prefix_sent = self.prefix_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if afi_safi_name is not UNSET:
            field_dict["afiSafiName"] = afi_safi_name
        if prefix_rcvd is not UNSET:
            field_dict["prefixRcvd"] = prefix_rcvd
        if prefix_sent is not UNSET:
            field_dict["prefixSent"] = prefix_sent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        afi_safi_name = d.pop("afiSafiName", UNSET)

        prefix_rcvd = d.pop("prefixRcvd", UNSET)

        prefix_sent = d.pop("prefixSent", UNSET)

        get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200_prefixes_item = cls(
            afi_safi_name=afi_safi_name,
            prefix_rcvd=prefix_rcvd,
            prefix_sent=prefix_sent,
        )

        get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200_prefixes_item.additional_properties = d
        return get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200_prefixes_item

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
