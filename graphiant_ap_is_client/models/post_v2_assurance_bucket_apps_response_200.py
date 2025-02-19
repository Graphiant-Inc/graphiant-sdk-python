from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_bucket_apps_response_200_apps_item import (
        PostV2AssuranceBucketAppsResponse200AppsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceBucketAppsResponse200")


@_attrs_define
class PostV2AssuranceBucketAppsResponse200:
    """
    Attributes:
        apps (Union[Unset, list['PostV2AssuranceBucketAppsResponse200AppsItem']]):
    """

    apps: Union[Unset, list["PostV2AssuranceBucketAppsResponse200AppsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_bucket_apps_response_200_apps_item import (
            PostV2AssuranceBucketAppsResponse200AppsItem,
        )

        d = src_dict.copy()
        apps = []
        _apps = d.pop("apps", UNSET)
        for apps_item_data in _apps or []:
            apps_item = PostV2AssuranceBucketAppsResponse200AppsItem.from_dict(apps_item_data)

            apps.append(apps_item)

        post_v2_assurance_bucket_apps_response_200 = cls(
            apps=apps,
        )

        post_v2_assurance_bucket_apps_response_200.additional_properties = d
        return post_v2_assurance_bucket_apps_response_200

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
