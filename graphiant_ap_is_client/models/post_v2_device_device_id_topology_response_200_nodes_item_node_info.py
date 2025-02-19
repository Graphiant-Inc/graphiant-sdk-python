from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_topology_response_200_nodes_item_node_info_uptime import (
        PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo")


@_attrs_define
class PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfo:
    """
    Attributes:
        control_quality (Union[Unset, str]):  Example: TYPE_ENUM.
        cpu (Union[Unset, str]):  Example: TYPE_FLOAT.
        data_quality (Union[Unset, str]):  Example: TYPE_ENUM.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        location (Union[Unset, str]):  Example: TYPE_STRING.
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        memory (Union[Unset, str]):  Example: TYPE_FLOAT.
        mgmt_ip (Union[Unset, str]):  Example: TYPE_STRING.
        model (Union[Unset, str]):  Example: TYPE_STRING.
        portal_quality (Union[Unset, str]):  Example: TYPE_ENUM.
        serial_number (Union[Unset, str]):  Example: TYPE_STRING.
        software_version (Union[Unset, str]):  Example: TYPE_STRING.
        staging_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        temperature (Union[Unset, str]):  Example: TYPE_FLOAT.
        uptime (Union[Unset, PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime]):
    """

    control_quality: Union[Unset, str] = UNSET
    cpu: Union[Unset, str] = UNSET
    data_quality: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    mgmt_ip: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    portal_quality: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    software_version: Union[Unset, str] = UNSET
    staging_mode: Union[Unset, str] = UNSET
    temperature: Union[Unset, str] = UNSET
    uptime: Union[Unset, "PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_quality = self.control_quality

        cpu = self.cpu

        data_quality = self.data_quality

        device_id = self.device_id

        hostname = self.hostname

        location = self.location

        maintenance_mode = self.maintenance_mode

        memory = self.memory

        mgmt_ip = self.mgmt_ip

        model = self.model

        portal_quality = self.portal_quality

        serial_number = self.serial_number

        software_version = self.software_version

        staging_mode = self.staging_mode

        temperature = self.temperature

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_quality is not UNSET:
            field_dict["controlQuality"] = control_quality
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if data_quality is not UNSET:
            field_dict["dataQuality"] = data_quality
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if location is not UNSET:
            field_dict["location"] = location
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if memory is not UNSET:
            field_dict["memory"] = memory
        if mgmt_ip is not UNSET:
            field_dict["mgmtIp"] = mgmt_ip
        if model is not UNSET:
            field_dict["model"] = model
        if portal_quality is not UNSET:
            field_dict["portalQuality"] = portal_quality
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if staging_mode is not UNSET:
            field_dict["stagingMode"] = staging_mode
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if uptime is not UNSET:
            field_dict["uptime"] = uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_topology_response_200_nodes_item_node_info_uptime import (
            PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime,
        )

        d = src_dict.copy()
        control_quality = d.pop("controlQuality", UNSET)

        cpu = d.pop("cpu", UNSET)

        data_quality = d.pop("dataQuality", UNSET)

        device_id = d.pop("deviceId", UNSET)

        hostname = d.pop("hostname", UNSET)

        location = d.pop("location", UNSET)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        memory = d.pop("memory", UNSET)

        mgmt_ip = d.pop("mgmtIp", UNSET)

        model = d.pop("model", UNSET)

        portal_quality = d.pop("portalQuality", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        staging_mode = d.pop("stagingMode", UNSET)

        temperature = d.pop("temperature", UNSET)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = PostV2DeviceDeviceIdTopologyResponse200NodesItemNodeInfoUptime.from_dict(_uptime)

        post_v2_device_device_id_topology_response_200_nodes_item_node_info = cls(
            control_quality=control_quality,
            cpu=cpu,
            data_quality=data_quality,
            device_id=device_id,
            hostname=hostname,
            location=location,
            maintenance_mode=maintenance_mode,
            memory=memory,
            mgmt_ip=mgmt_ip,
            model=model,
            portal_quality=portal_quality,
            serial_number=serial_number,
            software_version=software_version,
            staging_mode=staging_mode,
            temperature=temperature,
            uptime=uptime,
        )

        post_v2_device_device_id_topology_response_200_nodes_item_node_info.additional_properties = d
        return post_v2_device_device_id_topology_response_200_nodes_item_node_info

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
