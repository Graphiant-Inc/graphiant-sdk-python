from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_app_summary_response_200_app_summary_app_incidents_data_item_ts import (
        PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs,
    )


T = TypeVar("T", bound="PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItem")


@_attrs_define
class PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItem:
    """
    Attributes:
        app_count (Union[Unset, str]):  Example: TYPE_UINT32.
        app_status (Union[Unset, str]):  Example: TYPE_ENUM.
        ts (Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs]):
    """

    app_count: Union[Unset, str] = UNSET
    app_status: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_count = self.app_count

        app_status = self.app_status

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_count is not UNSET:
            field_dict["appCount"] = app_count
        if app_status is not UNSET:
            field_dict["appStatus"] = app_status
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_app_summary_response_200_app_summary_app_incidents_data_item_ts import (
            PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs,
        )

        d = src_dict.copy()
        app_count = d.pop("appCount", UNSET)

        app_status = d.pop("appStatus", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1AppsAppSummaryResponse200AppSummaryAppIncidentsDataItemTs.from_dict(_ts)

        post_v1_apps_app_summary_response_200_app_summary_app_incidents_data_item = cls(
            app_count=app_count,
            app_status=app_status,
            ts=ts,
        )

        post_v1_apps_app_summary_response_200_app_summary_app_incidents_data_item.additional_properties = d
        return post_v1_apps_app_summary_response_200_app_summary_app_incidents_data_item

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
