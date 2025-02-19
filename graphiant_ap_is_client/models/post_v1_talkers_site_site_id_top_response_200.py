from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_talkers_site_site_id_top_response_200_apps_utilization_item import (
        PostV1TalkersSiteSiteIdTopResponse200AppsUtilizationItem,
    )


T = TypeVar("T", bound="PostV1TalkersSiteSiteIdTopResponse200")


@_attrs_define
class PostV1TalkersSiteSiteIdTopResponse200:
    """
    Attributes:
        apps_utilization (Union[Unset, list['PostV1TalkersSiteSiteIdTopResponse200AppsUtilizationItem']]):
    """

    apps_utilization: Union[Unset, list["PostV1TalkersSiteSiteIdTopResponse200AppsUtilizationItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps_utilization: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps_utilization, Unset):
            apps_utilization = []
            for apps_utilization_item_data in self.apps_utilization:
                apps_utilization_item = apps_utilization_item_data.to_dict()
                apps_utilization.append(apps_utilization_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps_utilization is not UNSET:
            field_dict["appsUtilization"] = apps_utilization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_talkers_site_site_id_top_response_200_apps_utilization_item import (
            PostV1TalkersSiteSiteIdTopResponse200AppsUtilizationItem,
        )

        d = src_dict.copy()
        apps_utilization = []
        _apps_utilization = d.pop("appsUtilization", UNSET)
        for apps_utilization_item_data in _apps_utilization or []:
            apps_utilization_item = PostV1TalkersSiteSiteIdTopResponse200AppsUtilizationItem.from_dict(
                apps_utilization_item_data
            )

            apps_utilization.append(apps_utilization_item)

        post_v1_talkers_site_site_id_top_response_200 = cls(
            apps_utilization=apps_utilization,
        )

        post_v1_talkers_site_site_id_top_response_200.additional_properties = d
        return post_v1_talkers_site_site_id_top_response_200

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
