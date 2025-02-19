from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane_session_slas_item_values_item_time import (
        PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem:
    """
    Attributes:
        delay_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        jitter_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        loss_value (Union[Unset, str]):  Example: TYPE_DOUBLE.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        time (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime]):
        value (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    delay_value: Union[Unset, str] = UNSET
    jitter_value: Union[Unset, str] = UNSET
    loss_value: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    time: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_value = self.delay_value

        jitter_value = self.jitter_value

        loss_value = self.loss_value

        status = self.status

        time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_value is not UNSET:
            field_dict["delayValue"] = delay_value
        if jitter_value is not UNSET:
            field_dict["jitterValue"] = jitter_value
        if loss_value is not UNSET:
            field_dict["lossValue"] = loss_value
        if status is not UNSET:
            field_dict["status"] = status
        if time is not UNSET:
            field_dict["time"] = time
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane_session_slas_item_values_item_time import (
            PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime,
        )

        d = src_dict.copy()
        delay_value = d.pop("delayValue", UNSET)

        jitter_value = d.pop("jitterValue", UNSET)

        loss_value = d.pop("lossValue", UNSET)

        status = d.pop("status", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItemTime.from_dict(_time)

        value = d.pop("value", UNSET)

        post_v1_backbone_health_device_device_id_response_200_data_plane_session_slas_item_values_item = cls(
            delay_value=delay_value,
            jitter_value=jitter_value,
            loss_value=loss_value,
            status=status,
            time=time,
            value=value,
        )

        post_v1_backbone_health_device_device_id_response_200_data_plane_session_slas_item_values_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_data_plane_session_slas_item_values_item

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
