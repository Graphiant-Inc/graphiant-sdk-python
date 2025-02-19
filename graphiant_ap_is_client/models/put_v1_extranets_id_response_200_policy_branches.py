from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_extranets_id_response_200_policy_branches_excluded_devices_item import (
        PutV1ExtranetsIdResponse200PolicyBranchesExcludedDevicesItem,
    )
    from ..models.put_v1_extranets_id_response_200_policy_branches_prefix_set import (
        PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet,
    )
    from ..models.put_v1_extranets_id_response_200_policy_branches_sites_item import (
        PutV1ExtranetsIdResponse200PolicyBranchesSitesItem,
    )


T = TypeVar("T", bound="PutV1ExtranetsIdResponse200PolicyBranches")


@_attrs_define
class PutV1ExtranetsIdResponse200PolicyBranches:
    """
    Attributes:
        excluded_devices (Union[Unset, list['PutV1ExtranetsIdResponse200PolicyBranchesExcludedDevicesItem']]):
        prefix_set (Union[Unset, PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet]):
        sites (Union[Unset, list['PutV1ExtranetsIdResponse200PolicyBranchesSitesItem']]):
    """

    excluded_devices: Union[Unset, list["PutV1ExtranetsIdResponse200PolicyBranchesExcludedDevicesItem"]] = UNSET
    prefix_set: Union[Unset, "PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet"] = UNSET
    sites: Union[Unset, list["PutV1ExtranetsIdResponse200PolicyBranchesSitesItem"]] = UNSET
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
        from ..models.put_v1_extranets_id_response_200_policy_branches_excluded_devices_item import (
            PutV1ExtranetsIdResponse200PolicyBranchesExcludedDevicesItem,
        )
        from ..models.put_v1_extranets_id_response_200_policy_branches_prefix_set import (
            PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet,
        )
        from ..models.put_v1_extranets_id_response_200_policy_branches_sites_item import (
            PutV1ExtranetsIdResponse200PolicyBranchesSitesItem,
        )

        d = src_dict.copy()
        excluded_devices = []
        _excluded_devices = d.pop("excludedDevices", UNSET)
        for excluded_devices_item_data in _excluded_devices or []:
            excluded_devices_item = PutV1ExtranetsIdResponse200PolicyBranchesExcludedDevicesItem.from_dict(
                excluded_devices_item_data
            )

            excluded_devices.append(excluded_devices_item)

        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PutV1ExtranetsIdResponse200PolicyBranchesPrefixSet.from_dict(_prefix_set)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PutV1ExtranetsIdResponse200PolicyBranchesSitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        put_v1_extranets_id_response_200_policy_branches = cls(
            excluded_devices=excluded_devices,
            prefix_set=prefix_set,
            sites=sites,
        )

        put_v1_extranets_id_response_200_policy_branches.additional_properties = d
        return put_v1_extranets_id_response_200_policy_branches

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
