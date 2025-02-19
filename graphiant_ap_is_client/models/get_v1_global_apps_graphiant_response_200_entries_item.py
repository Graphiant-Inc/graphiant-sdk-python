from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_graphiant_response_200_entries_item_app import (
        GetV1GlobalAppsGraphiantResponse200EntriesItemApp,
    )


T = TypeVar("T", bound="GetV1GlobalAppsGraphiantResponse200EntriesItem")


@_attrs_define
class GetV1GlobalAppsGraphiantResponse200EntriesItem:
    """
    Attributes:
        app (Union[Unset, GetV1GlobalAppsGraphiantResponse200EntriesItemApp]):
        app_list_reference_count (Union[Unset, str]):  Example: TYPE_INT32.
        policy_reference_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    app: Union[Unset, "GetV1GlobalAppsGraphiantResponse200EntriesItemApp"] = UNSET
    app_list_reference_count: Union[Unset, str] = UNSET
    policy_reference_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        app_list_reference_count = self.app_list_reference_count

        policy_reference_count = self.policy_reference_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if app_list_reference_count is not UNSET:
            field_dict["appListReferenceCount"] = app_list_reference_count
        if policy_reference_count is not UNSET:
            field_dict["policyReferenceCount"] = policy_reference_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_graphiant_response_200_entries_item_app import (
            GetV1GlobalAppsGraphiantResponse200EntriesItemApp,
        )

        d = src_dict.copy()
        _app = d.pop("app", UNSET)
        app: Union[Unset, GetV1GlobalAppsGraphiantResponse200EntriesItemApp]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = GetV1GlobalAppsGraphiantResponse200EntriesItemApp.from_dict(_app)

        app_list_reference_count = d.pop("appListReferenceCount", UNSET)

        policy_reference_count = d.pop("policyReferenceCount", UNSET)

        get_v1_global_apps_graphiant_response_200_entries_item = cls(
            app=app,
            app_list_reference_count=app_list_reference_count,
            policy_reference_count=policy_reference_count,
        )

        get_v1_global_apps_graphiant_response_200_entries_item.additional_properties = d
        return get_v1_global_apps_graphiant_response_200_entries_item

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
