from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_dpi_applications_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_network_lists_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesNetworkListsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_port_lists_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesPortListsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_security_rulesets_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesSecurityRulesetsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_traffic_rulesets_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_zone_firewalls_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItem,
    )
    from ..models.patch_v1_global_config_body_traffic_policies_zones_item import (
        PatchV1GlobalConfigBodyTrafficPoliciesZonesItem,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPolicies")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPolicies:
    """
    Attributes:
        dpi_applications (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItem']]):
        network_lists (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesNetworkListsItem']]):
        port_lists (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesPortListsItem']]):
        security_rulesets (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesSecurityRulesetsItem']]):
        traffic_rulesets (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItem']]):
        zone_firewalls (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItem']]):
        zones (Union[Unset, list['PatchV1GlobalConfigBodyTrafficPoliciesZonesItem']]):
    """

    dpi_applications: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItem"]] = UNSET
    network_lists: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesNetworkListsItem"]] = UNSET
    port_lists: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesPortListsItem"]] = UNSET
    security_rulesets: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesSecurityRulesetsItem"]] = UNSET
    traffic_rulesets: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItem"]] = UNSET
    zone_firewalls: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItem"]] = UNSET
    zones: Union[Unset, list["PatchV1GlobalConfigBodyTrafficPoliciesZonesItem"]] = UNSET
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

        zones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = []
            for zones_item_data in self.zones:
                zones_item = zones_item_data.to_dict()
                zones.append(zones_item)

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
        if zones is not UNSET:
            field_dict["zones"] = zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_dpi_applications_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_network_lists_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesNetworkListsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_port_lists_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesPortListsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_security_rulesets_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesSecurityRulesetsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_traffic_rulesets_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_zone_firewalls_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItem,
        )
        from ..models.patch_v1_global_config_body_traffic_policies_zones_item import (
            PatchV1GlobalConfigBodyTrafficPoliciesZonesItem,
        )

        d = src_dict.copy()
        dpi_applications = []
        _dpi_applications = d.pop("dpiApplications", UNSET)
        for dpi_applications_item_data in _dpi_applications or []:
            dpi_applications_item = PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItem.from_dict(
                dpi_applications_item_data
            )

            dpi_applications.append(dpi_applications_item)

        network_lists = []
        _network_lists = d.pop("networkLists", UNSET)
        for network_lists_item_data in _network_lists or []:
            network_lists_item = PatchV1GlobalConfigBodyTrafficPoliciesNetworkListsItem.from_dict(
                network_lists_item_data
            )

            network_lists.append(network_lists_item)

        port_lists = []
        _port_lists = d.pop("portLists", UNSET)
        for port_lists_item_data in _port_lists or []:
            port_lists_item = PatchV1GlobalConfigBodyTrafficPoliciesPortListsItem.from_dict(port_lists_item_data)

            port_lists.append(port_lists_item)

        security_rulesets = []
        _security_rulesets = d.pop("securityRulesets", UNSET)
        for security_rulesets_item_data in _security_rulesets or []:
            security_rulesets_item = PatchV1GlobalConfigBodyTrafficPoliciesSecurityRulesetsItem.from_dict(
                security_rulesets_item_data
            )

            security_rulesets.append(security_rulesets_item)

        traffic_rulesets = []
        _traffic_rulesets = d.pop("trafficRulesets", UNSET)
        for traffic_rulesets_item_data in _traffic_rulesets or []:
            traffic_rulesets_item = PatchV1GlobalConfigBodyTrafficPoliciesTrafficRulesetsItem.from_dict(
                traffic_rulesets_item_data
            )

            traffic_rulesets.append(traffic_rulesets_item)

        zone_firewalls = []
        _zone_firewalls = d.pop("zoneFirewalls", UNSET)
        for zone_firewalls_item_data in _zone_firewalls or []:
            zone_firewalls_item = PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItem.from_dict(
                zone_firewalls_item_data
            )

            zone_firewalls.append(zone_firewalls_item)

        zones = []
        _zones = d.pop("zones", UNSET)
        for zones_item_data in _zones or []:
            zones_item = PatchV1GlobalConfigBodyTrafficPoliciesZonesItem.from_dict(zones_item_data)

            zones.append(zones_item)

        patch_v1_global_config_body_traffic_policies = cls(
            dpi_applications=dpi_applications,
            network_lists=network_lists,
            port_lists=port_lists,
            security_rulesets=security_rulesets,
            traffic_rulesets=traffic_rulesets,
            zone_firewalls=zone_firewalls,
            zones=zones,
        )

        patch_v1_global_config_body_traffic_policies.additional_properties = d
        return patch_v1_global_config_body_traffic_policies

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
