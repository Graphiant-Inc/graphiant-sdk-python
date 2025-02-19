from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_ipsec_profile_id_response_200_ipsec_profile import (
        GetV1GlobalIpsecProfileIdResponse200IpsecProfile,
    )


T = TypeVar("T", bound="GetV1GlobalIpsecProfileIdResponse200")


@_attrs_define
class GetV1GlobalIpsecProfileIdResponse200:
    """
    Attributes:
        ipsec_profile (Union[Unset, GetV1GlobalIpsecProfileIdResponse200IpsecProfile]):
    """

    ipsec_profile: Union[Unset, "GetV1GlobalIpsecProfileIdResponse200IpsecProfile"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipsec_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipsec_profile, Unset):
            ipsec_profile = self.ipsec_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipsec_profile is not UNSET:
            field_dict["ipsecProfile"] = ipsec_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_ipsec_profile_id_response_200_ipsec_profile import (
            GetV1GlobalIpsecProfileIdResponse200IpsecProfile,
        )

        d = src_dict.copy()
        _ipsec_profile = d.pop("ipsecProfile", UNSET)
        ipsec_profile: Union[Unset, GetV1GlobalIpsecProfileIdResponse200IpsecProfile]
        if isinstance(_ipsec_profile, Unset):
            ipsec_profile = UNSET
        else:
            ipsec_profile = GetV1GlobalIpsecProfileIdResponse200IpsecProfile.from_dict(_ipsec_profile)

        get_v1_global_ipsec_profile_id_response_200 = cls(
            ipsec_profile=ipsec_profile,
        )

        get_v1_global_ipsec_profile_id_response_200.additional_properties = d
        return get_v1_global_ipsec_profile_id_response_200

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
