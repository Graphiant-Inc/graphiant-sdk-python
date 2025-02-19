from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_bgp_nbr_stats_response_200_page_info import (
        GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo,
    )
    from ..models.get_v1_device_routing_bgp_nbr_stats_response_200_stats import (
        GetV1DeviceRoutingBgpNbrStatsResponse200Stats,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrStatsResponse200")


@_attrs_define
class GetV1DeviceRoutingBgpNbrStatsResponse200:
    """
    Attributes:
        page_info (Union[Unset, GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo]):
        stats (Union[Unset, GetV1DeviceRoutingBgpNbrStatsResponse200Stats]):
        token (Union[Unset, str]):  Example: xxxxxxxxx.
    """

    page_info: Union[Unset, "GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo"] = UNSET
    stats: Union[Unset, "GetV1DeviceRoutingBgpNbrStatsResponse200Stats"] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if stats is not UNSET:
            field_dict["stats"] = stats
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_bgp_nbr_stats_response_200_page_info import (
            GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo,
        )
        from ..models.get_v1_device_routing_bgp_nbr_stats_response_200_stats import (
            GetV1DeviceRoutingBgpNbrStatsResponse200Stats,
        )

        d = src_dict.copy()
        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DeviceRoutingBgpNbrStatsResponse200PageInfo.from_dict(_page_info)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, GetV1DeviceRoutingBgpNbrStatsResponse200Stats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = GetV1DeviceRoutingBgpNbrStatsResponse200Stats.from_dict(_stats)

        token = d.pop("token", UNSET)

        get_v1_device_routing_bgp_nbr_stats_response_200 = cls(
            page_info=page_info,
            stats=stats,
            token=token,
        )

        get_v1_device_routing_bgp_nbr_stats_response_200.additional_properties = d
        return get_v1_device_routing_bgp_nbr_stats_response_200

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
