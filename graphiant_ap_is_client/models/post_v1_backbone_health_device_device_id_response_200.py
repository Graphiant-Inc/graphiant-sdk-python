from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane import (
        PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane import (
        PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_issues_item import (
        PostV1BackboneHealthDeviceDeviceIdResponse200IssuesItem,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_sw_version_v2 import (
        PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_system_plane import (
        PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_up_since_ts import (
        PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200:
    """
    Attributes:
        control_plane (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane]):
        data_plane (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane]):
        issues (Union[Unset, list['PostV1BackboneHealthDeviceDeviceIdResponse200IssuesItem']]):
        qoe_matrix (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix]):
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        sw_version (Union[Unset, str]):  Example: TYPE_STRING.
        sw_version_v2 (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2]):
        system_plane (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane]):
        up_since_ts (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs]):
    """

    control_plane: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane"] = UNSET
    data_plane: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane"] = UNSET
    issues: Union[Unset, list["PostV1BackboneHealthDeviceDeviceIdResponse200IssuesItem"]] = UNSET
    qoe_matrix: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix"] = UNSET
    role: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    sw_version: Union[Unset, str] = UNSET
    sw_version_v2: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2"] = UNSET
    system_plane: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane"] = UNSET
    up_since_ts: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.control_plane, Unset):
            control_plane = self.control_plane.to_dict()

        data_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_plane, Unset):
            data_plane = self.data_plane.to_dict()

        issues: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        qoe_matrix: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qoe_matrix, Unset):
            qoe_matrix = self.qoe_matrix.to_dict()

        role = self.role

        status = self.status

        sw_version = self.sw_version

        sw_version_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sw_version_v2, Unset):
            sw_version_v2 = self.sw_version_v2.to_dict()

        system_plane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_plane, Unset):
            system_plane = self.system_plane.to_dict()

        up_since_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.up_since_ts, Unset):
            up_since_ts = self.up_since_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_plane is not UNSET:
            field_dict["controlPlane"] = control_plane
        if data_plane is not UNSET:
            field_dict["dataPlane"] = data_plane
        if issues is not UNSET:
            field_dict["issues"] = issues
        if qoe_matrix is not UNSET:
            field_dict["qoeMatrix"] = qoe_matrix
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if sw_version is not UNSET:
            field_dict["swVersion"] = sw_version
        if sw_version_v2 is not UNSET:
            field_dict["swVersionV2"] = sw_version_v2
        if system_plane is not UNSET:
            field_dict["systemPlane"] = system_plane
        if up_since_ts is not UNSET:
            field_dict["upSinceTs"] = up_since_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_control_plane import (
            PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane import (
            PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_issues_item import (
            PostV1BackboneHealthDeviceDeviceIdResponse200IssuesItem,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_sw_version_v2 import (
            PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_system_plane import (
            PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_up_since_ts import (
            PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs,
        )

        d = src_dict.copy()
        _control_plane = d.pop("controlPlane", UNSET)
        control_plane: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane]
        if isinstance(_control_plane, Unset):
            control_plane = UNSET
        else:
            control_plane = PostV1BackboneHealthDeviceDeviceIdResponse200ControlPlane.from_dict(_control_plane)

        _data_plane = d.pop("dataPlane", UNSET)
        data_plane: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane]
        if isinstance(_data_plane, Unset):
            data_plane = UNSET
        else:
            data_plane = PostV1BackboneHealthDeviceDeviceIdResponse200DataPlane.from_dict(_data_plane)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = PostV1BackboneHealthDeviceDeviceIdResponse200IssuesItem.from_dict(issues_item_data)

            issues.append(issues_item)

        _qoe_matrix = d.pop("qoeMatrix", UNSET)
        qoe_matrix: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix]
        if isinstance(_qoe_matrix, Unset):
            qoe_matrix = UNSET
        else:
            qoe_matrix = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrix.from_dict(_qoe_matrix)

        role = d.pop("role", UNSET)

        status = d.pop("status", UNSET)

        sw_version = d.pop("swVersion", UNSET)

        _sw_version_v2 = d.pop("swVersionV2", UNSET)
        sw_version_v2: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2]
        if isinstance(_sw_version_v2, Unset):
            sw_version_v2 = UNSET
        else:
            sw_version_v2 = PostV1BackboneHealthDeviceDeviceIdResponse200SwVersionV2.from_dict(_sw_version_v2)

        _system_plane = d.pop("systemPlane", UNSET)
        system_plane: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane]
        if isinstance(_system_plane, Unset):
            system_plane = UNSET
        else:
            system_plane = PostV1BackboneHealthDeviceDeviceIdResponse200SystemPlane.from_dict(_system_plane)

        _up_since_ts = d.pop("upSinceTs", UNSET)
        up_since_ts: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs]
        if isinstance(_up_since_ts, Unset):
            up_since_ts = UNSET
        else:
            up_since_ts = PostV1BackboneHealthDeviceDeviceIdResponse200UpSinceTs.from_dict(_up_since_ts)

        post_v1_backbone_health_device_device_id_response_200 = cls(
            control_plane=control_plane,
            data_plane=data_plane,
            issues=issues,
            qoe_matrix=qoe_matrix,
            role=role,
            status=status,
            sw_version=sw_version,
            sw_version_v2=sw_version_v2,
            system_plane=system_plane,
            up_since_ts=up_since_ts,
        )

        post_v1_backbone_health_device_device_id_response_200.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200

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
