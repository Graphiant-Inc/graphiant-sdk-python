from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrsDetailsResponse200")


@_attrs_define
class GetV1DeviceRoutingBgpNbrsDetailsResponse200:
    """
    Attributes:
        ebgp_multi_hop_ttl (Union[Unset, str]):  Example: TYPE_INT32.
        hold_timer (Union[Unset, str]):  Example: TYPE_INT32.
        keep_alive_timer (Union[Unset, str]):  Example: TYPE_INT32.
    """

    ebgp_multi_hop_ttl: Union[Unset, str] = UNSET
    hold_timer: Union[Unset, str] = UNSET
    keep_alive_timer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ebgp_multi_hop_ttl = self.ebgp_multi_hop_ttl

        hold_timer = self.hold_timer

        keep_alive_timer = self.keep_alive_timer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ebgp_multi_hop_ttl is not UNSET:
            field_dict["ebgpMultiHopTtl"] = ebgp_multi_hop_ttl
        if hold_timer is not UNSET:
            field_dict["holdTimer"] = hold_timer
        if keep_alive_timer is not UNSET:
            field_dict["keepAliveTimer"] = keep_alive_timer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ebgp_multi_hop_ttl = d.pop("ebgpMultiHopTtl", UNSET)

        hold_timer = d.pop("holdTimer", UNSET)

        keep_alive_timer = d.pop("keepAliveTimer", UNSET)

        get_v1_device_routing_bgp_nbrs_details_response_200 = cls(
            ebgp_multi_hop_ttl=ebgp_multi_hop_ttl,
            hold_timer=hold_timer,
            keep_alive_timer=keep_alive_timer,
        )

        get_v1_device_routing_bgp_nbrs_details_response_200.additional_properties = d
        return get_v1_device_routing_bgp_nbrs_details_response_200

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
