from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item_region import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion]):
    """

    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    region: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item_region import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItemRegion.from_dict(_region)

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item = cls(
            device_id=device_id,
            device_name=device_name,
            region=region,
        )

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item

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
