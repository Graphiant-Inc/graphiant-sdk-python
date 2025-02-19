from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem")


@_attrs_define
class GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        host_name (Union[Unset, str]):  Example: TYPE_STRING.
        num_interfaces (Union[Unset, str]):  Example: TYPE_INT32.
        site (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    device_id: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    num_interfaces: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        host_name = self.host_name

        num_interfaces = self.num_interfaces

        site = self.site

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if num_interfaces is not UNSET:
            field_dict["numInterfaces"] = num_interfaces
        if site is not UNSET:
            field_dict["site"] = site
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        host_name = d.pop("hostName", UNSET)

        num_interfaces = d.pop("numInterfaces", UNSET)

        site = d.pop("site", UNSET)

        status = d.pop("status", UNSET)

        get_v1_global_lan_segments_vrf_id_devices_response_200_entries_item = cls(
            device_id=device_id,
            host_name=host_name,
            num_interfaces=num_interfaces,
            site=site,
            status=status,
        )

        get_v1_global_lan_segments_vrf_id_devices_response_200_entries_item.additional_properties = d
        return get_v1_global_lan_segments_vrf_id_devices_response_200_entries_item

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
