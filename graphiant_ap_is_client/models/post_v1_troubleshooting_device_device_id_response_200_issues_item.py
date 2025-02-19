from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_device_device_id_response_200_issues_item_end_time import (
        PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_issues_item_start_time import (
        PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime,
    )


T = TypeVar("T", bound="PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItem")


@_attrs_define
class PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItem:
    """
    Attributes:
        alert_id (Union[Unset, str]):  Example: TYPE_STRING.
        allow_listed (Union[Unset, str]):  Example: TYPE_BOOL.
        component (Union[Unset, str]):  Example: TYPE_STRING.
        end_time (Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime]):
        entity (Union[Unset, str]):  Example: TYPE_STRING.
        issue (Union[Unset, str]):  Example: TYPE_STRING.
        mute_listed (Union[Unset, str]):  Example: TYPE_BOOL.
        notification_created (Union[Unset, str]):  Example: TYPE_BOOL.
        plane (Union[Unset, str]):  Example: TYPE_STRING.
        reason (Union[Unset, str]):  Example: TYPE_STRING.
        severity (Union[Unset, str]):  Example: TYPE_ENUM.
        start_time (Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    alert_id: Union[Unset, str] = UNSET
    allow_listed: Union[Unset, str] = UNSET
    component: Union[Unset, str] = UNSET
    end_time: Union[Unset, "PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime"] = UNSET
    entity: Union[Unset, str] = UNSET
    issue: Union[Unset, str] = UNSET
    mute_listed: Union[Unset, str] = UNSET
    notification_created: Union[Unset, str] = UNSET
    plane: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    start_time: Union[Unset, "PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_id = self.alert_id

        allow_listed = self.allow_listed

        component = self.component

        end_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        entity = self.entity

        issue = self.issue

        mute_listed = self.mute_listed

        notification_created = self.notification_created

        plane = self.plane

        reason = self.reason

        severity = self.severity

        start_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if allow_listed is not UNSET:
            field_dict["allowListed"] = allow_listed
        if component is not UNSET:
            field_dict["component"] = component
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if entity is not UNSET:
            field_dict["entity"] = entity
        if issue is not UNSET:
            field_dict["issue"] = issue
        if mute_listed is not UNSET:
            field_dict["muteListed"] = mute_listed
        if notification_created is not UNSET:
            field_dict["notificationCreated"] = notification_created
        if plane is not UNSET:
            field_dict["plane"] = plane
        if reason is not UNSET:
            field_dict["reason"] = reason
        if severity is not UNSET:
            field_dict["severity"] = severity
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_device_device_id_response_200_issues_item_end_time import (
            PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_issues_item_start_time import (
            PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime,
        )

        d = src_dict.copy()
        alert_id = d.pop("alertId", UNSET)

        allow_listed = d.pop("allowListed", UNSET)

        component = d.pop("component", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemEndTime.from_dict(_end_time)

        entity = d.pop("entity", UNSET)

        issue = d.pop("issue", UNSET)

        mute_listed = d.pop("muteListed", UNSET)

        notification_created = d.pop("notificationCreated", UNSET)

        plane = d.pop("plane", UNSET)

        reason = d.pop("reason", UNSET)

        severity = d.pop("severity", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = PostV1TroubleshootingDeviceDeviceIdResponse200IssuesItemStartTime.from_dict(_start_time)

        status = d.pop("status", UNSET)

        post_v1_troubleshooting_device_device_id_response_200_issues_item = cls(
            alert_id=alert_id,
            allow_listed=allow_listed,
            component=component,
            end_time=end_time,
            entity=entity,
            issue=issue,
            mute_listed=mute_listed,
            notification_created=notification_created,
            plane=plane,
            reason=reason,
            severity=severity,
            start_time=start_time,
            status=status,
        )

        post_v1_troubleshooting_device_device_id_response_200_issues_item.additional_properties = d
        return post_v1_troubleshooting_device_device_id_response_200_issues_item

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
