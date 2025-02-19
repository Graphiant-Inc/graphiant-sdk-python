from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_hops_item import (
        PostV1DiagnosticPingResponse200ResultTraceResultHopsItem,
    )
    from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_stopped_time import (
        PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime,
    )


T = TypeVar("T", bound="PostV1DiagnosticPingResponse200ResultTraceResult")


@_attrs_define
class PostV1DiagnosticPingResponse200ResultTraceResult:
    """
    Attributes:
        hops (Union[Unset, list['PostV1DiagnosticPingResponse200ResultTraceResultHopsItem']]):
        max_latency (Union[Unset, str]):  Example: 10.
        max_latency_host (Union[Unset, str]):  Example: A123:3242::1111.
        max_path_mtu (Union[Unset, str]):  Example: 1500.
        min_path_mtu (Union[Unset, str]):  Example: 1000.
        result (Union[Unset, str]):  Example: Failed.
        stopped_time (Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime]):
    """

    hops: Union[Unset, list["PostV1DiagnosticPingResponse200ResultTraceResultHopsItem"]] = UNSET
    max_latency: Union[Unset, str] = UNSET
    max_latency_host: Union[Unset, str] = UNSET
    max_path_mtu: Union[Unset, str] = UNSET
    min_path_mtu: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    stopped_time: Union[Unset, "PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hops, Unset):
            hops = []
            for hops_item_data in self.hops:
                hops_item = hops_item_data.to_dict()
                hops.append(hops_item)

        max_latency = self.max_latency

        max_latency_host = self.max_latency_host

        max_path_mtu = self.max_path_mtu

        min_path_mtu = self.min_path_mtu

        result = self.result

        stopped_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stopped_time, Unset):
            stopped_time = self.stopped_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hops is not UNSET:
            field_dict["hops"] = hops
        if max_latency is not UNSET:
            field_dict["maxLatency"] = max_latency
        if max_latency_host is not UNSET:
            field_dict["maxLatencyHost"] = max_latency_host
        if max_path_mtu is not UNSET:
            field_dict["maxPathMtu"] = max_path_mtu
        if min_path_mtu is not UNSET:
            field_dict["minPathMtu"] = min_path_mtu
        if result is not UNSET:
            field_dict["result"] = result
        if stopped_time is not UNSET:
            field_dict["stoppedTime"] = stopped_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_hops_item import (
            PostV1DiagnosticPingResponse200ResultTraceResultHopsItem,
        )
        from ..models.post_v1_diagnostic_ping_response_200_result_trace_result_stopped_time import (
            PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime,
        )

        d = src_dict.copy()
        hops = []
        _hops = d.pop("hops", UNSET)
        for hops_item_data in _hops or []:
            hops_item = PostV1DiagnosticPingResponse200ResultTraceResultHopsItem.from_dict(hops_item_data)

            hops.append(hops_item)

        max_latency = d.pop("maxLatency", UNSET)

        max_latency_host = d.pop("maxLatencyHost", UNSET)

        max_path_mtu = d.pop("maxPathMtu", UNSET)

        min_path_mtu = d.pop("minPathMtu", UNSET)

        result = d.pop("result", UNSET)

        _stopped_time = d.pop("stoppedTime", UNSET)
        stopped_time: Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime]
        if isinstance(_stopped_time, Unset):
            stopped_time = UNSET
        else:
            stopped_time = PostV1DiagnosticPingResponse200ResultTraceResultStoppedTime.from_dict(_stopped_time)

        post_v1_diagnostic_ping_response_200_result_trace_result = cls(
            hops=hops,
            max_latency=max_latency,
            max_latency_host=max_latency_host,
            max_path_mtu=max_path_mtu,
            min_path_mtu=min_path_mtu,
            result=result,
            stopped_time=stopped_time,
        )

        post_v1_diagnostic_ping_response_200_result_trace_result.additional_properties = d
        return post_v1_diagnostic_ping_response_200_result_trace_result

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
