from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item_end_time import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item_start_time import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem:
    """
    Attributes:
        delay_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        end_time (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime]):
        jitter_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        loss_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        start_time (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        value (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    delay_value: Union[Unset, str] = UNSET
    end_time: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime"] = UNSET
    jitter_value: Union[Unset, str] = UNSET
    loss_value: Union[Unset, str] = UNSET
    start_time: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime"] = (
        UNSET
    )
    status: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_value = self.delay_value

        end_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        jitter_value = self.jitter_value

        loss_value = self.loss_value

        start_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        status = self.status

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_value is not UNSET:
            field_dict["delayValue"] = delay_value
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if jitter_value is not UNSET:
            field_dict["jitterValue"] = jitter_value
        if loss_value is not UNSET:
            field_dict["lossValue"] = loss_value
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item_end_time import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item_start_time import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime,
        )

        d = src_dict.copy()
        delay_value = d.pop("delayValue", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemEndTime.from_dict(
                _end_time
            )

        jitter_value = d.pop("jitterValue", UNSET)

        loss_value = d.pop("lossValue", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItemStartTime.from_dict(
                _start_time
            )

        status = d.pop("status", UNSET)

        value = d.pop("value", UNSET)

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item = cls(
            delay_value=delay_value,
            end_time=end_time,
            jitter_value=jitter_value,
            loss_value=loss_value,
            start_time=start_time,
            status=status,
            value=value,
        )

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item

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
