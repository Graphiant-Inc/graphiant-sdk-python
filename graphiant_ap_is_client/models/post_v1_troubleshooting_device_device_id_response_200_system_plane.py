from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_cpu_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCpuItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_crashes_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCrashesItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_disk_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneDiskItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_maintenance_windows_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMaintenanceWindowsItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_memory_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMemoryItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_temperature_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_temperature_series_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureSeriesItem,
    )


T = TypeVar("T", bound="PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlane")


@_attrs_define
class PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlane:
    """
    Attributes:
        cpu (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCpuItem']]):
        crashes (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCrashesItem']]):
        disk (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneDiskItem']]):
        last_crash (Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash]):
        maintenance_windows (Union[Unset,
            list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMaintenanceWindowsItem']]):
        memory (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMemoryItem']]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        temperature (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureItem']]):
        temperature_series (Union[Unset,
            list['PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureSeriesItem']]):
    """

    cpu: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCpuItem"]] = UNSET
    crashes: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCrashesItem"]] = UNSET
    disk: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneDiskItem"]] = UNSET
    last_crash: Union[Unset, "PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash"] = UNSET
    maintenance_windows: Union[
        Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMaintenanceWindowsItem"]
    ] = UNSET
    memory: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMemoryItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    temperature: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureItem"]] = UNSET
    temperature_series: Union[
        Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureSeriesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = []
            for cpu_item_data in self.cpu:
                cpu_item = cpu_item_data.to_dict()
                cpu.append(cpu_item)

        crashes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.crashes, Unset):
            crashes = []
            for crashes_item_data in self.crashes:
                crashes_item = crashes_item_data.to_dict()
                crashes.append(crashes_item)

        disk: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.disk, Unset):
            disk = []
            for disk_item_data in self.disk:
                disk_item = disk_item_data.to_dict()
                disk.append(disk_item)

        last_crash: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_crash, Unset):
            last_crash = self.last_crash.to_dict()

        maintenance_windows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maintenance_windows, Unset):
            maintenance_windows = []
            for maintenance_windows_item_data in self.maintenance_windows:
                maintenance_windows_item = maintenance_windows_item_data.to_dict()
                maintenance_windows.append(maintenance_windows_item)

        memory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.memory, Unset):
            memory = []
            for memory_item_data in self.memory:
                memory_item = memory_item_data.to_dict()
                memory.append(memory_item)

        status = self.status

        temperature: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = []
            for temperature_item_data in self.temperature:
                temperature_item = temperature_item_data.to_dict()
                temperature.append(temperature_item)

        temperature_series: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.temperature_series, Unset):
            temperature_series = []
            for temperature_series_item_data in self.temperature_series:
                temperature_series_item = temperature_series_item_data.to_dict()
                temperature_series.append(temperature_series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if crashes is not UNSET:
            field_dict["crashes"] = crashes
        if disk is not UNSET:
            field_dict["disk"] = disk
        if last_crash is not UNSET:
            field_dict["lastCrash"] = last_crash
        if maintenance_windows is not UNSET:
            field_dict["maintenanceWindows"] = maintenance_windows
        if memory is not UNSET:
            field_dict["memory"] = memory
        if status is not UNSET:
            field_dict["status"] = status
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if temperature_series is not UNSET:
            field_dict["temperatureSeries"] = temperature_series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_cpu_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCpuItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_crashes_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCrashesItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_disk_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneDiskItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_maintenance_windows_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMaintenanceWindowsItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_memory_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMemoryItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_temperature_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_temperature_series_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureSeriesItem,
        )

        d = src_dict.copy()
        cpu = []
        _cpu = d.pop("cpu", UNSET)
        for cpu_item_data in _cpu or []:
            cpu_item = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCpuItem.from_dict(cpu_item_data)

            cpu.append(cpu_item)

        crashes = []
        _crashes = d.pop("crashes", UNSET)
        for crashes_item_data in _crashes or []:
            crashes_item = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneCrashesItem.from_dict(
                crashes_item_data
            )

            crashes.append(crashes_item)

        disk = []
        _disk = d.pop("disk", UNSET)
        for disk_item_data in _disk or []:
            disk_item = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneDiskItem.from_dict(disk_item_data)

            disk.append(disk_item)

        _last_crash = d.pop("lastCrash", UNSET)
        last_crash: Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash]
        if isinstance(_last_crash, Unset):
            last_crash = UNSET
        else:
            last_crash = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash.from_dict(_last_crash)

        maintenance_windows = []
        _maintenance_windows = d.pop("maintenanceWindows", UNSET)
        for maintenance_windows_item_data in _maintenance_windows or []:
            maintenance_windows_item = (
                PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMaintenanceWindowsItem.from_dict(
                    maintenance_windows_item_data
                )
            )

            maintenance_windows.append(maintenance_windows_item)

        memory = []
        _memory = d.pop("memory", UNSET)
        for memory_item_data in _memory or []:
            memory_item = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneMemoryItem.from_dict(
                memory_item_data
            )

            memory.append(memory_item)

        status = d.pop("status", UNSET)

        temperature = []
        _temperature = d.pop("temperature", UNSET)
        for temperature_item_data in _temperature or []:
            temperature_item = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureItem.from_dict(
                temperature_item_data
            )

            temperature.append(temperature_item)

        temperature_series = []
        _temperature_series = d.pop("temperatureSeries", UNSET)
        for temperature_series_item_data in _temperature_series or []:
            temperature_series_item = (
                PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneTemperatureSeriesItem.from_dict(
                    temperature_series_item_data
                )
            )

            temperature_series.append(temperature_series_item)

        post_v1_troubleshooting_device_device_id_response_200_system_plane = cls(
            cpu=cpu,
            crashes=crashes,
            disk=disk,
            last_crash=last_crash,
            maintenance_windows=maintenance_windows,
            memory=memory,
            status=status,
            temperature=temperature,
            temperature_series=temperature_series,
        )

        post_v1_troubleshooting_device_device_id_response_200_system_plane.additional_properties = d
        return post_v1_troubleshooting_device_device_id_response_200_system_plane

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
