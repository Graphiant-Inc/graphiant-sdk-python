from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_dpi_applications_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_network_lists_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyNetworkListsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_port_lists_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyPortListsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_traffic_rulesets_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyTrafficRulesetsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_zone_firewalls_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItem,
    )
    from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_zone_pairs_item import (
        PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZonePairsItem,
    )


T = TypeVar("T", bound="PostV1GlobalTrafficPoliciesResponse200TrafficPolicy")


@_attrs_define
class PostV1GlobalTrafficPoliciesResponse200TrafficPolicy:
    """
    Attributes:
        dpi_applications (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem']]):
        network_lists (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyNetworkListsItem']]):
        port_lists (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyPortListsItem']]):
        security_rulesets (Union[Unset,
            list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItem']]):
        traffic_rulesets (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyTrafficRulesetsItem']]):
        zone_firewalls (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItem']]):
        zone_pairs (Union[Unset, list['PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZonePairsItem']]):
    """

    dpi_applications: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem"]] = (
        UNSET
    )
    network_lists: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyNetworkListsItem"]] = UNSET
    port_lists: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyPortListsItem"]] = UNSET
    security_rulesets: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItem"]] = (
        UNSET
    )
    traffic_rulesets: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyTrafficRulesetsItem"]] = (
        UNSET
    )
    zone_firewalls: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItem"]] = UNSET
    zone_pairs: Union[Unset, list["PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZonePairsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dpi_applications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dpi_applications, Unset):
            dpi_applications = []
            for dpi_applications_item_data in self.dpi_applications:
                dpi_applications_item = dpi_applications_item_data.to_dict()
                dpi_applications.append(dpi_applications_item)

        network_lists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.network_lists, Unset):
            network_lists = []
            for network_lists_item_data in self.network_lists:
                network_lists_item = network_lists_item_data.to_dict()
                network_lists.append(network_lists_item)

        port_lists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.port_lists, Unset):
            port_lists = []
            for port_lists_item_data in self.port_lists:
                port_lists_item = port_lists_item_data.to_dict()
                port_lists.append(port_lists_item)

        security_rulesets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.security_rulesets, Unset):
            security_rulesets = []
            for security_rulesets_item_data in self.security_rulesets:
                security_rulesets_item = security_rulesets_item_data.to_dict()
                security_rulesets.append(security_rulesets_item)

        traffic_rulesets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_rulesets, Unset):
            traffic_rulesets = []
            for traffic_rulesets_item_data in self.traffic_rulesets:
                traffic_rulesets_item = traffic_rulesets_item_data.to_dict()
                traffic_rulesets.append(traffic_rulesets_item)

        zone_firewalls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zone_firewalls, Unset):
            zone_firewalls = []
            for zone_firewalls_item_data in self.zone_firewalls:
                zone_firewalls_item = zone_firewalls_item_data.to_dict()
                zone_firewalls.append(zone_firewalls_item)

        zone_pairs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zone_pairs, Unset):
            zone_pairs = []
            for zone_pairs_item_data in self.zone_pairs:
                zone_pairs_item = zone_pairs_item_data.to_dict()
                zone_pairs.append(zone_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dpi_applications is not UNSET:
            field_dict["dpiApplications"] = dpi_applications
        if network_lists is not UNSET:
            field_dict["networkLists"] = network_lists
        if port_lists is not UNSET:
            field_dict["portLists"] = port_lists
        if security_rulesets is not UNSET:
            field_dict["securityRulesets"] = security_rulesets
        if traffic_rulesets is not UNSET:
            field_dict["trafficRulesets"] = traffic_rulesets
        if zone_firewalls is not UNSET:
            field_dict["zoneFirewalls"] = zone_firewalls
        if zone_pairs is not UNSET:
            field_dict["zonePairs"] = zone_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_dpi_applications_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_network_lists_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyNetworkListsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_port_lists_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyPortListsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_security_rulesets_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_traffic_rulesets_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyTrafficRulesetsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_zone_firewalls_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItem,
        )
        from ..models.post_v1_global_traffic_policies_response_200_traffic_policy_zone_pairs_item import (
            PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZonePairsItem,
        )

        d = src_dict.copy()
        dpi_applications = []
        _dpi_applications = d.pop("dpiApplications", UNSET)
        for dpi_applications_item_data in _dpi_applications or []:
            dpi_applications_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem.from_dict(
                dpi_applications_item_data
            )

            dpi_applications.append(dpi_applications_item)

        network_lists = []
        _network_lists = d.pop("networkLists", UNSET)
        for network_lists_item_data in _network_lists or []:
            network_lists_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyNetworkListsItem.from_dict(
                network_lists_item_data
            )

            network_lists.append(network_lists_item)

        port_lists = []
        _port_lists = d.pop("portLists", UNSET)
        for port_lists_item_data in _port_lists or []:
            port_lists_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyPortListsItem.from_dict(
                port_lists_item_data
            )

            port_lists.append(port_lists_item)

        security_rulesets = []
        _security_rulesets = d.pop("securityRulesets", UNSET)
        for security_rulesets_item_data in _security_rulesets or []:
            security_rulesets_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicySecurityRulesetsItem.from_dict(
                security_rulesets_item_data
            )

            security_rulesets.append(security_rulesets_item)

        traffic_rulesets = []
        _traffic_rulesets = d.pop("trafficRulesets", UNSET)
        for traffic_rulesets_item_data in _traffic_rulesets or []:
            traffic_rulesets_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyTrafficRulesetsItem.from_dict(
                traffic_rulesets_item_data
            )

            traffic_rulesets.append(traffic_rulesets_item)

        zone_firewalls = []
        _zone_firewalls = d.pop("zoneFirewalls", UNSET)
        for zone_firewalls_item_data in _zone_firewalls or []:
            zone_firewalls_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZoneFirewallsItem.from_dict(
                zone_firewalls_item_data
            )

            zone_firewalls.append(zone_firewalls_item)

        zone_pairs = []
        _zone_pairs = d.pop("zonePairs", UNSET)
        for zone_pairs_item_data in _zone_pairs or []:
            zone_pairs_item = PostV1GlobalTrafficPoliciesResponse200TrafficPolicyZonePairsItem.from_dict(
                zone_pairs_item_data
            )

            zone_pairs.append(zone_pairs_item)

        post_v1_global_traffic_policies_response_200_traffic_policy = cls(
            dpi_applications=dpi_applications,
            network_lists=network_lists,
            port_lists=port_lists,
            security_rulesets=security_rulesets,
            traffic_rulesets=traffic_rulesets,
            zone_firewalls=zone_firewalls,
            zone_pairs=zone_pairs,
        )

        post_v1_global_traffic_policies_response_200_traffic_policy.additional_properties = d
        return post_v1_global_traffic_policies_response_200_traffic_policy

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
