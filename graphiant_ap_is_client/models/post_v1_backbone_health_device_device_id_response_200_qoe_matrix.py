from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix:
    """
    Attributes:
        devices (Union[Unset, list['PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem']]):
        qoe_matrix (Union[Unset, list['PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem']]):
    """

    devices: Union[Unset, list["PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem"]] = UNSET
    qoe_matrix: Union[Unset, list["PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        qoe_matrix: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.qoe_matrix, Unset):
            qoe_matrix = []
            for qoe_matrix_item_data in self.qoe_matrix:
                qoe_matrix_item = qoe_matrix_item_data.to_dict()
                qoe_matrix.append(qoe_matrix_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if qoe_matrix is not UNSET:
            field_dict["qoeMatrix"] = qoe_matrix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_devices_item import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixDevicesItem.from_dict(
                devices_item_data
            )

            devices.append(devices_item)

        qoe_matrix = []
        _qoe_matrix = d.pop("qoeMatrix", UNSET)
        for qoe_matrix_item_data in _qoe_matrix or []:
            qoe_matrix_item = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem.from_dict(
                qoe_matrix_item_data
            )

            qoe_matrix.append(qoe_matrix_item)

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix = cls(
            devices=devices,
            qoe_matrix=qoe_matrix,
        )

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_qoe_matrix

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
