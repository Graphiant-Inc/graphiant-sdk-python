from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item_events_item_ts import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs,
    )


T = TypeVar("T", bound="PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem")


@_attrs_define
class PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItem:
    """
    Attributes:
        state (Union[Unset, str]):  Example: TYPE_STRING.
        state_id (Union[Unset, str]):  Example: TYPE_INT32.
        trace_session_id (Union[Unset, str]):  Example: TYPE_STRING.
        ts (Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs]):
    """

    state: Union[Unset, str] = UNSET
    state_id: Union[Unset, str] = UNSET
    trace_session_id: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        state_id = self.state_id

        trace_session_id = self.trace_session_id

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if state_id is not UNSET:
            field_dict["stateId"] = state_id
        if trace_session_id is not UNSET:
            field_dict["traceSessionId"] = trace_session_id
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item_events_item_ts import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs,
        )

        d = src_dict.copy()
        state = d.pop("state", UNSET)

        state_id = d.pop("stateId", UNSET)

        trace_session_id = d.pop("traceSessionId", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1ActivityLogsResponse200DetailsItemTargetsItemEventsItemTs.from_dict(_ts)

        post_v1_activity_logs_response_200_details_item_targets_item_events_item = cls(
            state=state,
            state_id=state_id,
            trace_session_id=trace_session_id,
            ts=ts,
        )

        post_v1_activity_logs_response_200_details_item_targets_item_events_item.additional_properties = d
        return post_v1_activity_logs_response_200_details_item_targets_item_events_item

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
