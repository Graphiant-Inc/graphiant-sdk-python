from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_topology_body_snapshot_time import (
        PostV2DeviceDeviceIdTopologyBodySnapshotTime,
    )
    from ..models.post_v2_device_device_id_topology_body_time_window import PostV2DeviceDeviceIdTopologyBodyTimeWindow


T = TypeVar("T", bound="PostV2DeviceDeviceIdTopologyBody")


@_attrs_define
class PostV2DeviceDeviceIdTopologyBody:
    """
    Attributes:
        snapshot_time (Union[Unset, PostV2DeviceDeviceIdTopologyBodySnapshotTime]):
        time_window (Union[Unset, PostV2DeviceDeviceIdTopologyBodyTimeWindow]):
    """

    snapshot_time: Union[Unset, "PostV2DeviceDeviceIdTopologyBodySnapshotTime"] = UNSET
    time_window: Union[Unset, "PostV2DeviceDeviceIdTopologyBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.snapshot_time, Unset):
            snapshot_time = self.snapshot_time.to_dict()

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_time is not UNSET:
            field_dict["snapshotTime"] = snapshot_time
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_topology_body_snapshot_time import (
            PostV2DeviceDeviceIdTopologyBodySnapshotTime,
        )
        from ..models.post_v2_device_device_id_topology_body_time_window import (
            PostV2DeviceDeviceIdTopologyBodyTimeWindow,
        )

        d = src_dict.copy()
        _snapshot_time = d.pop("snapshotTime", UNSET)
        snapshot_time: Union[Unset, PostV2DeviceDeviceIdTopologyBodySnapshotTime]
        if isinstance(_snapshot_time, Unset):
            snapshot_time = UNSET
        else:
            snapshot_time = PostV2DeviceDeviceIdTopologyBodySnapshotTime.from_dict(_snapshot_time)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2DeviceDeviceIdTopologyBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2DeviceDeviceIdTopologyBodyTimeWindow.from_dict(_time_window)

        post_v2_device_device_id_topology_body = cls(
            snapshot_time=snapshot_time,
            time_window=time_window,
        )

        post_v2_device_device_id_topology_body.additional_properties = d
        return post_v2_device_device_id_topology_body

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
