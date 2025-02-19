from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1AlarmsSummaryResponse200")


@_attrs_define
class GetV1AlarmsSummaryResponse200:
    """
    Attributes:
        critical (Union[Unset, str]):  Example: TYPE_INT32.
        high (Union[Unset, str]):  Example: TYPE_INT32.
        info (Union[Unset, str]):  Example: TYPE_INT32.
        low (Union[Unset, str]):  Example: TYPE_INT32.
        medium (Union[Unset, str]):  Example: TYPE_INT32.
        total (Union[Unset, str]):  Example: TYPE_INT32.
    """

    critical: Union[Unset, str] = UNSET
    high: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    low: Union[Unset, str] = UNSET
    medium: Union[Unset, str] = UNSET
    total: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        critical = self.critical

        high = self.high

        info = self.info

        low = self.low

        medium = self.medium

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if high is not UNSET:
            field_dict["high"] = high
        if info is not UNSET:
            field_dict["info"] = info
        if low is not UNSET:
            field_dict["low"] = low
        if medium is not UNSET:
            field_dict["medium"] = medium
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        critical = d.pop("critical", UNSET)

        high = d.pop("high", UNSET)

        info = d.pop("info", UNSET)

        low = d.pop("low", UNSET)

        medium = d.pop("medium", UNSET)

        total = d.pop("total", UNSET)

        get_v1_alarms_summary_response_200 = cls(
            critical=critical,
            high=high,
            info=info,
            low=low,
            medium=medium,
            total=total,
        )

        get_v1_alarms_summary_response_200.additional_properties = d
        return get_v1_alarms_summary_response_200

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
