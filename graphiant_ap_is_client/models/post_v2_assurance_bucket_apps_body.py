from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_bucket_apps_body_time_window import PostV2AssuranceBucketAppsBodyTimeWindow


T = TypeVar("T", bound="PostV2AssuranceBucketAppsBody")


@_attrs_define
class PostV2AssuranceBucketAppsBody:
    """
    Attributes:
        bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
        time_window (Union[Unset, PostV2AssuranceBucketAppsBodyTimeWindow]):
        unclassified_only (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    bucket_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2AssuranceBucketAppsBodyTimeWindow"] = UNSET
    unclassified_only: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        unclassified_only = self.unclassified_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_id is not UNSET:
            field_dict["bucketId"] = bucket_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window
        if unclassified_only is not UNSET:
            field_dict["unclassifiedOnly"] = unclassified_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_bucket_apps_body_time_window import PostV2AssuranceBucketAppsBodyTimeWindow

        d = src_dict.copy()
        bucket_id = d.pop("bucketId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceBucketAppsBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceBucketAppsBodyTimeWindow.from_dict(_time_window)

        unclassified_only = d.pop("unclassifiedOnly", UNSET)

        post_v2_assurance_bucket_apps_body = cls(
            bucket_id=bucket_id,
            time_window=time_window,
            unclassified_only=unclassified_only,
        )

        post_v2_assurance_bucket_apps_body.additional_properties = d
        return post_v2_assurance_bucket_apps_body

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
