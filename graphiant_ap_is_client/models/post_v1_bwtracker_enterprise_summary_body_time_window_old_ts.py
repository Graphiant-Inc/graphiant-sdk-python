from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BwtrackerEnterpriseSummaryBodyTimeWindowOldTs")


@_attrs_define
class PostV1BwtrackerEnterpriseSummaryBodyTimeWindowOldTs:
    """
    Attributes:
        nanos (Union[Unset, str]):  Example: TYPE_INT32.
        seconds (Union[Unset, str]):  Example: TYPE_INT64.
    """

    nanos: Union[Unset, str] = UNSET
    seconds: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nanos = self.nanos

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nanos is not UNSET:
            field_dict["nanos"] = nanos
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        nanos = d.pop("nanos", UNSET)

        seconds = d.pop("seconds", UNSET)

        post_v1_bwtracker_enterprise_summary_body_time_window_old_ts = cls(
            nanos=nanos,
            seconds=seconds,
        )

        post_v1_bwtracker_enterprise_summary_body_time_window_old_ts.additional_properties = d
        return post_v1_bwtracker_enterprise_summary_body_time_window_old_ts

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
