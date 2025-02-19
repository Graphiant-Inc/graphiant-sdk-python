from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile")


@_attrs_define
class PatchV1GlobalConfigBodyVpnProfilesItemValueVpnProfile:
    """
    Attributes:
        anti_replay_window_size (Union[Unset, str]):  Example: TYPE_UINT32.
        dpd_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        esn (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ike_dh_group (Union[Unset, str]):  Example: TYPE_ENUM.
        ike_encryption_alg (Union[Unset, str]):  Example: TYPE_ENUM.
        ike_integrity (Union[Unset, str]):  Example: TYPE_ENUM.
        ipsec_encryption_alg (Union[Unset, str]):  Example: TYPE_ENUM.
        ipsec_integrity (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        perfect_forward_secrecy (Union[Unset, str]):  Example: TYPE_ENUM.
        reauth_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        rekey_interval (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    anti_replay_window_size: Union[Unset, str] = UNSET
    dpd_interval: Union[Unset, str] = UNSET
    esn: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ike_dh_group: Union[Unset, str] = UNSET
    ike_encryption_alg: Union[Unset, str] = UNSET
    ike_integrity: Union[Unset, str] = UNSET
    ipsec_encryption_alg: Union[Unset, str] = UNSET
    ipsec_integrity: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    perfect_forward_secrecy: Union[Unset, str] = UNSET
    reauth_interval: Union[Unset, str] = UNSET
    rekey_interval: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anti_replay_window_size = self.anti_replay_window_size

        dpd_interval = self.dpd_interval

        esn = self.esn

        id = self.id

        ike_dh_group = self.ike_dh_group

        ike_encryption_alg = self.ike_encryption_alg

        ike_integrity = self.ike_integrity

        ipsec_encryption_alg = self.ipsec_encryption_alg

        ipsec_integrity = self.ipsec_integrity

        name = self.name

        perfect_forward_secrecy = self.perfect_forward_secrecy

        reauth_interval = self.reauth_interval

        rekey_interval = self.rekey_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anti_replay_window_size is not UNSET:
            field_dict["antiReplayWindowSize"] = anti_replay_window_size
        if dpd_interval is not UNSET:
            field_dict["dpdInterval"] = dpd_interval
        if esn is not UNSET:
            field_dict["esn"] = esn
        if id is not UNSET:
            field_dict["id"] = id
        if ike_dh_group is not UNSET:
            field_dict["ikeDhGroup"] = ike_dh_group
        if ike_encryption_alg is not UNSET:
            field_dict["ikeEncryptionAlg"] = ike_encryption_alg
        if ike_integrity is not UNSET:
            field_dict["ikeIntegrity"] = ike_integrity
        if ipsec_encryption_alg is not UNSET:
            field_dict["ipsecEncryptionAlg"] = ipsec_encryption_alg
        if ipsec_integrity is not UNSET:
            field_dict["ipsecIntegrity"] = ipsec_integrity
        if name is not UNSET:
            field_dict["name"] = name
        if perfect_forward_secrecy is not UNSET:
            field_dict["perfectForwardSecrecy"] = perfect_forward_secrecy
        if reauth_interval is not UNSET:
            field_dict["reauthInterval"] = reauth_interval
        if rekey_interval is not UNSET:
            field_dict["rekeyInterval"] = rekey_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        anti_replay_window_size = d.pop("antiReplayWindowSize", UNSET)

        dpd_interval = d.pop("dpdInterval", UNSET)

        esn = d.pop("esn", UNSET)

        id = d.pop("id", UNSET)

        ike_dh_group = d.pop("ikeDhGroup", UNSET)

        ike_encryption_alg = d.pop("ikeEncryptionAlg", UNSET)

        ike_integrity = d.pop("ikeIntegrity", UNSET)

        ipsec_encryption_alg = d.pop("ipsecEncryptionAlg", UNSET)

        ipsec_integrity = d.pop("ipsecIntegrity", UNSET)

        name = d.pop("name", UNSET)

        perfect_forward_secrecy = d.pop("perfectForwardSecrecy", UNSET)

        reauth_interval = d.pop("reauthInterval", UNSET)

        rekey_interval = d.pop("rekeyInterval", UNSET)

        patch_v1_global_config_body_vpn_profiles_item_value_vpn_profile = cls(
            anti_replay_window_size=anti_replay_window_size,
            dpd_interval=dpd_interval,
            esn=esn,
            id=id,
            ike_dh_group=ike_dh_group,
            ike_encryption_alg=ike_encryption_alg,
            ike_integrity=ike_integrity,
            ipsec_encryption_alg=ipsec_encryption_alg,
            ipsec_integrity=ipsec_integrity,
            name=name,
            perfect_forward_secrecy=perfect_forward_secrecy,
            reauth_interval=reauth_interval,
            rekey_interval=rekey_interval,
        )

        patch_v1_global_config_body_vpn_profiles_item_value_vpn_profile.additional_properties = d
        return patch_v1_global_config_body_vpn_profiles_item_value_vpn_profile

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
