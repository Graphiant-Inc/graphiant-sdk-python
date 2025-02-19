from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranet_sites_usage_top_response_200_top_sites_item import (
        PostV1ExtranetSitesUsageTopResponse200TopSitesItem,
    )


T = TypeVar("T", bound="PostV1ExtranetSitesUsageTopResponse200")


@_attrs_define
class PostV1ExtranetSitesUsageTopResponse200:
    """
    Attributes:
        top_sites (Union[Unset, list['PostV1ExtranetSitesUsageTopResponse200TopSitesItem']]):
    """

    top_sites: Union[Unset, list["PostV1ExtranetSitesUsageTopResponse200TopSitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_sites, Unset):
            top_sites = []
            for top_sites_item_data in self.top_sites:
                top_sites_item = top_sites_item_data.to_dict()
                top_sites.append(top_sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_sites is not UNSET:
            field_dict["topSites"] = top_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranet_sites_usage_top_response_200_top_sites_item import (
            PostV1ExtranetSitesUsageTopResponse200TopSitesItem,
        )

        d = src_dict.copy()
        top_sites = []
        _top_sites = d.pop("topSites", UNSET)
        for top_sites_item_data in _top_sites or []:
            top_sites_item = PostV1ExtranetSitesUsageTopResponse200TopSitesItem.from_dict(top_sites_item_data)

            top_sites.append(top_sites_item)

        post_v1_extranet_sites_usage_top_response_200 = cls(
            top_sites=top_sites,
        )

        post_v1_extranet_sites_usage_top_response_200.additional_properties = d
        return post_v1_extranet_sites_usage_top_response_200

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
