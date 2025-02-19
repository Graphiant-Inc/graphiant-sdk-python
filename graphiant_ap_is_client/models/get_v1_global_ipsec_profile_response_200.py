from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_ipsec_profile_response_200_ipsec_profiles_item import (
        GetV1GlobalIpsecProfileResponse200IpsecProfilesItem,
    )


T = TypeVar("T", bound="GetV1GlobalIpsecProfileResponse200")


@_attrs_define
class GetV1GlobalIpsecProfileResponse200:
    """
    Attributes:
        ipsec_profiles (Union[Unset, list['GetV1GlobalIpsecProfileResponse200IpsecProfilesItem']]):
    """

    ipsec_profiles: Union[Unset, list["GetV1GlobalIpsecProfileResponse200IpsecProfilesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipsec_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipsec_profiles, Unset):
            ipsec_profiles = []
            for ipsec_profiles_item_data in self.ipsec_profiles:
                ipsec_profiles_item = ipsec_profiles_item_data.to_dict()
                ipsec_profiles.append(ipsec_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipsec_profiles is not UNSET:
            field_dict["ipsecProfiles"] = ipsec_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_ipsec_profile_response_200_ipsec_profiles_item import (
            GetV1GlobalIpsecProfileResponse200IpsecProfilesItem,
        )

        d = src_dict.copy()
        ipsec_profiles = []
        _ipsec_profiles = d.pop("ipsecProfiles", UNSET)
        for ipsec_profiles_item_data in _ipsec_profiles or []:
            ipsec_profiles_item = GetV1GlobalIpsecProfileResponse200IpsecProfilesItem.from_dict(
                ipsec_profiles_item_data
            )

            ipsec_profiles.append(ipsec_profiles_item)

        get_v1_global_ipsec_profile_response_200 = cls(
            ipsec_profiles=ipsec_profiles,
        )

        get_v1_global_ipsec_profile_response_200.additional_properties = d
        return get_v1_global_ipsec_profile_response_200

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
