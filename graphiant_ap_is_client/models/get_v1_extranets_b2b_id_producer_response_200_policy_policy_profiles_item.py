from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1ExtranetsB2BIdProducerResponse200PolicyPolicyProfilesItem")


@_attrs_define
class GetV1ExtranetsB2BIdProducerResponse200PolicyPolicyProfilesItem:
    """
    Attributes:
        ports (Union[Unset, list[str]]):  Example: ['TYPE_INT32'].
        protocol (Union[Unset, str]):  Example: TYPE_INT32.
    """

    ports: Union[Unset, list[str]] = UNSET
    protocol: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ports: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ports is not UNSET:
            field_dict["ports"] = ports
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ports = cast(list[str], d.pop("ports", UNSET))

        protocol = d.pop("protocol", UNSET)

        get_v1_extranets_b2b_id_producer_response_200_policy_policy_profiles_item = cls(
            ports=ports,
            protocol=protocol,
        )

        get_v1_extranets_b2b_id_producer_response_200_policy_policy_profiles_item.additional_properties = d
        return get_v1_extranets_b2b_id_producer_response_200_policy_policy_profiles_item

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
