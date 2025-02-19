from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_apps_custom_response_200_app_identifier import (
        PostV1GlobalAppsCustomResponse200AppIdentifier,
    )


T = TypeVar("T", bound="PostV1GlobalAppsCustomResponse200")


@_attrs_define
class PostV1GlobalAppsCustomResponse200:
    """
    Attributes:
        app_identifier (Union[Unset, PostV1GlobalAppsCustomResponse200AppIdentifier]):
    """

    app_identifier: Union[Unset, "PostV1GlobalAppsCustomResponse200AppIdentifier"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_identifier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_identifier, Unset):
            app_identifier = self.app_identifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_identifier is not UNSET:
            field_dict["appIdentifier"] = app_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_apps_custom_response_200_app_identifier import (
            PostV1GlobalAppsCustomResponse200AppIdentifier,
        )

        d = src_dict.copy()
        _app_identifier = d.pop("appIdentifier", UNSET)
        app_identifier: Union[Unset, PostV1GlobalAppsCustomResponse200AppIdentifier]
        if isinstance(_app_identifier, Unset):
            app_identifier = UNSET
        else:
            app_identifier = PostV1GlobalAppsCustomResponse200AppIdentifier.from_dict(_app_identifier)

        post_v1_global_apps_custom_response_200 = cls(
            app_identifier=app_identifier,
        )

        post_v1_global_apps_custom_response_200.additional_properties = d
        return post_v1_global_apps_custom_response_200

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
