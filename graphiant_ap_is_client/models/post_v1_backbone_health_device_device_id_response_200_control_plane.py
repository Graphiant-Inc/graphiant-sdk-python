from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane_control_transitions import (
        PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane_management_transitions import (
        PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane:
    """
    Attributes:
        control_transitions (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions]):
        management_transitions (Union[Unset,
            PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    control_transitions: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions"] = (
        UNSET
    )
    management_transitions: Union[
        Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions"
    ] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_transitions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.control_transitions, Unset):
            control_transitions = self.control_transitions.to_dict()

        management_transitions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.management_transitions, Unset):
            management_transitions = self.management_transitions.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_transitions is not UNSET:
            field_dict["controlTransitions"] = control_transitions
        if management_transitions is not UNSET:
            field_dict["managementTransitions"] = management_transitions
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane_control_transitions import (
            PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane_management_transitions import (
            PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions,
        )

        d = src_dict.copy()
        _control_transitions = d.pop("controlTransitions", UNSET)
        control_transitions: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions]
        if isinstance(_control_transitions, Unset):
            control_transitions = UNSET
        else:
            control_transitions = PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneControlTransitions.from_dict(
                _control_transitions
            )

        _management_transitions = d.pop("managementTransitions", UNSET)
        management_transitions: Union[
            Unset, PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions
        ]
        if isinstance(_management_transitions, Unset):
            management_transitions = UNSET
        else:
            management_transitions = (
                PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlaneManagementTransitions.from_dict(
                    _management_transitions
                )
            )

        status = d.pop("status", UNSET)

        post_v1_backbone_health_device_device_id_response_200_control_plane = cls(
            control_transitions=control_transitions,
            management_transitions=management_transitions,
            status=status,
        )

        post_v1_backbone_health_device_device_id_response_200_control_plane.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_control_plane

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
