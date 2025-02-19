from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_ping_response_200_result_ping_result_completed_time import (
        PostV1DiagnosticPingResponse200ResultPingResultCompletedTime,
    )


T = TypeVar("T", bound="PostV1DiagnosticPingResponse200ResultPingResult")


@_attrs_define
class PostV1DiagnosticPingResponse200ResultPingResult:
    """
    Attributes:
        avg_loss (Union[Unset, str]):  Example: 64.
        avg_time (Union[Unset, str]):  Example: 3.
        completed_time (Union[Unset, PostV1DiagnosticPingResponse200ResultPingResultCompletedTime]):
        max_time (Union[Unset, str]):  Example: 10.
        min_time (Union[Unset, str]):  Example: 5.
        result (Union[Unset, str]):  Example: Success.
    """

    avg_loss: Union[Unset, str] = UNSET
    avg_time: Union[Unset, str] = UNSET
    completed_time: Union[Unset, "PostV1DiagnosticPingResponse200ResultPingResultCompletedTime"] = UNSET
    max_time: Union[Unset, str] = UNSET
    min_time: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_loss = self.avg_loss

        avg_time = self.avg_time

        completed_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.to_dict()

        max_time = self.max_time

        min_time = self.min_time

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_loss is not UNSET:
            field_dict["avgLoss"] = avg_loss
        if avg_time is not UNSET:
            field_dict["avgTime"] = avg_time
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time
        if max_time is not UNSET:
            field_dict["maxTime"] = max_time
        if min_time is not UNSET:
            field_dict["minTime"] = min_time
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_ping_response_200_result_ping_result_completed_time import (
            PostV1DiagnosticPingResponse200ResultPingResultCompletedTime,
        )

        d = src_dict.copy()
        avg_loss = d.pop("avgLoss", UNSET)

        avg_time = d.pop("avgTime", UNSET)

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: Union[Unset, PostV1DiagnosticPingResponse200ResultPingResultCompletedTime]
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = PostV1DiagnosticPingResponse200ResultPingResultCompletedTime.from_dict(_completed_time)

        max_time = d.pop("maxTime", UNSET)

        min_time = d.pop("minTime", UNSET)

        result = d.pop("result", UNSET)

        post_v1_diagnostic_ping_response_200_result_ping_result = cls(
            avg_loss=avg_loss,
            avg_time=avg_time,
            completed_time=completed_time,
            max_time=max_time,
            min_time=min_time,
            result=result,
        )

        post_v1_diagnostic_ping_response_200_result_ping_result.additional_properties = d
        return post_v1_diagnostic_ping_response_200_result_ping_result

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
