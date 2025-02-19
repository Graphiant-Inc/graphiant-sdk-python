from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2NotificationUpdateBodyNotificationBody")


@_attrs_define
class PostV2NotificationUpdateBodyNotificationBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        duration (Union[Unset, str]):  Example: TYPE_ENUM.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        frequency (Union[Unset, str]):  Example: TYPE_UINT64.
        message_body (Union[Unset, str]):  Example: TYPE_STRING.
        notification_name (Union[Unset, str]):  Example: TYPE_STRING.
        opsgenie_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        opsramp_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        recipient_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        teams_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    description: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    frequency: Union[Unset, str] = UNSET
    message_body: Union[Unset, str] = UNSET
    notification_name: Union[Unset, str] = UNSET
    opsgenie_list: Union[Unset, list[str]] = UNSET
    opsramp_list: Union[Unset, list[str]] = UNSET
    recipient_list: Union[Unset, list[str]] = UNSET
    teams_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        duration = self.duration

        enabled = self.enabled

        frequency = self.frequency

        message_body = self.message_body

        notification_name = self.notification_name

        opsgenie_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.opsgenie_list, Unset):
            opsgenie_list = self.opsgenie_list

        opsramp_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.opsramp_list, Unset):
            opsramp_list = self.opsramp_list

        recipient_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_list, Unset):
            recipient_list = self.recipient_list

        teams_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.teams_list, Unset):
            teams_list = self.teams_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if message_body is not UNSET:
            field_dict["messageBody"] = message_body
        if notification_name is not UNSET:
            field_dict["notificationName"] = notification_name
        if opsgenie_list is not UNSET:
            field_dict["opsgenieList"] = opsgenie_list
        if opsramp_list is not UNSET:
            field_dict["opsrampList"] = opsramp_list
        if recipient_list is not UNSET:
            field_dict["recipientList"] = recipient_list
        if teams_list is not UNSET:
            field_dict["teamsList"] = teams_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        enabled = d.pop("enabled", UNSET)

        frequency = d.pop("frequency", UNSET)

        message_body = d.pop("messageBody", UNSET)

        notification_name = d.pop("notificationName", UNSET)

        opsgenie_list = cast(list[str], d.pop("opsgenieList", UNSET))

        opsramp_list = cast(list[str], d.pop("opsrampList", UNSET))

        recipient_list = cast(list[str], d.pop("recipientList", UNSET))

        teams_list = cast(list[str], d.pop("teamsList", UNSET))

        post_v2_notification_update_body_notification_body = cls(
            description=description,
            duration=duration,
            enabled=enabled,
            frequency=frequency,
            message_body=message_body,
            notification_name=notification_name,
            opsgenie_list=opsgenie_list,
            opsramp_list=opsramp_list,
            recipient_list=recipient_list,
            teams_list=teams_list,
        )

        post_v2_notification_update_body_notification_body.additional_properties = d
        return post_v2_notification_update_body_notification_body

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
