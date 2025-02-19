from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem")


@_attrs_define
class GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        device_status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    device_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        device_status = self.device_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_status = d.pop("deviceStatus", UNSET)

        get_v1_troubleshooting_site_site_id_response_200_edge_statuses_item = cls(
            device_id=device_id,
            device_name=device_name,
            device_status=device_status,
        )

        get_v1_troubleshooting_site_site_id_response_200_edge_statuses_item.additional_properties = d
        return get_v1_troubleshooting_site_site_id_response_200_edge_statuses_item

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
