from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_app_lists_response_200_entries_item_app_list import (
        GetV1GlobalAppsAppListsResponse200EntriesItemAppList,
    )


T = TypeVar("T", bound="GetV1GlobalAppsAppListsResponse200EntriesItem")


@_attrs_define
class GetV1GlobalAppsAppListsResponse200EntriesItem:
    """
    Attributes:
        app_count (Union[Unset, str]):  Example: TYPE_INT32.
        app_list (Union[Unset, GetV1GlobalAppsAppListsResponse200EntriesItemAppList]):
        policy_reference_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    app_count: Union[Unset, str] = UNSET
    app_list: Union[Unset, "GetV1GlobalAppsAppListsResponse200EntriesItemAppList"] = UNSET
    policy_reference_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_count = self.app_count

        app_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_list, Unset):
            app_list = self.app_list.to_dict()

        policy_reference_count = self.policy_reference_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_count is not UNSET:
            field_dict["appCount"] = app_count
        if app_list is not UNSET:
            field_dict["appList"] = app_list
        if policy_reference_count is not UNSET:
            field_dict["policyReferenceCount"] = policy_reference_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_app_lists_response_200_entries_item_app_list import (
            GetV1GlobalAppsAppListsResponse200EntriesItemAppList,
        )

        d = src_dict.copy()
        app_count = d.pop("appCount", UNSET)

        _app_list = d.pop("appList", UNSET)
        app_list: Union[Unset, GetV1GlobalAppsAppListsResponse200EntriesItemAppList]
        if isinstance(_app_list, Unset):
            app_list = UNSET
        else:
            app_list = GetV1GlobalAppsAppListsResponse200EntriesItemAppList.from_dict(_app_list)

        policy_reference_count = d.pop("policyReferenceCount", UNSET)

        get_v1_global_apps_app_lists_response_200_entries_item = cls(
            app_count=app_count,
            app_list=app_list,
            policy_reference_count=policy_reference_count,
        )

        get_v1_global_apps_app_lists_response_200_entries_item.additional_properties = d
        return get_v1_global_apps_app_lists_response_200_entries_item

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
