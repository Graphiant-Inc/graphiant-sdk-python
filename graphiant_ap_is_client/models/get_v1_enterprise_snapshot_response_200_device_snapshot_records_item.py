from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItem,
    )
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_uptime import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime,
    )


T = TypeVar("T", bound="GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem")


@_attrs_define
class GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, str]):  Example: TYPE_STRING.
        site (Union[Unset, str]):  Example: TYPE_STRING.
        snapshot_count (Union[Unset, str]):  Example: TYPE_UINT32.
        snapshots (Union[Unset, list['GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItem']]):
        uptime (Union[Unset, GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime]):
    """

    device_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    snapshot_count: Union[Unset, str] = UNSET
    snapshots: Union[Unset, list["GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItem"]] = UNSET
    uptime: Union[Unset, "GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        hostname = self.hostname

        region = self.region

        site = self.site

        snapshot_count = self.snapshot_count

        snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if region is not UNSET:
            field_dict["region"] = region
        if site is not UNSET:
            field_dict["site"] = site
        if snapshot_count is not UNSET:
            field_dict["snapshotCount"] = snapshot_count
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots
        if uptime is not UNSET:
            field_dict["uptime"] = uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItem,
        )
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_uptime import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        hostname = d.pop("hostname", UNSET)

        region = d.pop("region", UNSET)

        site = d.pop("site", UNSET)

        snapshot_count = d.pop("snapshotCount", UNSET)

        snapshots = []
        _snapshots = d.pop("snapshots", UNSET)
        for snapshots_item_data in _snapshots or []:
            snapshots_item = GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItem.from_dict(
                snapshots_item_data
            )

            snapshots.append(snapshots_item)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemUptime.from_dict(_uptime)

        get_v1_enterprise_snapshot_response_200_device_snapshot_records_item = cls(
            device_id=device_id,
            hostname=hostname,
            region=region,
            site=site,
            snapshot_count=snapshot_count,
            snapshots=snapshots,
            uptime=uptime,
        )

        get_v1_enterprise_snapshot_response_200_device_snapshot_records_item.additional_properties = d
        return get_v1_enterprise_snapshot_response_200_device_snapshot_records_item

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
