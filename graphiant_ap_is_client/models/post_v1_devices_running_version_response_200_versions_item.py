from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_running_version_response_200_versions_item_version import (
        PostV1DevicesRunningVersionResponse200VersionsItemVersion,
    )


T = TypeVar("T", bound="PostV1DevicesRunningVersionResponse200VersionsItem")


@_attrs_define
class PostV1DevicesRunningVersionResponse200VersionsItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        version (Union[Unset, PostV1DevicesRunningVersionResponse200VersionsItemVersion]):
    """

    device_id: Union[Unset, str] = UNSET
    version: Union[Unset, "PostV1DevicesRunningVersionResponse200VersionsItemVersion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_running_version_response_200_versions_item_version import (
            PostV1DevicesRunningVersionResponse200VersionsItemVersion,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, PostV1DevicesRunningVersionResponse200VersionsItemVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = PostV1DevicesRunningVersionResponse200VersionsItemVersion.from_dict(_version)

        post_v1_devices_running_version_response_200_versions_item = cls(
            device_id=device_id,
            version=version,
        )

        post_v1_devices_running_version_response_200_versions_item.additional_properties = d
        return post_v1_devices_running_version_response_200_versions_item

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
