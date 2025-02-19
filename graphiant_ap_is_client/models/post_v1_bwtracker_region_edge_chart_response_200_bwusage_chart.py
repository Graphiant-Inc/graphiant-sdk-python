from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_edge_chart_response_200_bwusage_chart_bwusage_chart_item import (
        PostV1BwtrackerRegionEdgeChartResponse200BwusageChartBwusageChartItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionEdgeChartResponse200BwusageChart")


@_attrs_define
class PostV1BwtrackerRegionEdgeChartResponse200BwusageChart:
    """
    Attributes:
        bwusage_chart (Union[Unset, list['PostV1BwtrackerRegionEdgeChartResponse200BwusageChartBwusageChartItem']]):
        percentile_usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    bwusage_chart: Union[Unset, list["PostV1BwtrackerRegionEdgeChartResponse200BwusageChartBwusageChartItem"]] = UNSET
    percentile_usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_chart: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_chart, Unset):
            bwusage_chart = []
            for bwusage_chart_item_data in self.bwusage_chart:
                bwusage_chart_item = bwusage_chart_item_data.to_dict()
                bwusage_chart.append(bwusage_chart_item)

        percentile_usage_kbps = self.percentile_usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_chart is not UNSET:
            field_dict["bwusageChart"] = bwusage_chart
        if percentile_usage_kbps is not UNSET:
            field_dict["percentileUsageKbps"] = percentile_usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_edge_chart_response_200_bwusage_chart_bwusage_chart_item import (
            PostV1BwtrackerRegionEdgeChartResponse200BwusageChartBwusageChartItem,
        )

        d = src_dict.copy()
        bwusage_chart = []
        _bwusage_chart = d.pop("bwusageChart", UNSET)
        for bwusage_chart_item_data in _bwusage_chart or []:
            bwusage_chart_item = PostV1BwtrackerRegionEdgeChartResponse200BwusageChartBwusageChartItem.from_dict(
                bwusage_chart_item_data
            )

            bwusage_chart.append(bwusage_chart_item)

        percentile_usage_kbps = d.pop("percentileUsageKbps", UNSET)

        post_v1_bwtracker_region_edge_chart_response_200_bwusage_chart = cls(
            bwusage_chart=bwusage_chart,
            percentile_usage_kbps=percentile_usage_kbps,
        )

        post_v1_bwtracker_region_edge_chart_response_200_bwusage_chart.additional_properties = d
        return post_v1_bwtracker_region_edge_chart_response_200_bwusage_chart

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
