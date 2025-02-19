from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_snapshot_device_id_response_200_snapshots_item import (
        GetV1DeviceSnapshotDeviceIdResponse200SnapshotsItem,
    )


T = TypeVar("T", bound="GetV1DeviceSnapshotDeviceIdResponse200")


@_attrs_define
class GetV1DeviceSnapshotDeviceIdResponse200:
    """
    Attributes:
        snapshots (Union[Unset, list['GetV1DeviceSnapshotDeviceIdResponse200SnapshotsItem']]):
    """

    snapshots: Union[Unset, list["GetV1DeviceSnapshotDeviceIdResponse200SnapshotsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_snapshot_device_id_response_200_snapshots_item import (
            GetV1DeviceSnapshotDeviceIdResponse200SnapshotsItem,
        )

        d = src_dict.copy()
        snapshots = []
        _snapshots = d.pop("snapshots", UNSET)
        for snapshots_item_data in _snapshots or []:
            snapshots_item = GetV1DeviceSnapshotDeviceIdResponse200SnapshotsItem.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        get_v1_device_snapshot_device_id_response_200 = cls(
            snapshots=snapshots,
        )

        get_v1_device_snapshot_device_id_response_200.additional_properties = d
        return get_v1_device_snapshot_device_id_response_200

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
