from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_sites_site_id_devices_response_200_device_item_uptime import (
        GetV1SitesSiteIdDevicesResponse200DeviceItemUptime,
    )


T = TypeVar("T", bound="GetV1SitesSiteIdDevicesResponse200DeviceItem")


@_attrs_define
class GetV1SitesSiteIdDevicesResponse200DeviceItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        location (Union[Unset, str]):  Example: TYPE_STRING.
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        management_ip (Union[Unset, str]):  Example: TYPE_STRING.
        model (Union[Unset, str]):  Example: TYPE_STRING.
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        serial_number (Union[Unset, str]):  Example: TYPE_STRING.
        site_id (Union[Unset, str]):  Example: TYPE_UINT64.
        software_version (Union[Unset, str]):  Example: TYPE_STRING.
        staging_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        uptime (Union[Unset, GetV1SitesSiteIdDevicesResponse200DeviceItemUptime]):
        vrrp_interface (Union[Unset, str]):  Example: TYPE_STRING.
        vrrp_state (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    management_ip: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    software_version: Union[Unset, str] = UNSET
    staging_mode: Union[Unset, str] = UNSET
    uptime: Union[Unset, "GetV1SitesSiteIdDevicesResponse200DeviceItemUptime"] = UNSET
    vrrp_interface: Union[Unset, str] = UNSET
    vrrp_state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        hostname = self.hostname

        location = self.location

        maintenance_mode = self.maintenance_mode

        management_ip = self.management_ip

        model = self.model

        role = self.role

        serial_number = self.serial_number

        site_id = self.site_id

        software_version = self.software_version

        staging_mode = self.staging_mode

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        vrrp_interface = self.vrrp_interface

        vrrp_state = self.vrrp_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if location is not UNSET:
            field_dict["location"] = location
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if management_ip is not UNSET:
            field_dict["managementIp"] = management_ip
        if model is not UNSET:
            field_dict["model"] = model
        if role is not UNSET:
            field_dict["role"] = role
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if staging_mode is not UNSET:
            field_dict["stagingMode"] = staging_mode
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if vrrp_interface is not UNSET:
            field_dict["vrrpInterface"] = vrrp_interface
        if vrrp_state is not UNSET:
            field_dict["vrrpState"] = vrrp_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_sites_site_id_devices_response_200_device_item_uptime import (
            GetV1SitesSiteIdDevicesResponse200DeviceItemUptime,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        hostname = d.pop("hostname", UNSET)

        location = d.pop("location", UNSET)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        management_ip = d.pop("managementIp", UNSET)

        model = d.pop("model", UNSET)

        role = d.pop("role", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        site_id = d.pop("siteId", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        staging_mode = d.pop("stagingMode", UNSET)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, GetV1SitesSiteIdDevicesResponse200DeviceItemUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = GetV1SitesSiteIdDevicesResponse200DeviceItemUptime.from_dict(_uptime)

        vrrp_interface = d.pop("vrrpInterface", UNSET)

        vrrp_state = d.pop("vrrpState", UNSET)

        get_v1_sites_site_id_devices_response_200_device_item = cls(
            device_id=device_id,
            hostname=hostname,
            location=location,
            maintenance_mode=maintenance_mode,
            management_ip=management_ip,
            model=model,
            role=role,
            serial_number=serial_number,
            site_id=site_id,
            software_version=software_version,
            staging_mode=staging_mode,
            uptime=uptime,
            vrrp_interface=vrrp_interface,
            vrrp_state=vrrp_state,
        )

        get_v1_sites_site_id_devices_response_200_device_item.additional_properties = d
        return get_v1_sites_site_id_devices_response_200_device_item

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
