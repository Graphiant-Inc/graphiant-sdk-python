from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp")


@_attrs_define
class GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp:
    """
    Attributes:
        expiry (Union[Unset, str]):  Example: TYPE_UINT32.
        unidirectional_flow_limit (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    expiry: Union[Unset, str] = UNSET
    unidirectional_flow_limit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry = self.expiry

        unidirectional_flow_limit = self.unidirectional_flow_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if unidirectional_flow_limit is not UNSET:
            field_dict["unidirectionalFlowLimit"] = unidirectional_flow_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        expiry = d.pop("expiry", UNSET)

        unidirectional_flow_limit = d.pop("unidirectionalFlowLimit", UNSET)

        get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_udp = cls(
            expiry=expiry,
            unidirectional_flow_limit=unidirectional_flow_limit,
        )

        get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_udp.additional_properties = d
        return get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_udp

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
