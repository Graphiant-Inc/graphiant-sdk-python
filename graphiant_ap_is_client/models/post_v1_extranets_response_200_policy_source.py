from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_response_200_policy_source_excluded_devices_item import (
        PostV1ExtranetsResponse200PolicySourceExcludedDevicesItem,
    )
    from ..models.post_v1_extranets_response_200_policy_source_prefix_set import (
        PostV1ExtranetsResponse200PolicySourcePrefixSet,
    )
    from ..models.post_v1_extranets_response_200_policy_source_sites_item import (
        PostV1ExtranetsResponse200PolicySourceSitesItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsResponse200PolicySource")


@_attrs_define
class PostV1ExtranetsResponse200PolicySource:
    """
    Attributes:
        excluded_devices (Union[Unset, list['PostV1ExtranetsResponse200PolicySourceExcludedDevicesItem']]):
        prefix_set (Union[Unset, PostV1ExtranetsResponse200PolicySourcePrefixSet]):
        sites (Union[Unset, list['PostV1ExtranetsResponse200PolicySourceSitesItem']]):
    """

    excluded_devices: Union[Unset, list["PostV1ExtranetsResponse200PolicySourceExcludedDevicesItem"]] = UNSET
    prefix_set: Union[Unset, "PostV1ExtranetsResponse200PolicySourcePrefixSet"] = UNSET
    sites: Union[Unset, list["PostV1ExtranetsResponse200PolicySourceSitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.excluded_devices, Unset):
            excluded_devices = []
            for excluded_devices_item_data in self.excluded_devices:
                excluded_devices_item = excluded_devices_item_data.to_dict()
                excluded_devices.append(excluded_devices_item)

        prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prefix_set, Unset):
            prefix_set = self.prefix_set.to_dict()

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_devices is not UNSET:
            field_dict["excludedDevices"] = excluded_devices
        if prefix_set is not UNSET:
            field_dict["prefixSet"] = prefix_set
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_response_200_policy_source_excluded_devices_item import (
            PostV1ExtranetsResponse200PolicySourceExcludedDevicesItem,
        )
        from ..models.post_v1_extranets_response_200_policy_source_prefix_set import (
            PostV1ExtranetsResponse200PolicySourcePrefixSet,
        )
        from ..models.post_v1_extranets_response_200_policy_source_sites_item import (
            PostV1ExtranetsResponse200PolicySourceSitesItem,
        )

        d = src_dict.copy()
        excluded_devices = []
        _excluded_devices = d.pop("excludedDevices", UNSET)
        for excluded_devices_item_data in _excluded_devices or []:
            excluded_devices_item = PostV1ExtranetsResponse200PolicySourceExcludedDevicesItem.from_dict(
                excluded_devices_item_data
            )

            excluded_devices.append(excluded_devices_item)

        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PostV1ExtranetsResponse200PolicySourcePrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PostV1ExtranetsResponse200PolicySourcePrefixSet.from_dict(_prefix_set)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PostV1ExtranetsResponse200PolicySourceSitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        post_v1_extranets_response_200_policy_source = cls(
            excluded_devices=excluded_devices,
            prefix_set=prefix_set,
            sites=sites,
        )

        post_v1_extranets_response_200_policy_source.additional_properties = d
        return post_v1_extranets_response_200_policy_source

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
