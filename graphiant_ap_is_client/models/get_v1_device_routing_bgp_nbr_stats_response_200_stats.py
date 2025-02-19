from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrStatsResponse200Stats")


@_attrs_define
class GetV1DeviceRoutingBgpNbrStatsResponse200Stats:
    """
    Attributes:
        prefix_rcvd (Union[Unset, str]):  Example: 245.
    """

    prefix_rcvd: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_rcvd = self.prefix_rcvd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix_rcvd is not UNSET:
            field_dict["prefixRcvd"] = prefix_rcvd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        prefix_rcvd = d.pop("prefixRcvd", UNSET)

        get_v1_device_routing_bgp_nbr_stats_response_200_stats = cls(
            prefix_rcvd=prefix_rcvd,
        )

        get_v1_device_routing_bgp_nbr_stats_response_200_stats.additional_properties = d
        return get_v1_device_routing_bgp_nbr_stats_response_200_stats

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
