from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_consumers_usage_top_body_time_window_old_ts import (
        PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs,
    )
    from ..models.post_v2_extranet_consumers_usage_top_body_time_window_recent_ts import (
        PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs,
    )


T = TypeVar("T", bound="PostV2ExtranetConsumersUsageTopBodyTimeWindow")


@_attrs_define
class PostV2ExtranetConsumersUsageTopBodyTimeWindow:
    """
    Attributes:
        bucket_size_sec (Union[Unset, str]):  Example: TYPE_UINT32.
        old_ts (Union[Unset, PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs]):
        recent_ts (Union[Unset, PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs]):
    """

    bucket_size_sec: Union[Unset, str] = UNSET
    old_ts: Union[Unset, "PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs"] = UNSET
    recent_ts: Union[Unset, "PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_size_sec = self.bucket_size_sec

        old_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.old_ts, Unset):
            old_ts = self.old_ts.to_dict()

        recent_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recent_ts, Unset):
            recent_ts = self.recent_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_size_sec is not UNSET:
            field_dict["bucketSizeSec"] = bucket_size_sec
        if old_ts is not UNSET:
            field_dict["oldTs"] = old_ts
        if recent_ts is not UNSET:
            field_dict["recentTs"] = recent_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_consumers_usage_top_body_time_window_old_ts import (
            PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs,
        )
        from ..models.post_v2_extranet_consumers_usage_top_body_time_window_recent_ts import (
            PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs,
        )

        d = src_dict.copy()
        bucket_size_sec = d.pop("bucketSizeSec", UNSET)

        _old_ts = d.pop("oldTs", UNSET)
        old_ts: Union[Unset, PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs]
        if isinstance(_old_ts, Unset):
            old_ts = UNSET
        else:
            old_ts = PostV2ExtranetConsumersUsageTopBodyTimeWindowOldTs.from_dict(_old_ts)

        _recent_ts = d.pop("recentTs", UNSET)
        recent_ts: Union[Unset, PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs]
        if isinstance(_recent_ts, Unset):
            recent_ts = UNSET
        else:
            recent_ts = PostV2ExtranetConsumersUsageTopBodyTimeWindowRecentTs.from_dict(_recent_ts)

        post_v2_extranet_consumers_usage_top_body_time_window = cls(
            bucket_size_sec=bucket_size_sec,
            old_ts=old_ts,
            recent_ts=recent_ts,
        )

        post_v2_extranet_consumers_usage_top_body_time_window.additional_properties = d
        return post_v2_extranet_consumers_usage_top_body_time_window

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
