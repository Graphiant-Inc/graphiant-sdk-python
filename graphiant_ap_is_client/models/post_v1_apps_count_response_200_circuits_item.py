from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_count_response_200_circuits_item_apps_count_bucket_item import (
        PostV1AppsCountResponse200CircuitsItemAppsCountBucketItem,
    )
    from ..models.post_v1_apps_count_response_200_circuits_item_queues_item import (
        PostV1AppsCountResponse200CircuitsItemQueuesItem,
    )


T = TypeVar("T", bound="PostV1AppsCountResponse200CircuitsItem")


@_attrs_define
class PostV1AppsCountResponse200CircuitsItem:
    """
    Attributes:
        apps_count (Union[Unset, str]):  Example: TYPE_UINT32.
        apps_count_bucket (Union[Unset, list['PostV1AppsCountResponse200CircuitsItemAppsCountBucketItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        queues (Union[Unset, list['PostV1AppsCountResponse200CircuitsItemQueuesItem']]):
    """

    apps_count: Union[Unset, str] = UNSET
    apps_count_bucket: Union[Unset, list["PostV1AppsCountResponse200CircuitsItemAppsCountBucketItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    queues: Union[Unset, list["PostV1AppsCountResponse200CircuitsItemQueuesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps_count = self.apps_count

        apps_count_bucket: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps_count_bucket, Unset):
            apps_count_bucket = []
            for apps_count_bucket_item_data in self.apps_count_bucket:
                apps_count_bucket_item = apps_count_bucket_item_data.to_dict()
                apps_count_bucket.append(apps_count_bucket_item)

        name = self.name

        queues: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.queues, Unset):
            queues = []
            for queues_item_data in self.queues:
                queues_item = queues_item_data.to_dict()
                queues.append(queues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps_count is not UNSET:
            field_dict["appsCount"] = apps_count
        if apps_count_bucket is not UNSET:
            field_dict["appsCountBucket"] = apps_count_bucket
        if name is not UNSET:
            field_dict["name"] = name
        if queues is not UNSET:
            field_dict["queues"] = queues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_count_response_200_circuits_item_apps_count_bucket_item import (
            PostV1AppsCountResponse200CircuitsItemAppsCountBucketItem,
        )
        from ..models.post_v1_apps_count_response_200_circuits_item_queues_item import (
            PostV1AppsCountResponse200CircuitsItemQueuesItem,
        )

        d = src_dict.copy()
        apps_count = d.pop("appsCount", UNSET)

        apps_count_bucket = []
        _apps_count_bucket = d.pop("appsCountBucket", UNSET)
        for apps_count_bucket_item_data in _apps_count_bucket or []:
            apps_count_bucket_item = PostV1AppsCountResponse200CircuitsItemAppsCountBucketItem.from_dict(
                apps_count_bucket_item_data
            )

            apps_count_bucket.append(apps_count_bucket_item)

        name = d.pop("name", UNSET)

        queues = []
        _queues = d.pop("queues", UNSET)
        for queues_item_data in _queues or []:
            queues_item = PostV1AppsCountResponse200CircuitsItemQueuesItem.from_dict(queues_item_data)

            queues.append(queues_item)

        post_v1_apps_count_response_200_circuits_item = cls(
            apps_count=apps_count,
            apps_count_bucket=apps_count_bucket,
            name=name,
            queues=queues,
        )

        post_v1_apps_count_response_200_circuits_item.additional_properties = d
        return post_v1_apps_count_response_200_circuits_item

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
