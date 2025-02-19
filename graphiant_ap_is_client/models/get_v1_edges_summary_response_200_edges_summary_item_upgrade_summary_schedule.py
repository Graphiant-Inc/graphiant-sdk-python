from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule_ts import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule_version import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion,
    )


T = TypeVar("T", bound="GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule")


@_attrs_define
class GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule:
    """
    Attributes:
        action (Union[Unset, str]):  Example: TYPE_ENUM.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        download_progress (Union[Unset, str]):  Example: TYPE_UINT32.
        failure_reason (Union[Unset, str]):  Example: TYPE_STRING.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        ts (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs]):
        version (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion]):
    """

    action: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    download_progress: Union[Unset, str] = UNSET
    failure_reason: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    ts: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs"] = UNSET
    version: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        device_id = self.device_id

        download_progress = self.download_progress

        failure_reason = self.failure_reason

        state = self.state

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if download_progress is not UNSET:
            field_dict["downloadProgress"] = download_progress
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if state is not UNSET:
            field_dict["state"] = state
        if ts is not UNSET:
            field_dict["ts"] = ts
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule_ts import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule_version import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion,
        )

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        device_id = d.pop("deviceId", UNSET)

        download_progress = d.pop("downloadProgress", UNSET)

        failure_reason = d.pop("failureReason", UNSET)

        state = d.pop("state", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleTs.from_dict(_ts)

        _version = d.pop("version", UNSET)
        version: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryScheduleVersion.from_dict(_version)

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule = cls(
            action=action,
            device_id=device_id,
            download_progress=download_progress,
            failure_reason=failure_reason,
            state=state,
            ts=ts,
            version=version,
        )

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule.additional_properties = d
        return get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule

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
