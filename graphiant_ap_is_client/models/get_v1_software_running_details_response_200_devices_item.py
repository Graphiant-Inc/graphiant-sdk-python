from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SoftwareRunningDetailsResponse200DevicesItem")


@_attrs_define
class GetV1SoftwareRunningDetailsResponse200DevicesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_id: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    enterprise_name: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        enterprise_id = self.enterprise_id

        enterprise_name = self.enterprise_name

        hostname = self.hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if enterprise_name is not UNSET:
            field_dict["enterpriseName"] = enterprise_name
        if hostname is not UNSET:
            field_dict["hostname"] = hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        enterprise_name = d.pop("enterpriseName", UNSET)

        hostname = d.pop("hostname", UNSET)

        get_v1_software_running_details_response_200_devices_item = cls(
            device_id=device_id,
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            hostname=hostname,
        )

        get_v1_software_running_details_response_200_devices_item.additional_properties = d
        return get_v1_software_running_details_response_200_devices_item

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
