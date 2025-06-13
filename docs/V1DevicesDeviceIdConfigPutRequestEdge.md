# V1DevicesDeviceIdConfigPutRequestEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_enabled** | **bool** |  | [optional] 
**bgp_instance** | [**V1DevicesDeviceIdConfigPutRequestCoreBgpInstance**](V1DevicesDeviceIdConfigPutRequestCoreBgpInstance.md) |  | [optional] 
**circuits** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue]**](V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue.md) |  | [optional] 
**dhcp_server_enabled** | **bool** |  | [optional] 
**dns** | [**V1DevicesDeviceIdConfigPutRequestEdgeDns**](V1DevicesDeviceIdConfigPutRequestEdgeDns.md) |  | [optional] 
**interfaces** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValue]**](V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValue.md) |  | [optional] 
**ipfix_enabled** | **bool** |  | [optional] 
**ipfix_exporters** | [**Dict[str, V1GlobalConfigPatchRequestIpfixExportersValue]**](V1GlobalConfigPatchRequestIpfixExportersValue.md) |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**local_route_tag** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTag**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTag.md) |  | [optional] 
**local_web_server_password** | **str** |  | [optional] 
**location** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation.md) |  | [optional] 
**maintenance_mode** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**nat_policy** | [**V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy**](V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy.md) |  | [optional] 
**ospfv2_enabled** | **bool** |  | [optional] 
**ospfv3_enabled** | **bool** |  | [optional] 
**prefix_sets** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValue]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValue.md) |  | [optional] 
**region** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**route_policies** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValue.md) |  | [optional] 
**segments** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrf]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.md) |  | [optional] 
**site** | [**V1SitesPostRequestSite**](V1SitesPostRequestSite.md) |  | [optional] 
**site_to_site_vpn** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValue]**](V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValue.md) |  | [optional] 
**snmp** | [**V1GlobalConfigPatchRequestSnmpsValue**](V1GlobalConfigPatchRequestSnmpsValue.md) |  | [optional] 
**snmp_global_object** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValue]**](V1GlobalConfigPatchRequestSnmpsValue.md) |  | [optional] 
**static_routes_enabled** | **bool** |  | [optional] 
**traffic_policy** | [**V1GlobalConfigPatchRequestTrafficPolicies**](V1GlobalConfigPatchRequestTrafficPolicies.md) |  | [optional] 
**vrrp_enabled** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge import V1DevicesDeviceIdConfigPutRequestEdge

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdge from a JSON string
v1_devices_device_id_config_put_request_edge_instance = V1DevicesDeviceIdConfigPutRequestEdge.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdge.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_dict = v1_devices_device_id_config_put_request_edge_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdge from a dict
v1_devices_device_id_config_put_request_edge_from_dict = V1DevicesDeviceIdConfigPutRequestEdge.from_dict(v1_devices_device_id_config_put_request_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


