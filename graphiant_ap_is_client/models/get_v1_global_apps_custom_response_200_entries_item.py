from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_custom_response_200_entries_item_app import (
        GetV1GlobalAppsCustomResponse200EntriesItemApp,
    )
    from ..models.get_v1_global_apps_custom_response_200_entries_item_app_config import (
        GetV1GlobalAppsCustomResponse200EntriesItemAppConfig,
    )


T = TypeVar("T", bound="GetV1GlobalAppsCustomResponse200EntriesItem")


@_attrs_define
class GetV1GlobalAppsCustomResponse200EntriesItem:
    """
    Attributes:
        app (Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemApp]):
        app_config (Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemAppConfig]):
        app_list_reference_count (Union[Unset, str]):  Example: TYPE_INT32.
        policy_reference_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    app: Union[Unset, "GetV1GlobalAppsCustomResponse200EntriesItemApp"] = UNSET
    app_config: Union[Unset, "GetV1GlobalAppsCustomResponse200EntriesItemAppConfig"] = UNSET
    app_list_reference_count: Union[Unset, str] = UNSET
    policy_reference_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        app_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_config, Unset):
            app_config = self.app_config.to_dict()

        app_list_reference_count = self.app_list_reference_count

        policy_reference_count = self.policy_reference_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if app_config is not UNSET:
            field_dict["appConfig"] = app_config
        if app_list_reference_count is not UNSET:
            field_dict["appListReferenceCount"] = app_list_reference_count
        if policy_reference_count is not UNSET:
            field_dict["policyReferenceCount"] = policy_reference_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_custom_response_200_entries_item_app import (
            GetV1GlobalAppsCustomResponse200EntriesItemApp,
        )
        from ..models.get_v1_global_apps_custom_response_200_entries_item_app_config import (
            GetV1GlobalAppsCustomResponse200EntriesItemAppConfig,
        )

        d = src_dict.copy()
        _app = d.pop("app", UNSET)
        app: Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemApp]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = GetV1GlobalAppsCustomResponse200EntriesItemApp.from_dict(_app)

        _app_config = d.pop("appConfig", UNSET)
        app_config: Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemAppConfig]
        if isinstance(_app_config, Unset):
            app_config = UNSET
        else:
            app_config = GetV1GlobalAppsCustomResponse200EntriesItemAppConfig.from_dict(_app_config)

        app_list_reference_count = d.pop("appListReferenceCount", UNSET)

        policy_reference_count = d.pop("policyReferenceCount", UNSET)

        get_v1_global_apps_custom_response_200_entries_item = cls(
            app=app,
            app_config=app_config,
            app_list_reference_count=app_list_reference_count,
            policy_reference_count=policy_reference_count,
        )

        get_v1_global_apps_custom_response_200_entries_item.additional_properties = d
        return get_v1_global_apps_custom_response_200_entries_item

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
