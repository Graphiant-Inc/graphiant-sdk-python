from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_sites_usage_response_200_ul_stats_item_ts import (
        PostV2ExtranetSitesUsageResponse200UlStatsItemTs,
    )


T = TypeVar("T", bound="PostV2ExtranetSitesUsageResponse200UlStatsItem")


@_attrs_define
class PostV2ExtranetSitesUsageResponse200UlStatsItem:
    """
    Attributes:
        avg_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        peak_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        ts (Union[Unset, PostV2ExtranetSitesUsageResponse200UlStatsItemTs]):
    """

    avg_usage: Union[Unset, str] = UNSET
    peak_usage: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV2ExtranetSitesUsageResponse200UlStatsItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_usage = self.avg_usage

        peak_usage = self.peak_usage

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_usage is not UNSET:
            field_dict["avgUsage"] = avg_usage
        if peak_usage is not UNSET:
            field_dict["peakUsage"] = peak_usage
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_sites_usage_response_200_ul_stats_item_ts import (
            PostV2ExtranetSitesUsageResponse200UlStatsItemTs,
        )

        d = src_dict.copy()
        avg_usage = d.pop("avgUsage", UNSET)

        peak_usage = d.pop("peakUsage", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2ExtranetSitesUsageResponse200UlStatsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2ExtranetSitesUsageResponse200UlStatsItemTs.from_dict(_ts)

        post_v2_extranet_sites_usage_response_200_ul_stats_item = cls(
            avg_usage=avg_usage,
            peak_usage=peak_usage,
            ts=ts,
        )

        post_v2_extranet_sites_usage_response_200_ul_stats_item.additional_properties = d
        return post_v2_extranet_sites_usage_response_200_ul_stats_item

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
