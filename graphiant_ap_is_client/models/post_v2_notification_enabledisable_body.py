from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2NotificationEnabledisableBody")


@_attrs_define
class PostV2NotificationEnabledisableBody:
    """
    Attributes:
        enable (Union[Unset, str]):  Example: TYPE_BOOL.
        notification_id_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    enable: Union[Unset, str] = UNSET
    notification_id_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        notification_id_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.notification_id_list, Unset):
            notification_id_list = self.notification_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if notification_id_list is not UNSET:
            field_dict["notificationIdList"] = notification_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        notification_id_list = cast(list[str], d.pop("notificationIdList", UNSET))

        post_v2_notification_enabledisable_body = cls(
            enable=enable,
            notification_id_list=notification_id_list,
        )

        post_v2_notification_enabledisable_body.additional_properties = d
        return post_v2_notification_enabledisable_body

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
