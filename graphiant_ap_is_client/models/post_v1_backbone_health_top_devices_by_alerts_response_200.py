from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_control_plane import (
        PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane,
    )
    from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_data_plane import (
        PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane,
    )
    from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane import (
        PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane,
    )


T = TypeVar("T", bound="PostV1BackboneHealthTopDevicesByAlertsResponse200")


@_attrs_define
class PostV1BackboneHealthTopDevicesByAlertsResponse200:
    """
    Attributes:
        control_plane (Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane]):
        data_plane (Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane]):
        system_plane (Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane]):
    """

    control_plane: Union[Unset, "PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane"] = UNSET
    data_plane: Union[Unset, "PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane"] = UNSET
    system_plane: Union[Unset, "PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.control_plane, Unset):
            control_plane = self.control_plane.to_dict()

        data_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_plane, Unset):
            data_plane = self.data_plane.to_dict()

        system_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_plane, Unset):
            system_plane = self.system_plane.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_plane is not UNSET:
            field_dict["controlPlane"] = control_plane
        if data_plane is not UNSET:
            field_dict["dataPlane"] = data_plane
        if system_plane is not UNSET:
            field_dict["systemPlane"] = system_plane

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_control_plane import (
            PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane,
        )
        from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_data_plane import (
            PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane,
        )
        from ..models.post_v1_backbone_health_top_devices_by_alerts_response_200_system_plane import (
            PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane,
        )

        d = src_dict.copy()
        _control_plane = d.pop("controlPlane", UNSET)
        control_plane: Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane]
        if isinstance(_control_plane, Unset):
            control_plane = UNSET
        else:
            control_plane = PostV1BackboneHealthTopDevicesByAlertsResponse200ControlPlane.from_dict(_control_plane)

        _data_plane = d.pop("dataPlane", UNSET)
        data_plane: Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane]
        if isinstance(_data_plane, Unset):
            data_plane = UNSET
        else:
            data_plane = PostV1BackboneHealthTopDevicesByAlertsResponse200DataPlane.from_dict(_data_plane)

        _system_plane = d.pop("systemPlane", UNSET)
        system_plane: Union[Unset, PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane]
        if isinstance(_system_plane, Unset):
            system_plane = UNSET
        else:
            system_plane = PostV1BackboneHealthTopDevicesByAlertsResponse200SystemPlane.from_dict(_system_plane)

        post_v1_backbone_health_top_devices_by_alerts_response_200 = cls(
            control_plane=control_plane,
            data_plane=data_plane,
            system_plane=system_plane,
        )

        post_v1_backbone_health_top_devices_by_alerts_response_200.additional_properties = d
        return post_v1_backbone_health_top_devices_by_alerts_response_200

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
