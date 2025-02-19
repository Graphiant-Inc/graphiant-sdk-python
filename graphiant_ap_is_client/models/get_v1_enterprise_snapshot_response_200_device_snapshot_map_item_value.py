from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value_snapshots_item import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValueSnapshotsItem,
    )


T = TypeVar("T", bound="GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue")


@_attrs_define
class GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue:
    """
    Attributes:
        count (Union[Unset, str]):  Example: TYPE_INT32.
        snapshots (Union[Unset, list['GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValueSnapshotsItem']]):
    """

    count: Union[Unset, str] = UNSET
    snapshots: Union[Unset, list["GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValueSnapshotsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value_snapshots_item import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValueSnapshotsItem,
        )

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        snapshots = []
        _snapshots = d.pop("snapshots", UNSET)
        for snapshots_item_data in _snapshots or []:
            snapshots_item = GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValueSnapshotsItem.from_dict(
                snapshots_item_data
            )

            snapshots.append(snapshots_item)

        get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value = cls(
            count=count,
            snapshots=snapshots,
        )

        get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value.additional_properties = d
        return get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value

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
