from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_summary_response_200_sites_item_devices_item import (
        GetV1DevicesSummaryResponse200SitesItemDevicesItem,
    )


T = TypeVar("T", bound="GetV1DevicesSummaryResponse200SitesItem")


@_attrs_define
class GetV1DevicesSummaryResponse200SitesItem:
    """
    Attributes:
        devices (Union[Unset, list['GetV1DevicesSummaryResponse200SitesItemDevicesItem']]):
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    devices: Union[Unset, list["GetV1DevicesSummaryResponse200SitesItemDevicesItem"]] = UNSET
    site_id: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        site_id = self.site_id

        site_name = self.site_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_summary_response_200_sites_item_devices_item import (
            GetV1DevicesSummaryResponse200SitesItemDevicesItem,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1DevicesSummaryResponse200SitesItemDevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        get_v1_devices_summary_response_200_sites_item = cls(
            devices=devices,
            site_id=site_id,
            site_name=site_name,
        )

        get_v1_devices_summary_response_200_sites_item.additional_properties = d
        return get_v1_devices_summary_response_200_sites_item

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
