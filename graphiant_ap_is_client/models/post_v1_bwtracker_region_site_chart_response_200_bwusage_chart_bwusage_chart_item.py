from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_chart_response_200_bwusage_chart_bwusage_chart_item_start_time import (
        PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItem")


@_attrs_define
class PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItem:
    """
    Attributes:
        avg_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        duration (Union[Unset, str]):  Example: TYPE_UINT64.
        max_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        start_time (Union[Unset, PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime]):
    """

    avg_value: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    max_value: Union[Unset, str] = UNSET
    start_time: Union[Unset, "PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_value = self.avg_value

        duration = self.duration

        max_value = self.max_value

        start_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_value is not UNSET:
            field_dict["avgValue"] = avg_value
        if duration is not UNSET:
            field_dict["duration"] = duration
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_chart_response_200_bwusage_chart_bwusage_chart_item_start_time import (
            PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime,
        )

        d = src_dict.copy()
        avg_value = d.pop("avgValue", UNSET)

        duration = d.pop("duration", UNSET)

        max_value = d.pop("maxValue", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = PostV1BwtrackerRegionSiteChartResponse200BwusageChartBwusageChartItemStartTime.from_dict(
                _start_time
            )

        post_v1_bwtracker_region_site_chart_response_200_bwusage_chart_bwusage_chart_item = cls(
            avg_value=avg_value,
            duration=duration,
            max_value=max_value,
            start_time=start_time,
        )

        post_v1_bwtracker_region_site_chart_response_200_bwusage_chart_bwusage_chart_item.additional_properties = d
        return post_v1_bwtracker_region_site_chart_response_200_bwusage_chart_bwusage_chart_item

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
