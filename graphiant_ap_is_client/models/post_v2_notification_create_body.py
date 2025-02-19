from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_notification_create_body_notification_body import PostV2NotificationCreateBodyNotificationBody


T = TypeVar("T", bound="PostV2NotificationCreateBody")


@_attrs_define
class PostV2NotificationCreateBody:
    """
    Attributes:
        notification_body (Union[Unset, PostV2NotificationCreateBodyNotificationBody]):
        rule_id_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    notification_body: Union[Unset, "PostV2NotificationCreateBodyNotificationBody"] = UNSET
    rule_id_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_body, Unset):
            notification_body = self.notification_body.to_dict()

        rule_id_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rule_id_list, Unset):
            rule_id_list = self.rule_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_body is not UNSET:
            field_dict["notificationBody"] = notification_body
        if rule_id_list is not UNSET:
            field_dict["ruleIdList"] = rule_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_notification_create_body_notification_body import (
            PostV2NotificationCreateBodyNotificationBody,
        )

        d = src_dict.copy()
        _notification_body = d.pop("notificationBody", UNSET)
        notification_body: Union[Unset, PostV2NotificationCreateBodyNotificationBody]
        if isinstance(_notification_body, Unset):
            notification_body = UNSET
        else:
            notification_body = PostV2NotificationCreateBodyNotificationBody.from_dict(_notification_body)

        rule_id_list = cast(list[str], d.pop("ruleIdList", UNSET))

        post_v2_notification_create_body = cls(
            notification_body=notification_body,
            rule_id_list=rule_id_list,
        )

        post_v2_notification_create_body.additional_properties = d
        return post_v2_notification_create_body

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
