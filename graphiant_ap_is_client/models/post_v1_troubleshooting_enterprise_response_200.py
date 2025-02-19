from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_enterprise_response_200_sites_item import (
        PostV1TroubleshootingEnterpriseResponse200SitesItem,
    )


T = TypeVar("T", bound="PostV1TroubleshootingEnterpriseResponse200")


@_attrs_define
class PostV1TroubleshootingEnterpriseResponse200:
    """
    Attributes:
        sites (Union[Unset, list['PostV1TroubleshootingEnterpriseResponse200SitesItem']]):
    """

    sites: Union[Unset, list["PostV1TroubleshootingEnterpriseResponse200SitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_enterprise_response_200_sites_item import (
            PostV1TroubleshootingEnterpriseResponse200SitesItem,
        )

        d = src_dict.copy()
        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PostV1TroubleshootingEnterpriseResponse200SitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        post_v1_troubleshooting_enterprise_response_200 = cls(
            sites=sites,
        )

        post_v1_troubleshooting_enterprise_response_200.additional_properties = d
        return post_v1_troubleshooting_enterprise_response_200

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
