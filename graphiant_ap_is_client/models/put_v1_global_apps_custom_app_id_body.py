from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_global_apps_custom_app_id_body_app_config import PutV1GlobalAppsCustomAppIdBodyAppConfig


T = TypeVar("T", bound="PutV1GlobalAppsCustomAppIdBody")


@_attrs_define
class PutV1GlobalAppsCustomAppIdBody:
    """
    Attributes:
        app_config (Union[Unset, PutV1GlobalAppsCustomAppIdBodyAppConfig]):
    """

    app_config: Union[Unset, "PutV1GlobalAppsCustomAppIdBodyAppConfig"] = UNSET
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
        from ..models.put_v1_global_apps_custom_app_id_body_app_config import PutV1GlobalAppsCustomAppIdBodyAppConfig

        d = src_dict.copy()
        _app_config = d.pop("appConfig", UNSET)
        app_config: Union[Unset, PutV1GlobalAppsCustomAppIdBodyAppConfig]
        if isinstance(_app_config, Unset):
            app_config = UNSET
        else:
            app_config = PutV1GlobalAppsCustomAppIdBodyAppConfig.from_dict(_app_config)

        put_v1_global_apps_custom_app_id_body = cls(
            app_config=app_config,
        )

        put_v1_global_apps_custom_app_id_body.additional_properties = d
        return put_v1_global_apps_custom_app_id_body

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
