from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalIpsecProfileResponse200IpsecProfilesItem")


@_attrs_define
class GetV1GlobalIpsecProfileResponse200IpsecProfilesItem:
    """
    Attributes:
        count (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ipsec_profile_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    count: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipsec_profile_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        id = self.id

        ipsec_profile_name = self.ipsec_profile_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if id is not UNSET:
            field_dict["id"] = id
        if ipsec_profile_name is not UNSET:
            field_dict["ipsecProfileName"] = ipsec_profile_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        id = d.pop("id", UNSET)

        ipsec_profile_name = d.pop("ipsecProfileName", UNSET)

        get_v1_global_ipsec_profile_response_200_ipsec_profiles_item = cls(
            count=count,
            id=id,
            ipsec_profile_name=ipsec_profile_name,
        )

        get_v1_global_ipsec_profile_response_200_ipsec_profiles_item.additional_properties = d
        return get_v1_global_ipsec_profile_response_200_ipsec_profiles_item

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
