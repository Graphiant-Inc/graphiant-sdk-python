from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_app_lists_app_list_id_response_200_app_list_config import (
        GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig,
    )


T = TypeVar("T", bound="GetV1GlobalAppsAppListsAppListIdResponse200")


@_attrs_define
class GetV1GlobalAppsAppListsAppListIdResponse200:
    """
    Attributes:
        app_list_config (Union[Unset, GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig]):
    """

    app_list_config: Union[Unset, "GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_list_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_list_config, Unset):
            app_list_config = self.app_list_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_list_config is not UNSET:
            field_dict["appListConfig"] = app_list_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_app_lists_app_list_id_response_200_app_list_config import (
            GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig,
        )

        d = src_dict.copy()
        _app_list_config = d.pop("appListConfig", UNSET)
        app_list_config: Union[Unset, GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig]
        if isinstance(_app_list_config, Unset):
            app_list_config = UNSET
        else:
            app_list_config = GetV1GlobalAppsAppListsAppListIdResponse200AppListConfig.from_dict(_app_list_config)

        get_v1_global_apps_app_lists_app_list_id_response_200 = cls(
            app_list_config=app_list_config,
        )

        get_v1_global_apps_app_lists_app_list_id_response_200.additional_properties = d
        return get_v1_global_apps_app_lists_app_list_id_response_200

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
