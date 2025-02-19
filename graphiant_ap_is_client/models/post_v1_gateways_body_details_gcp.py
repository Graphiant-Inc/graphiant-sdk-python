from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GatewaysBodyDetailsGcp")


@_attrs_define
class PostV1GatewaysBodyDetailsGcp:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        pairing_key (Union[Unset, str]):  Example: TYPE_STRING.
        routing_policy (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    pairing_key: Union[Unset, str] = UNSET
    routing_policy: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        pairing_key = self.pairing_key

        routing_policy = self.routing_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if pairing_key is not UNSET:
            field_dict["pairingKey"] = pairing_key
        if routing_policy is not UNSET:
            field_dict["routingPolicy"] = routing_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        pairing_key = d.pop("pairingKey", UNSET)

        routing_policy = d.pop("routingPolicy", UNSET)

        post_v1_gateways_body_details_gcp = cls(
            description=description,
            pairing_key=pairing_key,
            routing_policy=routing_policy,
        )

        post_v1_gateways_body_details_gcp.additional_properties = d
        return post_v1_gateways_body_details_gcp

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
