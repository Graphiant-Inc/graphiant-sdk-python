from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_childalertlist_response_200_alert_list_item import (
        PostV2ChildalertlistResponse200AlertListItem,
    )


T = TypeVar("T", bound="PostV2ChildalertlistResponse200")


@_attrs_define
class PostV2ChildalertlistResponse200:
    """
    Attributes:
        alert_list (Union[Unset, list['PostV2ChildalertlistResponse200AlertListItem']]):
    """

    alert_list: Union[Unset, list["PostV2ChildalertlistResponse200AlertListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.alert_list, Unset):
            alert_list = []
            for alert_list_item_data in self.alert_list:
                alert_list_item = alert_list_item_data.to_dict()
                alert_list.append(alert_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_list is not UNSET:
            field_dict["alertList"] = alert_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_childalertlist_response_200_alert_list_item import (
            PostV2ChildalertlistResponse200AlertListItem,
        )

        d = src_dict.copy()
        alert_list = []
        _alert_list = d.pop("alertList", UNSET)
        for alert_list_item_data in _alert_list or []:
            alert_list_item = PostV2ChildalertlistResponse200AlertListItem.from_dict(alert_list_item_data)

            alert_list.append(alert_list_item)

        post_v2_childalertlist_response_200 = cls(
            alert_list=alert_list,
        )

        post_v2_childalertlist_response_200.additional_properties = d
        return post_v2_childalertlist_response_200

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
