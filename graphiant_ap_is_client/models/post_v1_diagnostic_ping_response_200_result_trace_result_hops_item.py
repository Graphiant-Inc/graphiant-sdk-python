from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_hops_item_stats import (
        PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats,
    )


T = TypeVar("T", bound="PostV1DiagnosticPingResponse200ResultTraceResultHopsItem")


@_attrs_define
class PostV1DiagnosticPingResponse200ResultTraceResultHopsItem:
    """
    Attributes:
        host_address (Union[Unset, str]):  Example: 1213:1::6451.
        path_mtu (Union[Unset, str]):  Example: 1500.
        round_trip_time (Union[Unset, str]):  Example: 10.
        stats (Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats]):
    """

    host_address: Union[Unset, str] = UNSET
    path_mtu: Union[Unset, str] = UNSET
    round_trip_time: Union[Unset, str] = UNSET
    stats: Union[Unset, "PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host_address = self.host_address

        path_mtu = self.path_mtu

        round_trip_time = self.round_trip_time

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_address is not UNSET:
            field_dict["hostAddress"] = host_address
        if path_mtu is not UNSET:
            field_dict["pathMtu"] = path_mtu
        if round_trip_time is not UNSET:
            field_dict["roundTripTime"] = round_trip_time
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_hops_item_stats import (
            PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats,
        )

        d = src_dict.copy()
        host_address = d.pop("hostAddress", UNSET)

        path_mtu = d.pop("pathMtu", UNSET)

        round_trip_time = d.pop("roundTripTime", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = PostV1DiagnosticPingResponse200ResultTraceResultHopsItemStats.from_dict(_stats)

        post_v1_diagnostic_ping_response_200_result_trace_result_hops_item = cls(
            host_address=host_address,
            path_mtu=path_mtu,
            round_trip_time=round_trip_time,
            stats=stats,
        )

        post_v1_diagnostic_ping_response_200_result_trace_result_hops_item.additional_properties = d
        return post_v1_diagnostic_ping_response_200_result_trace_result_hops_item

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
