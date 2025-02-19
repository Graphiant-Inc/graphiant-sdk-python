from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_logs_response_200_histogram_item_ts import PostV1LogsResponse200HistogramItemTs


T = TypeVar("T", bound="PostV1LogsResponse200HistogramItem")


@_attrs_define
class PostV1LogsResponse200HistogramItem:
    """
    Attributes:
        count (Union[Unset, str]):  Example: TYPE_UINT32.
        ts (Union[Unset, PostV1LogsResponse200HistogramItemTs]):
    """

    count: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1LogsResponse200HistogramItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_logs_response_200_histogram_item_ts import PostV1LogsResponse200HistogramItemTs

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1LogsResponse200HistogramItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1LogsResponse200HistogramItemTs.from_dict(_ts)

        post_v1_logs_response_200_histogram_item = cls(
            count=count,
            ts=ts,
        )

        post_v1_logs_response_200_histogram_item.additional_properties = d
        return post_v1_logs_response_200_histogram_item

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
