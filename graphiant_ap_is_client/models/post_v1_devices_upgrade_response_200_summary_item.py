from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_upgrade_response_200_summary_item_last_discovered_ts import (
        PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs,
    )
    from ..models.post_v1_devices_upgrade_response_200_summary_item_last_upgrade_ts import (
        PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs,
    )
    from ..models.post_v1_devices_upgrade_response_200_summary_item_running_version import (
        PostV1DevicesUpgradeResponse200SummaryItemRunningVersion,
    )
    from ..models.post_v1_devices_upgrade_response_200_summary_item_schedule import (
        PostV1DevicesUpgradeResponse200SummaryItemSchedule,
    )


T = TypeVar("T", bound="PostV1DevicesUpgradeResponse200SummaryItem")


@_attrs_define
class PostV1DevicesUpgradeResponse200SummaryItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        last_discovered_ts (Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs]):
        last_upgrade_ts (Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs]):
        running_version (Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemRunningVersion]):
        schedule (Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemSchedule]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    last_discovered_ts: Union[Unset, "PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs"] = UNSET
    last_upgrade_ts: Union[Unset, "PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs"] = UNSET
    running_version: Union[Unset, "PostV1DevicesUpgradeResponse200SummaryItemRunningVersion"] = UNSET
    schedule: Union[Unset, "PostV1DevicesUpgradeResponse200SummaryItemSchedule"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        last_discovered_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_discovered_ts, Unset):
            last_discovered_ts = self.last_discovered_ts.to_dict()

        last_upgrade_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_upgrade_ts, Unset):
            last_upgrade_ts = self.last_upgrade_ts.to_dict()

        running_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.running_version, Unset):
            running_version = self.running_version.to_dict()

        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if last_discovered_ts is not UNSET:
            field_dict["lastDiscoveredTs"] = last_discovered_ts
        if last_upgrade_ts is not UNSET:
            field_dict["lastUpgradeTs"] = last_upgrade_ts
        if running_version is not UNSET:
            field_dict["runningVersion"] = running_version
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_upgrade_response_200_summary_item_last_discovered_ts import (
            PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs,
        )
        from ..models.post_v1_devices_upgrade_response_200_summary_item_last_upgrade_ts import (
            PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs,
        )
        from ..models.post_v1_devices_upgrade_response_200_summary_item_running_version import (
            PostV1DevicesUpgradeResponse200SummaryItemRunningVersion,
        )
        from ..models.post_v1_devices_upgrade_response_200_summary_item_schedule import (
            PostV1DevicesUpgradeResponse200SummaryItemSchedule,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _last_discovered_ts = d.pop("lastDiscoveredTs", UNSET)
        last_discovered_ts: Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs]
        if isinstance(_last_discovered_ts, Unset):
            last_discovered_ts = UNSET
        else:
            last_discovered_ts = PostV1DevicesUpgradeResponse200SummaryItemLastDiscoveredTs.from_dict(
                _last_discovered_ts
            )

        _last_upgrade_ts = d.pop("lastUpgradeTs", UNSET)
        last_upgrade_ts: Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs]
        if isinstance(_last_upgrade_ts, Unset):
            last_upgrade_ts = UNSET
        else:
            last_upgrade_ts = PostV1DevicesUpgradeResponse200SummaryItemLastUpgradeTs.from_dict(_last_upgrade_ts)

        _running_version = d.pop("runningVersion", UNSET)
        running_version: Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemRunningVersion]
        if isinstance(_running_version, Unset):
            running_version = UNSET
        else:
            running_version = PostV1DevicesUpgradeResponse200SummaryItemRunningVersion.from_dict(_running_version)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, PostV1DevicesUpgradeResponse200SummaryItemSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = PostV1DevicesUpgradeResponse200SummaryItemSchedule.from_dict(_schedule)

        status = d.pop("status", UNSET)

        post_v1_devices_upgrade_response_200_summary_item = cls(
            device_id=device_id,
            last_discovered_ts=last_discovered_ts,
            last_upgrade_ts=last_upgrade_ts,
            running_version=running_version,
            schedule=schedule,
            status=status,
        )

        post_v1_devices_upgrade_response_200_summary_item.additional_properties = d
        return post_v1_devices_upgrade_response_200_summary_item

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
