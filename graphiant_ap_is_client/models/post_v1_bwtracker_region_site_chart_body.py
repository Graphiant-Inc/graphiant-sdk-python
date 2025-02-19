from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_region_site_chart_body_time_window import (
        PostV1BwtrackerRegionSiteChartBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV1BwtrackerRegionSiteChartBody")


@_attrs_define
class PostV1BwtrackerRegionSiteChartBody:
    """
    Attributes:
        region_id (Union[Unset, str]):  Example: TYPE_UINT64.
        site_id (Union[Unset, str]):  Example: TYPE_UINT64.
        time_window (Union[Unset, PostV1BwtrackerRegionSiteChartBodyTimeWindow]):
    """

    region_id: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1BwtrackerRegionSiteChartBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        site_id = self.site_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_region_site_chart_body_time_window import (
            PostV1BwtrackerRegionSiteChartBodyTimeWindow,
        )

        d = src_dict.copy()
        region_id = d.pop("regionId", UNSET)

        site_id = d.pop("siteId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1BwtrackerRegionSiteChartBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1BwtrackerRegionSiteChartBodyTimeWindow.from_dict(_time_window)

        post_v1_bwtracker_region_site_chart_body = cls(
            region_id=region_id,
            site_id=site_id,
            time_window=time_window,
        )

        post_v1_bwtracker_region_site_chart_body.additional_properties = d
        return post_v1_bwtracker_region_site_chart_body

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
