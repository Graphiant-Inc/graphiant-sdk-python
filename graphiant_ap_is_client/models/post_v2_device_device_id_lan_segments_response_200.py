from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item import (
        PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdLanSegmentsResponse200")


@_attrs_define
class PostV2DeviceDeviceIdLanSegmentsResponse200:
    """
    Attributes:
        device_segments (Union[Unset, list['PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem']]):
    """

    device_segments: Union[Unset, list["PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_segments, Unset):
            device_segments = []
            for device_segments_item_data in self.device_segments:
                device_segments_item = device_segments_item_data.to_dict()
                device_segments.append(device_segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_segments is not UNSET:
            field_dict["deviceSegments"] = device_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item import (
            PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem,
        )

        d = src_dict.copy()
        device_segments = []
        _device_segments = d.pop("deviceSegments", UNSET)
        for device_segments_item_data in _device_segments or []:
            device_segments_item = PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem.from_dict(
                device_segments_item_data
            )

            device_segments.append(device_segments_item)

        post_v2_device_device_id_lan_segments_response_200 = cls(
            device_segments=device_segments,
        )

        post_v2_device_device_id_lan_segments_response_200.additional_properties = d
        return post_v2_device_device_id_lan_segments_response_200

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
