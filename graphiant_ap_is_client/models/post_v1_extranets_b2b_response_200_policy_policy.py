from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_response_200_policy_policy_profiles_item import (
        PostV1ExtranetsB2BResponse200PolicyPolicyProfilesItem,
    )
    from ..models.post_v1_extranets_b2b_response_200_policy_policy_sites_item import (
        PostV1ExtranetsB2BResponse200PolicyPolicySitesItem,
    )
    from ..models.post_v1_extranets_b2b_response_200_policy_policy_sla import (
        PostV1ExtranetsB2BResponse200PolicyPolicySla,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BResponse200PolicyPolicy")


@_attrs_define
class PostV1ExtranetsB2BResponse200PolicyPolicy:
    """
    Attributes:
        nat_pools (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        profiles (Union[Unset, list['PostV1ExtranetsB2BResponse200PolicyPolicyProfilesItem']]):
        service_lan_segment (Union[Unset, str]):  Example: TYPE_INT64.
        service_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        sites (Union[Unset, list['PostV1ExtranetsB2BResponse200PolicyPolicySitesItem']]):
        sla (Union[Unset, PostV1ExtranetsB2BResponse200PolicyPolicySla]):
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    nat_pools: Union[Unset, list[str]] = UNSET
    profiles: Union[Unset, list["PostV1ExtranetsB2BResponse200PolicyPolicyProfilesItem"]] = UNSET
    service_lan_segment: Union[Unset, str] = UNSET
    service_prefixes: Union[Unset, list[str]] = UNSET
    sites: Union[Unset, list["PostV1ExtranetsB2BResponse200PolicyPolicySitesItem"]] = UNSET
    sla: Union[Unset, "PostV1ExtranetsB2BResponse200PolicyPolicySla"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nat_pools: Union[Unset, list[str]] = UNSET
        if not isinstance(self.nat_pools, Unset):
            nat_pools = self.nat_pools

        profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        service_lan_segment = self.service_lan_segment

        service_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.service_prefixes, Unset):
            service_prefixes = self.service_prefixes

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        sla: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sla, Unset):
            sla = self.sla.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nat_pools is not UNSET:
            field_dict["natPools"] = nat_pools
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if service_lan_segment is not UNSET:
            field_dict["serviceLanSegment"] = service_lan_segment
        if service_prefixes is not UNSET:
            field_dict["servicePrefixes"] = service_prefixes
        if sites is not UNSET:
            field_dict["sites"] = sites
        if sla is not UNSET:
            field_dict["sla"] = sla
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_response_200_policy_policy_profiles_item import (
            PostV1ExtranetsB2BResponse200PolicyPolicyProfilesItem,
        )
        from ..models.post_v1_extranets_b2b_response_200_policy_policy_sites_item import (
            PostV1ExtranetsB2BResponse200PolicyPolicySitesItem,
        )
        from ..models.post_v1_extranets_b2b_response_200_policy_policy_sla import (
            PostV1ExtranetsB2BResponse200PolicyPolicySla,
        )

        d = src_dict.copy()
        nat_pools = cast(list[str], d.pop("natPools", UNSET))

        profiles = []
        _profiles = d.pop("profiles", UNSET)
        for profiles_item_data in _profiles or []:
            profiles_item = PostV1ExtranetsB2BResponse200PolicyPolicyProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        service_lan_segment = d.pop("serviceLanSegment", UNSET)

        service_prefixes = cast(list[str], d.pop("servicePrefixes", UNSET))

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PostV1ExtranetsB2BResponse200PolicyPolicySitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        _sla = d.pop("sla", UNSET)
        sla: Union[Unset, PostV1ExtranetsB2BResponse200PolicyPolicySla]
        if isinstance(_sla, Unset):
            sla = UNSET
        else:
            sla = PostV1ExtranetsB2BResponse200PolicyPolicySla.from_dict(_sla)

        type_ = d.pop("type", UNSET)

        post_v1_extranets_b2b_response_200_policy_policy = cls(
            nat_pools=nat_pools,
            profiles=profiles,
            service_lan_segment=service_lan_segment,
            service_prefixes=service_prefixes,
            sites=sites,
            sla=sla,
            type_=type_,
        )

        post_v1_extranets_b2b_response_200_policy_policy.additional_properties = d
        return post_v1_extranets_b2b_response_200_policy_policy

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
