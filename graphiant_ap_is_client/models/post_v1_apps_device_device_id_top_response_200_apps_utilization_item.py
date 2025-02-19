from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AppsDeviceDeviceIdTopResponse200AppsUtilizationItem")


@_attrs_define
class PostV1AppsDeviceDeviceIdTopResponse200AppsUtilizationItem:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        usage (Union[Unset, str]):  Example: TYPE_INT64.
    """

    app_id: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        app_name = d.pop("appName", UNSET)

        usage = d.pop("usage", UNSET)

        post_v1_apps_device_device_id_top_response_200_apps_utilization_item = cls(
            app_id=app_id,
            app_name=app_name,
            usage=usage,
        )

        post_v1_apps_device_device_id_top_response_200_apps_utilization_item.additional_properties = d
        return post_v1_apps_device_device_id_top_response_200_apps_utilization_item

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
