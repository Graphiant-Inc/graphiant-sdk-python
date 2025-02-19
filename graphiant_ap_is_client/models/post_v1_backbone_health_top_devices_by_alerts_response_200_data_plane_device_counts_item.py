from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlaneDeviceCountsItem")


@_attrs_define
class PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlaneDeviceCountsItem:
    """
    Attributes:
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        num_alerts (Union[Unset, str]):  Example: TYPE_INT32.
    """

    device_name: Union[Unset, str] = UNSET
    num_alerts: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        num_alerts = self.num_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if num_alerts is not UNSET:
            field_dict["numAlerts"] = num_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_name = d.pop("deviceName", UNSET)

        num_alerts = d.pop("numAlerts", UNSET)

        post_v1_backbone_health_top_devices_by_alerts_response_200_data_plane_device_counts_item = cls(
            device_name=device_name,
            num_alerts=num_alerts,
        )

        post_v1_backbone_health_top_devices_by_alerts_response_200_data_plane_device_counts_item.additional_properties = d
        return post_v1_backbone_health_top_devices_by_alerts_response_200_data_plane_device_counts_item

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
