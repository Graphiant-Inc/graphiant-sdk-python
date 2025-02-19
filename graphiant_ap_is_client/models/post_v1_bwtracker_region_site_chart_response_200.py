from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_chart_response_200_bwusage_chart import (
        PostV1BwtrackerRegionSiteChartResponse200BwusageChart,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteChartResponse200")


@_attrs_define
class PostV1BwtrackerRegionSiteChartResponse200:
    """
    Attributes:
        bwusage_chart (Union[Unset, PostV1BwtrackerRegionSiteChartResponse200BwusageChart]):
    """

    bwusage_chart: Union[Unset, "PostV1BwtrackerRegionSiteChartResponse200BwusageChart"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_chart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bwusage_chart, Unset):
            bwusage_chart = self.bwusage_chart.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_chart is not UNSET:
            field_dict["bwusageChart"] = bwusage_chart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_chart_response_200_bwusage_chart import (
            PostV1BwtrackerRegionSiteChartResponse200BwusageChart,
        )

        d = src_dict.copy()
        _bwusage_chart = d.pop("bwusageChart", UNSET)
        bwusage_chart: Union[Unset, PostV1BwtrackerRegionSiteChartResponse200BwusageChart]
        if isinstance(_bwusage_chart, Unset):
            bwusage_chart = UNSET
        else:
            bwusage_chart = PostV1BwtrackerRegionSiteChartResponse200BwusageChart.from_dict(_bwusage_chart)

        post_v1_bwtracker_region_site_chart_response_200 = cls(
            bwusage_chart=bwusage_chart,
        )

        post_v1_bwtracker_region_site_chart_response_200.additional_properties = d
        return post_v1_bwtracker_region_site_chart_response_200

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
