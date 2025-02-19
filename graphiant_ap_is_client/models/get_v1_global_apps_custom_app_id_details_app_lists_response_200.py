from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_custom_app_id_details_app_lists_response_200_app_lists_item import (
        GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200AppListsItem,
    )


T = TypeVar("T", bound="GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200")


@_attrs_define
class GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200:
    """
    Attributes:
        app_lists (Union[Unset, list['GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200AppListsItem']]):
    """

    app_lists: Union[Unset, list["GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200AppListsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_lists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_lists, Unset):
            app_lists = []
            for app_lists_item_data in self.app_lists:
                app_lists_item = app_lists_item_data.to_dict()
                app_lists.append(app_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_lists is not UNSET:
            field_dict["appLists"] = app_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_custom_app_id_details_app_lists_response_200_app_lists_item import (
            GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200AppListsItem,
        )

        d = src_dict.copy()
        app_lists = []
        _app_lists = d.pop("appLists", UNSET)
        for app_lists_item_data in _app_lists or []:
            app_lists_item = GetV1GlobalAppsCustomAppIdDetailsAppListsResponse200AppListsItem.from_dict(
                app_lists_item_data
            )

            app_lists.append(app_lists_item)

        get_v1_global_apps_custom_app_id_details_app_lists_response_200 = cls(
            app_lists=app_lists,
        )

        get_v1_global_apps_custom_app_id_details_app_lists_response_200.additional_properties = d
        return get_v1_global_apps_custom_app_id_details_app_lists_response_200

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
