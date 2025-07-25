# coding: utf-8

"""
    Graphiant APIs

    Graphiant API documentation.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_bgp_aggregations_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_bgp_redistribution_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValue
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_ebgp_multipath import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_nat_ruleset import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_ospfv2 import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue
from graphiant_sdk.models.v1_global_config_patch_request_ipfix_exporters_value import V1GlobalConfigPatchRequestIpfixExportersValue
from graphiant_sdk.models.v1_global_config_patch_request_syslog_servers_value import V1GlobalConfigPatchRequestSyslogServersValue
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdConfigPutRequestCoreCoreVrf(BaseModel):
    """
    V1DevicesDeviceIdConfigPutRequestCoreCoreVrf
    """ # noqa: E501
    bgp_aggregations: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue]] = Field(default=None, alias="bgpAggregations")
    bgp_neighbors: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue]] = Field(default=None, alias="bgpNeighbors")
    bgp_redistribution: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue]] = Field(default=None, alias="bgpRedistribution")
    dhcp_subnets: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValue]] = Field(default=None, alias="dhcpSubnets")
    ebgp_multipath: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath] = Field(default=None, alias="ebgpMultipath")
    ipfix_exporters: Optional[Dict[str, V1GlobalConfigPatchRequestIpfixExportersValue]] = Field(default=None, alias="ipfixExporters")
    nat_ruleset: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset] = Field(default=None, alias="natRuleset")
    networks: Optional[List[StrictStr]] = None
    ospfv2: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2] = None
    ospfv3: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2] = None
    overlay_filters: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters] = Field(default=None, alias="overlayFilters")
    static_routes: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue]] = Field(default=None, alias="staticRoutes")
    syslog_targets: Optional[Dict[str, V1GlobalConfigPatchRequestSyslogServersValue]] = Field(default=None, alias="syslogTargets")
    traffic_ruleset: Optional[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset] = Field(default=None, alias="trafficRuleset")
    __properties: ClassVar[List[str]] = ["bgpAggregations", "bgpNeighbors", "bgpRedistribution", "dhcpSubnets", "ebgpMultipath", "ipfixExporters", "natRuleset", "networks", "ospfv2", "ospfv3", "overlayFilters", "staticRoutes", "syslogTargets", "trafficRuleset"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in bgp_aggregations (dict)
        _field_dict = {}
        if self.bgp_aggregations:
            for _key_bgp_aggregations in self.bgp_aggregations:
                if self.bgp_aggregations[_key_bgp_aggregations]:
                    _field_dict[_key_bgp_aggregations] = self.bgp_aggregations[_key_bgp_aggregations].to_dict()
            _dict['bgpAggregations'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bgp_neighbors (dict)
        _field_dict = {}
        if self.bgp_neighbors:
            for _key_bgp_neighbors in self.bgp_neighbors:
                if self.bgp_neighbors[_key_bgp_neighbors]:
                    _field_dict[_key_bgp_neighbors] = self.bgp_neighbors[_key_bgp_neighbors].to_dict()
            _dict['bgpNeighbors'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bgp_redistribution (dict)
        _field_dict = {}
        if self.bgp_redistribution:
            for _key_bgp_redistribution in self.bgp_redistribution:
                if self.bgp_redistribution[_key_bgp_redistribution]:
                    _field_dict[_key_bgp_redistribution] = self.bgp_redistribution[_key_bgp_redistribution].to_dict()
            _dict['bgpRedistribution'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in dhcp_subnets (dict)
        _field_dict = {}
        if self.dhcp_subnets:
            for _key_dhcp_subnets in self.dhcp_subnets:
                if self.dhcp_subnets[_key_dhcp_subnets]:
                    _field_dict[_key_dhcp_subnets] = self.dhcp_subnets[_key_dhcp_subnets].to_dict()
            _dict['dhcpSubnets'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of ebgp_multipath
        if self.ebgp_multipath:
            _dict['ebgpMultipath'] = self.ebgp_multipath.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in ipfix_exporters (dict)
        _field_dict = {}
        if self.ipfix_exporters:
            for _key_ipfix_exporters in self.ipfix_exporters:
                if self.ipfix_exporters[_key_ipfix_exporters]:
                    _field_dict[_key_ipfix_exporters] = self.ipfix_exporters[_key_ipfix_exporters].to_dict()
            _dict['ipfixExporters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of nat_ruleset
        if self.nat_ruleset:
            _dict['natRuleset'] = self.nat_ruleset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ospfv2
        if self.ospfv2:
            _dict['ospfv2'] = self.ospfv2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ospfv3
        if self.ospfv3:
            _dict['ospfv3'] = self.ospfv3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overlay_filters
        if self.overlay_filters:
            _dict['overlayFilters'] = self.overlay_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in static_routes (dict)
        _field_dict = {}
        if self.static_routes:
            for _key_static_routes in self.static_routes:
                if self.static_routes[_key_static_routes]:
                    _field_dict[_key_static_routes] = self.static_routes[_key_static_routes].to_dict()
            _dict['staticRoutes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in syslog_targets (dict)
        _field_dict = {}
        if self.syslog_targets:
            for _key_syslog_targets in self.syslog_targets:
                if self.syslog_targets[_key_syslog_targets]:
                    _field_dict[_key_syslog_targets] = self.syslog_targets[_key_syslog_targets].to_dict()
            _dict['syslogTargets'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of traffic_ruleset
        if self.traffic_ruleset:
            _dict['trafficRuleset'] = self.traffic_ruleset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bgpAggregations": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue.from_dict(_v))
                for _k, _v in obj["bgpAggregations"].items()
            )
            if obj.get("bgpAggregations") is not None
            else None,
            "bgpNeighbors": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue.from_dict(_v))
                for _k, _v in obj["bgpNeighbors"].items()
            )
            if obj.get("bgpNeighbors") is not None
            else None,
            "bgpRedistribution": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue.from_dict(_v))
                for _k, _v in obj["bgpRedistribution"].items()
            )
            if obj.get("bgpRedistribution") is not None
            else None,
            "dhcpSubnets": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValue.from_dict(_v))
                for _k, _v in obj["dhcpSubnets"].items()
            )
            if obj.get("dhcpSubnets") is not None
            else None,
            "ebgpMultipath": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath.from_dict(obj["ebgpMultipath"]) if obj.get("ebgpMultipath") is not None else None,
            "ipfixExporters": dict(
                (_k, V1GlobalConfigPatchRequestIpfixExportersValue.from_dict(_v))
                for _k, _v in obj["ipfixExporters"].items()
            )
            if obj.get("ipfixExporters") is not None
            else None,
            "natRuleset": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset.from_dict(obj["natRuleset"]) if obj.get("natRuleset") is not None else None,
            "networks": obj.get("networks"),
            "ospfv2": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2.from_dict(obj["ospfv2"]) if obj.get("ospfv2") is not None else None,
            "ospfv3": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2.from_dict(obj["ospfv3"]) if obj.get("ospfv3") is not None else None,
            "overlayFilters": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters.from_dict(obj["overlayFilters"]) if obj.get("overlayFilters") is not None else None,
            "staticRoutes": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue.from_dict(_v))
                for _k, _v in obj["staticRoutes"].items()
            )
            if obj.get("staticRoutes") is not None
            else None,
            "syslogTargets": dict(
                (_k, V1GlobalConfigPatchRequestSyslogServersValue.from_dict(_v))
                for _k, _v in obj["syslogTargets"].items()
            )
            if obj.get("syslogTargets") is not None
            else None,
            "trafficRuleset": V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset.from_dict(obj["trafficRuleset"]) if obj.get("trafficRuleset") is not None else None
        })
        return _obj


