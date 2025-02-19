from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_ping_response_200_result_ping_result import (
        PostV1DiagnosticPingResponse200ResultPingResult,
    )
    from ..models.post_v1_diagnostic_ping_response_200_result_route_info import (
        PostV1DiagnosticPingResponse200ResultRouteInfo,
    )
    from ..models.post_v1_diagnostic_ping_response_200_result_trace_result import (
        PostV1DiagnosticPingResponse200ResultTraceResult,
    )


T = TypeVar("T", bound="PostV1DiagnosticPingResponse200Result")


@_attrs_define
class PostV1DiagnosticPingResponse200Result:
    """
    Attributes:
        ping_result (Union[Unset, PostV1DiagnosticPingResponse200ResultPingResult]):
        route_info (Union[Unset, PostV1DiagnosticPingResponse200ResultRouteInfo]):
        trace_result (Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResult]):
    """

    ping_result: Union[Unset, "PostV1DiagnosticPingResponse200ResultPingResult"] = UNSET
    route_info: Union[Unset, "PostV1DiagnosticPingResponse200ResultRouteInfo"] = UNSET
    trace_result: Union[Unset, "PostV1DiagnosticPingResponse200ResultTraceResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ping_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ping_result, Unset):
            ping_result = self.ping_result.to_dict()

        route_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.route_info, Unset):
            route_info = self.route_info.to_dict()

        trace_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trace_result, Unset):
            trace_result = self.trace_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ping_result is not UNSET:
            field_dict["pingResult"] = ping_result
        if route_info is not UNSET:
            field_dict["routeInfo"] = route_info
        if trace_result is not UNSET:
            field_dict["traceResult"] = trace_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_ping_response_200_result_ping_result import (
            PostV1DiagnosticPingResponse200ResultPingResult,
        )
        from ..models.post_v1_diagnostic_ping_response_200_result_route_info import (
            PostV1DiagnosticPingResponse200ResultRouteInfo,
        )
        from ..models.post_v1_diagnostic_ping_response_200_result_trace_result import (
            PostV1DiagnosticPingResponse200ResultTraceResult,
        )

        d = src_dict.copy()
        _ping_result = d.pop("pingResult", UNSET)
        ping_result: Union[Unset, PostV1DiagnosticPingResponse200ResultPingResult]
        if isinstance(_ping_result, Unset):
            ping_result = UNSET
        else:
            ping_result = PostV1DiagnosticPingResponse200ResultPingResult.from_dict(_ping_result)

        _route_info = d.pop("routeInfo", UNSET)
        route_info: Union[Unset, PostV1DiagnosticPingResponse200ResultRouteInfo]
        if isinstance(_route_info, Unset):
            route_info = UNSET
        else:
            route_info = PostV1DiagnosticPingResponse200ResultRouteInfo.from_dict(_route_info)

        _trace_result = d.pop("traceResult", UNSET)
        trace_result: Union[Unset, PostV1DiagnosticPingResponse200ResultTraceResult]
        if isinstance(_trace_result, Unset):
            trace_result = UNSET
        else:
            trace_result = PostV1DiagnosticPingResponse200ResultTraceResult.from_dict(_trace_result)

        post_v1_diagnostic_ping_response_200_result = cls(
            ping_result=ping_result,
            route_info=route_info,
            trace_result=trace_result,
        )

        post_v1_diagnostic_ping_response_200_result.additional_properties = d
        return post_v1_diagnostic_ping_response_200_result

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
