from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftSiteDevicesItem")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftSiteDevicesItem:
    """
    Attributes:
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        post_v1_devices_device_id_draft_body_draft_site_devices_item = cls(
            hostname=hostname,
            id=id,
        )

        post_v1_devices_device_id_draft_body_draft_site_devices_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_site_devices_item

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
