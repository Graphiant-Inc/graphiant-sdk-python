from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_notification_update_body_notification_body import PostV2NotificationUpdateBodyNotificationBody


T = TypeVar("T", bound="PostV2NotificationUpdateBody")


@_attrs_define
class PostV2NotificationUpdateBody:
    """
    Attributes:
        notification_body (Union[Unset, PostV2NotificationUpdateBodyNotificationBody]):
        notification_id_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    notification_body: Union[Unset, "PostV2NotificationUpdateBodyNotificationBody"] = UNSET
    notification_id_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_body, Unset):
            notification_body = self.notification_body.to_dict()

        notification_id_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.notification_id_list, Unset):
            notification_id_list = self.notification_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_body is not UNSET:
            field_dict["notificationBody"] = notification_body
        if notification_id_list is not UNSET:
            field_dict["notificationIdList"] = notification_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_notification_update_body_notification_body import (
            PostV2NotificationUpdateBodyNotificationBody,
        )

        d = src_dict.copy()
        _notification_body = d.pop("notificationBody", UNSET)
        notification_body: Union[Unset, PostV2NotificationUpdateBodyNotificationBody]
        if isinstance(_notification_body, Unset):
            notification_body = UNSET
        else:
            notification_body = PostV2NotificationUpdateBodyNotificationBody.from_dict(_notification_body)

        notification_id_list = cast(list[str], d.pop("notificationIdList", UNSET))

        post_v2_notification_update_body = cls(
            notification_body=notification_body,
            notification_id_list=notification_id_list,
        )

        post_v2_notification_update_body.additional_properties = d
        return post_v2_notification_update_body

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
