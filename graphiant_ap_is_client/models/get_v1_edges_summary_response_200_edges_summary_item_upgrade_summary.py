from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_last_discovered_ts import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_last_upgrade_ts import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_running_version import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule,
    )


T = TypeVar("T", bound="GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary")


@_attrs_define
class GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        last_discovered_ts (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs]):
        last_upgrade_ts (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs]):
        running_version (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion]):
        schedule (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    last_discovered_ts: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs"] = (
        UNSET
    )
    last_upgrade_ts: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs"] = UNSET
    running_version: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion"] = UNSET
    schedule: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule"] = UNSET
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
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_last_discovered_ts import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_last_upgrade_ts import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_running_version import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_schedule import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _last_discovered_ts = d.pop("lastDiscoveredTs", UNSET)
        last_discovered_ts: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs]
        if isinstance(_last_discovered_ts, Unset):
            last_discovered_ts = UNSET
        else:
            last_discovered_ts = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastDiscoveredTs.from_dict(
                _last_discovered_ts
            )

        _last_upgrade_ts = d.pop("lastUpgradeTs", UNSET)
        last_upgrade_ts: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs]
        if isinstance(_last_upgrade_ts, Unset):
            last_upgrade_ts = UNSET
        else:
            last_upgrade_ts = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryLastUpgradeTs.from_dict(
                _last_upgrade_ts
            )

        _running_version = d.pop("runningVersion", UNSET)
        running_version: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion]
        if isinstance(_running_version, Unset):
            running_version = UNSET
        else:
            running_version = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion.from_dict(
                _running_version
            )

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummarySchedule.from_dict(_schedule)

        status = d.pop("status", UNSET)

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary = cls(
            device_id=device_id,
            last_discovered_ts=last_discovered_ts,
            last_upgrade_ts=last_upgrade_ts,
            running_version=running_version,
            schedule=schedule,
            status=status,
        )

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary.additional_properties = d
        return get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary

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
