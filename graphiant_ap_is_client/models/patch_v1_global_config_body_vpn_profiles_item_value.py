from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_vpn_profiles_item_value_vpn_profile import (
        PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyVpnProfilesItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyVpnProfilesItemValue:
    """
    Attributes:
        vpn_profile (Union[Unset, PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile]):
    """

    vpn_profile: Union[Unset, "PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vpn_profile, Unset):
            vpn_profile = self.vpn_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_profile is not UNSET:
            field_dict["vpnProfile"] = vpn_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_vpn_profiles_item_value_vpn_profile import (
            PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile,
        )

        d = src_dict.copy()
        _vpn_profile = d.pop("vpnProfile", UNSET)
        vpn_profile: Union[Unset, PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile]
        if isinstance(_vpn_profile, Unset):
            vpn_profile = UNSET
        else:
            vpn_profile = PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile.from_dict(_vpn_profile)

        patch_v1_global_config_body_vpn_profiles_item_value = cls(
            vpn_profile=vpn_profile,
        )

        patch_v1_global_config_body_vpn_profiles_item_value.additional_properties = d
        return patch_v1_global_config_body_vpn_profiles_item_value

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
