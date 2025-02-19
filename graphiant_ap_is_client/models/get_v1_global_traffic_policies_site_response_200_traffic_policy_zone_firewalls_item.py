from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_ip import (
        GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp,
    )
    from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_udp import (
        GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp,
    )


T = TypeVar("T", bound="GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItem")


@_attrs_define
class GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItem:
    """
    Attributes:
        ip (Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp]):
        udp (Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp]):
        zone_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ip: Union[Unset, "GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp"] = UNSET
    udp: Union[Unset, "GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp"] = UNSET
    zone_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip.to_dict()

        udp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.udp, Unset):
            udp = self.udp.to_dict()

        zone_name = self.zone_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if udp is not UNSET:
            field_dict["udp"] = udp
        if zone_name is not UNSET:
            field_dict["zoneName"] = zone_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_ip import (
            GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp,
        )
        from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item_udp import (
            GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp,
        )

        d = src_dict.copy()
        _ip = d.pop("ip", UNSET)
        ip: Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp]
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemIp.from_dict(_ip)

        _udp = d.pop("udp", UNSET)
        udp: Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp]
        if isinstance(_udp, Unset):
            udp = UNSET
        else:
            udp = GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicyZoneFirewallsItemUdp.from_dict(_udp)

        zone_name = d.pop("zoneName", UNSET)

        get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item = cls(
            ip=ip,
            udp=udp,
            zone_name=zone_name,
        )

        get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item.additional_properties = d
        return get_v1_global_traffic_policies_site_response_200_traffic_policy_zone_firewalls_item

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
