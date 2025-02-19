from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem")


@_attrs_define
class PutV1GlobalAppsAppListsAppListIdBodyAppListConfigAppsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        put_v1_global_apps_app_lists_app_list_id_body_app_list_config_apps_item = cls(
            id=id,
            type_=type_,
        )

        put_v1_global_apps_app_lists_app_list_id_body_app_list_config_apps_item.additional_properties = d
        return put_v1_global_apps_app_lists_app_list_id_body_app_list_config_apps_item

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
