from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_applicationdetailsbyid_body_time_window import (
        PostV2AssuranceApplicationdetailsbyidBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2AssuranceApplicationdetailsbyidBody")


@_attrs_define
class PostV2AssuranceApplicationdetailsbyidBody:
    """
    Attributes:
        app_id_key (Union[Unset, str]):  Example: TYPE_STRING.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
        time_window (Union[Unset, PostV2AssuranceApplicationdetailsbyidBodyTimeWindow]):
    """

    app_id_key: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    bucket_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2AssuranceApplicationdetailsbyidBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id_key = self.app_id_key

        app_name = self.app_name

        bucket_id = self.bucket_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id_key is not UNSET:
            field_dict["appIdKey"] = app_id_key
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if bucket_id is not UNSET:
            field_dict["bucketId"] = bucket_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_applicationdetailsbyid_body_time_window import (
            PostV2AssuranceApplicationdetailsbyidBodyTimeWindow,
        )

        d = src_dict.copy()
        app_id_key = d.pop("appIdKey", UNSET)

        app_name = d.pop("appName", UNSET)

        bucket_id = d.pop("bucketId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceApplicationdetailsbyidBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceApplicationdetailsbyidBodyTimeWindow.from_dict(_time_window)

        post_v2_assurance_applicationdetailsbyid_body = cls(
            app_id_key=app_id_key,
            app_name=app_name,
            bucket_id=bucket_id,
            time_window=time_window,
        )

        post_v2_assurance_applicationdetailsbyid_body.additional_properties = d
        return post_v2_assurance_applicationdetailsbyid_body

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
