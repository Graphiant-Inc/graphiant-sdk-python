from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane_device_counts_item import (
        PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlaneDeviceCountsItem,
    )


T = TypeVar("T", bound="PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane")


@_attrs_define
class PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane:
    """
    Attributes:
        device_counts (Union[Unset,
            list['PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlaneDeviceCountsItem']]):
    """

    device_counts: Union[
        Unset, list["PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlaneDeviceCountsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_counts, Unset):
            device_counts = []
            for device_counts_item_data in self.device_counts:
                device_counts_item = device_counts_item_data.to_dict()
                device_counts.append(device_counts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_counts is not UNSET:
            field_dict["deviceCounts"] = device_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane_device_counts_item import (
            PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlaneDeviceCountsItem,
        )

        d = src_dict.copy()
        device_counts = []
        _device_counts = d.pop("deviceCounts", UNSET)
        for device_counts_item_data in _device_counts or []:
            device_counts_item = PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlaneDeviceCountsItem.from_dict(
                device_counts_item_data
            )

            device_counts.append(device_counts_item)

        post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane = cls(
            device_counts=device_counts,
        )

        post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane.additional_properties = d
        return post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane

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
