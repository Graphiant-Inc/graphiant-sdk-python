from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GatewaysBodyDetailsAzure")


@_attrs_define
class PostV1GatewaysBodyDetailsAzure:
    """
    Attributes:
        ms_peering_vlan_id (Union[Unset, str]):  Example: TYPE_UINT32.
        routing_policy (Union[Unset, str]):  Example: TYPE_STRING.
        service_key (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ms_peering_vlan_id: Union[Unset, str] = UNSET
    routing_policy: Union[Unset, str] = UNSET
    service_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ms_peering_vlan_id = self.ms_peering_vlan_id

        routing_policy = self.routing_policy

        service_key = self.service_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ms_peering_vlan_id is not UNSET:
            field_dict["msPeeringVlanId"] = ms_peering_vlan_id
        if routing_policy is not UNSET:
            field_dict["routingPolicy"] = routing_policy
        if service_key is not UNSET:
            field_dict["serviceKey"] = service_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ms_peering_vlan_id = d.pop("msPeeringVlanId", UNSET)

        routing_policy = d.pop("routingPolicy", UNSET)

        service_key = d.pop("serviceKey", UNSET)

        post_v1_gateways_body_details_azure = cls(
            ms_peering_vlan_id=ms_peering_vlan_id,
            routing_policy=routing_policy,
            service_key=service_key,
        )

        post_v1_gateways_body_details_azure.additional_properties = d
        return post_v1_gateways_body_details_azure

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
