from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash_up_since_ts import (
        PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs,
    )


T = TypeVar("T", bound="PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash")


@_attrs_define
class PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrash:
    """
    Attributes:
        crash_details (Union[Unset, str]):  Example: TYPE_STRING.
        reason (Union[Unset, str]):  Example: TYPE_STRING.
        up_since_ts (Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs]):
    """

    crash_details: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    up_since_ts: Union[Unset, "PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crash_details = self.crash_details

        reason = self.reason

        up_since_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.up_since_ts, Unset):
            up_since_ts = self.up_since_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crash_details is not UNSET:
            field_dict["crashDetails"] = crash_details
        if reason is not UNSET:
            field_dict["reason"] = reason
        if up_since_ts is not UNSET:
            field_dict["upSinceTs"] = up_since_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash_up_since_ts import (
            PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs,
        )

        d = src_dict.copy()
        crash_details = d.pop("crashDetails", UNSET)

        reason = d.pop("reason", UNSET)

        _up_since_ts = d.pop("upSinceTs", UNSET)
        up_since_ts: Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs]
        if isinstance(_up_since_ts, Unset):
            up_since_ts = UNSET
        else:
            up_since_ts = PostV1TroubleshootingDeviceDeviceIdResponse200SystemPlaneLastCrashUpSinceTs.from_dict(
                _up_since_ts
            )

        post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash = cls(
            crash_details=crash_details,
            reason=reason,
            up_since_ts=up_since_ts,
        )

        post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash.additional_properties = d
        return post_v1_troubleshooting_device_device_id_response_200_system_plane_last_crash

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
