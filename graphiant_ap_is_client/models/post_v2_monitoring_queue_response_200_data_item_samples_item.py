from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_queue_response_200_data_item_samples_item_ts import (
        PostV2MonitoringQueueResponse200DataItemSamplesItemTs,
    )


T = TypeVar("T", bound="PostV2MonitoringQueueResponse200DataItemSamplesItem")


@_attrs_define
class PostV2MonitoringQueueResponse200DataItemSamplesItem:
    """
    Attributes:
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        ts (Union[Unset, PostV2MonitoringQueueResponse200DataItemSamplesItemTs]):
        value (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    status: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV2MonitoringQueueResponse200DataItemSamplesItemTs"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if ts is not UNSET:
            field_dict["ts"] = ts
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_queue_response_200_data_item_samples_item_ts import (
            PostV2MonitoringQueueResponse200DataItemSamplesItemTs,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2MonitoringQueueResponse200DataItemSamplesItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2MonitoringQueueResponse200DataItemSamplesItemTs.from_dict(_ts)

        value = d.pop("value", UNSET)

        post_v2_monitoring_queue_response_200_data_item_samples_item = cls(
            status=status,
            ts=ts,
            value=value,
        )

        post_v2_monitoring_queue_response_200_data_item_samples_item.additional_properties = d
        return post_v2_monitoring_queue_response_200_data_item_samples_item

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
