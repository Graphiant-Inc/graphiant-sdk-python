from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_global_apps_app_lists_app_list_id_body_app_list_config_apps_item import (
        PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem,
    )


T = TypeVar("T", bound="PutV1GlobalAppsAppListsAppListIdBodyAppListConfig")


@_attrs_define
class PutV1GlobalAppsAppListsAppListIdBodyAppListConfig:
    """
    Attributes:
        apps (Union[Unset, list['PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem']]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    apps: Union[Unset, list["PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem"]] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_global_apps_app_lists_app_list_id_body_app_list_config_apps_item import (
            PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem,
        )

        d = src_dict.copy()
        apps = []
        _apps = d.pop("apps", UNSET)
        for apps_item_data in _apps or []:
            apps_item = PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem.from_dict(apps_item_data)

            apps.append(apps_item)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        put_v1_global_apps_app_lists_app_list_id_body_app_list_config = cls(
            apps=apps,
            description=description,
            name=name,
        )

        put_v1_global_apps_app_lists_app_list_id_body_app_list_config.additional_properties = d
        return put_v1_global_apps_app_lists_app_list_id_body_app_list_config

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
