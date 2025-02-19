from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_lan_segments_usage_top_body_time_window import (
        PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2ExtranetLanSegmentsUsageTopBody")


@_attrs_define
class PostV2ExtranetLanSegmentsUsageTopBody:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_b2b (Union[Unset, str]):  Example: TYPE_BOOL.
        is_provider (Union[Unset, str]):  Example: TYPE_BOOL.
        time_window (Union[Unset, PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow]):
    """

    id: Union[Unset, str] = UNSET
    is_b2b: Union[Unset, str] = UNSET
    is_provider: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_b2b = self.is_b2b

        is_provider = self.is_provider

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_b2b is not UNSET:
            field_dict["isB2B"] = is_b2b
        if is_provider is not UNSET:
            field_dict["isProvider"] = is_provider
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_lan_segments_usage_top_body_time_window import (
            PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_b2b = d.pop("isB2B", UNSET)

        is_provider = d.pop("isProvider", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2ExtranetLanSegmentsUsageTopBodyTimeWindow.from_dict(_time_window)

        post_v2_extranet_lan_segments_usage_top_body = cls(
            id=id,
            is_b2b=is_b2b,
            is_provider=is_provider,
            time_window=time_window,
        )

        post_v2_extranet_lan_segments_usage_top_body.additional_properties = d
        return post_v2_extranet_lan_segments_usage_top_body

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
