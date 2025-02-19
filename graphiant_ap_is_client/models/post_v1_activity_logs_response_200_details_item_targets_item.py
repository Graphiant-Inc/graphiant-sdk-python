from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item_end_ts import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item_events_item import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item_ids_item import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItemIdsItem,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item_start_ts import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs,
    )


T = TypeVar("T", bound="PostV1ActivityLogsResponse200DetailsItemTargetsItem")


@_attrs_define
class PostV1ActivityLogsResponse200DetailsItemTargetsItem:
    """
    Attributes:
        detailed_failure_reason (Union[Unset, str]):  Example: TYPE_STRING.
        end_ts (Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs]):
        events (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem']]):
        failure_reason (Union[Unset, str]):  Example: TYPE_STRING.
        ids (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItemTargetsItemIdsItem']]):
        start_ts (Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    detailed_failure_reason: Union[Unset, str] = UNSET
    end_ts: Union[Unset, "PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs"] = UNSET
    events: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem"]] = UNSET
    failure_reason: Union[Unset, str] = UNSET
    ids: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItemTargetsItemIdsItem"]] = UNSET
    start_ts: Union[Unset, "PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detailed_failure_reason = self.detailed_failure_reason

        end_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_ts, Unset):
            end_ts = self.end_ts.to_dict()

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        failure_reason = self.failure_reason

        ids: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = ids_item_data.to_dict()
                ids.append(ids_item)

        start_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_ts, Unset):
            start_ts = self.start_ts.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detailed_failure_reason is not UNSET:
            field_dict["detailedFailureReason"] = detailed_failure_reason
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if events is not UNSET:
            field_dict["events"] = events
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if ids is not UNSET:
            field_dict["ids"] = ids
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item_end_ts import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item_events_item import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item_ids_item import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItemIdsItem,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item_start_ts import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs,
        )

        d = src_dict.copy()
        detailed_failure_reason = d.pop("detailedFailureReason", UNSET)

        _end_ts = d.pop("endTs", UNSET)
        end_ts: Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs]
        if isinstance(_end_ts, Unset):
            end_ts = UNSET
        else:
            end_ts = PostV1ActivityLogsResponse200DetailsItemTargetsItemEndTs.from_dict(_end_ts)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem.from_dict(events_item_data)

            events.append(events_item)

        failure_reason = d.pop("failureReason", UNSET)

        ids = []
        _ids = d.pop("ids", UNSET)
        for ids_item_data in _ids or []:
            ids_item = PostV1ActivityLogsResponse200DetailsItemTargetsItemIdsItem.from_dict(ids_item_data)

            ids.append(ids_item)

        _start_ts = d.pop("startTs", UNSET)
        start_ts: Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs]
        if isinstance(_start_ts, Unset):
            start_ts = UNSET
        else:
            start_ts = PostV1ActivityLogsResponse200DetailsItemTargetsItemStartTs.from_dict(_start_ts)

        status = d.pop("status", UNSET)

        post_v1_activity_logs_response_200_details_item_targets_item = cls(
            detailed_failure_reason=detailed_failure_reason,
            end_ts=end_ts,
            events=events,
            failure_reason=failure_reason,
            ids=ids,
            start_ts=start_ts,
            status=status,
        )

        post_v1_activity_logs_response_200_details_item_targets_item.additional_properties = d
        return post_v1_activity_logs_response_200_details_item_targets_item

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
