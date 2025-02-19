from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_apps_custom_body_app_config import PostV1GlobalAppsCustomBodyAppConfig


T = TypeVar("T", bound="PostV1GlobalAppsCustomBody")


@_attrs_define
class PostV1GlobalAppsCustomBody:
    """
    Attributes:
        app_config (Union[Unset, PostV1GlobalAppsCustomBodyAppConfig]):
    """

    app_config: Union[Unset, "PostV1GlobalAppsCustomBodyAppConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_config, Unset):
            app_config = self.app_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config is not UNSET:
            field_dict["appConfig"] = app_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_apps_custom_body_app_config import PostV1GlobalAppsCustomBodyAppConfig

        d = src_dict.copy()
        _app_config = d.pop("appConfig", UNSET)
        app_config: Union[Unset, PostV1GlobalAppsCustomBodyAppConfig]
        if isinstance(_app_config, Unset):
            app_config = UNSET
        else:
            app_config = PostV1GlobalAppsCustomBodyAppConfig.from_dict(_app_config)

        post_v1_global_apps_custom_body = cls(
            app_config=app_config,
        )

        post_v1_global_apps_custom_body.additional_properties = d
        return post_v1_global_apps_custom_body

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
