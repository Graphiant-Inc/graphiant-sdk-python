from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_bandwidth_response_200_stats_item_ts import PostV1AppsBandwidthResponse200StatsItemTs


T = TypeVar("T", bound="PostV1AppsBandwidthResponse200StatsItem")


@_attrs_define
class PostV1AppsBandwidthResponse200StatsItem:
    """
    Attributes:
        dl_bw (Union[Unset, str]):  Example: TYPE_DOUBLE.
        ts (Union[Unset, PostV1AppsBandwidthResponse200StatsItemTs]):
        ul_bw (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    dl_bw: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1AppsBandwidthResponse200StatsItemTs"] = UNSET
    ul_bw: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dl_bw = self.dl_bw

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        ul_bw = self.ul_bw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dl_bw is not UNSET:
            field_dict["dlBw"] = dl_bw
        if ts is not UNSET:
            field_dict["ts"] = ts
        if ul_bw is not UNSET:
            field_dict["ulBw"] = ul_bw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_bandwidth_response_200_stats_item_ts import PostV1AppsBandwidthResponse200StatsItemTs

        d = src_dict.copy()
        dl_bw = d.pop("dlBw", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1AppsBandwidthResponse200StatsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1AppsBandwidthResponse200StatsItemTs.from_dict(_ts)

        ul_bw = d.pop("ulBw", UNSET)

        post_v1_apps_bandwidth_response_200_stats_item = cls(
            dl_bw=dl_bw,
            ts=ts,
            ul_bw=ul_bw,
        )

        post_v1_apps_bandwidth_response_200_stats_item.additional_properties = d
        return post_v1_apps_bandwidth_response_200_stats_item

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
