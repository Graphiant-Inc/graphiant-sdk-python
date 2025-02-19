from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_notificationlist_response_200_notification_list_item_notification_body import (
        PostV2NotificationlistResponse200NotificationListItemNotificationBody,
    )


T = TypeVar("T", bound="PostV2NotificationlistResponse200NotificationListItem")


@_attrs_define
class PostV2NotificationlistResponse200NotificationListItem:
    """
    Attributes:
        alert_type (Union[Unset, str]):  Example: TYPE_STRING.
        mute_count (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notification_body (Union[Unset, PostV2NotificationlistResponse200NotificationListItemNotificationBody]):
        notification_id (Union[Unset, str]):  Example: TYPE_STRING.
        rule_id (Union[Unset, str]):  Example: TYPE_STRING.
        times_triggered (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    alert_type: Union[Unset, str] = UNSET
    mute_count: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notification_body: Union[Unset, "PostV2NotificationlistResponse200NotificationListItemNotificationBody"] = UNSET
    notification_id: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    times_triggered: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_type = self.alert_type

        mute_count = self.mute_count

        name = self.name

        notification_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_body, Unset):
            notification_body = self.notification_body.to_dict()

        notification_id = self.notification_id

        rule_id = self.rule_id

        times_triggered = self.times_triggered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_type is not UNSET:
            field_dict["alertType"] = alert_type
        if mute_count is not UNSET:
            field_dict["muteCount"] = mute_count
        if name is not UNSET:
            field_dict["name"] = name
        if notification_body is not UNSET:
            field_dict["notificationBody"] = notification_body
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if times_triggered is not UNSET:
            field_dict["timesTriggered"] = times_triggered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_notificationlist_response_200_notification_list_item_notification_body import (
            PostV2NotificationlistResponse200NotificationListItemNotificationBody,
        )

        d = src_dict.copy()
        alert_type = d.pop("alertType", UNSET)

        mute_count = d.pop("muteCount", UNSET)

        name = d.pop("name", UNSET)

        _notification_body = d.pop("notificationBody", UNSET)
        notification_body: Union[Unset, PostV2NotificationlistResponse200NotificationListItemNotificationBody]
        if isinstance(_notification_body, Unset):
            notification_body = UNSET
        else:
            notification_body = PostV2NotificationlistResponse200NotificationListItemNotificationBody.from_dict(
                _notification_body
            )

        notification_id = d.pop("notificationId", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        times_triggered = d.pop("timesTriggered", UNSET)

        post_v2_notificationlist_response_200_notification_list_item = cls(
            alert_type=alert_type,
            mute_count=mute_count,
            name=name,
            notification_body=notification_body,
            notification_id=notification_id,
            rule_id=rule_id,
            times_triggered=times_triggered,
        )

        post_v2_notificationlist_response_200_notification_list_item.additional_properties = d
        return post_v2_notificationlist_response_200_notification_list_item

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
