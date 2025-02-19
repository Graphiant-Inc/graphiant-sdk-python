from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_system_plane_cpu_item_time import (
        PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItem:
    """
    Attributes:
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        peer_name (Union[Unset, str]):  Example: TYPE_STRING.
        time (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime]):
        value (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    interface_name: Union[Unset, str] = UNSET
    peer_name: Union[Unset, str] = UNSET
    time: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_name = self.interface_name

        peer_name = self.peer_name

        time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if peer_name is not UNSET:
            field_dict["peerName"] = peer_name
        if time is not UNSET:
            field_dict["time"] = time
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_system_plane_cpu_item_time import (
            PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime,
        )

        d = src_dict.copy()
        interface_name = d.pop("interfaceName", UNSET)

        peer_name = d.pop("peerName", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlaneCpuItemTime.from_dict(_time)

        value = d.pop("value", UNSET)

        post_v1_backbone_health_device_device_id_response_200_system_plane_cpu_item = cls(
            interface_name=interface_name,
            peer_name=peer_name,
            time=time,
            value=value,
        )

        post_v1_backbone_health_device_device_id_response_200_system_plane_cpu_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_system_plane_cpu_item

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
