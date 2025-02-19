from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_notificationlist_response_200_notification_list_item import (
        PostV2NotificationlistResponse200NotificationListItem,
    )


T = TypeVar("T", bound="PostV2NotificationlistResponse200")


@_attrs_define
class PostV2NotificationlistResponse200:
    """
    Attributes:
        notification_list (Union[Unset, list['PostV2NotificationlistResponse200NotificationListItem']]):
    """

    notification_list: Union[Unset, list["PostV2NotificationlistResponse200NotificationListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_list, Unset):
            notification_list = []
            for notification_list_item_data in self.notification_list:
                notification_list_item = notification_list_item_data.to_dict()
                notification_list.append(notification_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_list is not UNSET:
            field_dict["notificationList"] = notification_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_notificationlist_response_200_notification_list_item import (
            PostV2NotificationlistResponse200NotificationListItem,
        )

        d = src_dict.copy()
        notification_list = []
        _notification_list = d.pop("notificationList", UNSET)
        for notification_list_item_data in _notification_list or []:
            notification_list_item = PostV2NotificationlistResponse200NotificationListItem.from_dict(
                notification_list_item_data
            )

            notification_list.append(notification_list_item)

        post_v2_notificationlist_response_200 = cls(
            notification_list=notification_list,
        )

        post_v2_notificationlist_response_200.additional_properties = d
        return post_v2_notificationlist_response_200

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
