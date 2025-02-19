from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_qos_circuit_profiles_response_200_profiles_item import (
        GetV1QosCircuitProfilesResponse200ProfilesItem,
    )


T = TypeVar("T", bound="GetV1QosCircuitProfilesResponse200")


@_attrs_define
class GetV1QosCircuitProfilesResponse200:
    """
    Attributes:
        profiles (Union[Unset, list['GetV1QosCircuitProfilesResponse200ProfilesItem']]):
    """

    profiles: Union[Unset, list["GetV1QosCircuitProfilesResponse200ProfilesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_qos_circuit_profiles_response_200_profiles_item import (
            GetV1QosCircuitProfilesResponse200ProfilesItem,
        )

        d = src_dict.copy()
        profiles = []
        _profiles = d.pop("profiles", UNSET)
        for profiles_item_data in _profiles or []:
            profiles_item = GetV1QosCircuitProfilesResponse200ProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        get_v1_qos_circuit_profiles_response_200 = cls(
            profiles=profiles,
        )

        get_v1_qos_circuit_profiles_response_200.additional_properties = d
        return get_v1_qos_circuit_profiles_response_200

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
