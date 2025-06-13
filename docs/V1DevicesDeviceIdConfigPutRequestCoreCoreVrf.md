# V1DevicesDeviceIdConfigPutRequestCoreCoreVrf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_aggregations** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue.md) |  | [optional] 
**bgp_neighbors** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue.md) |  | [optional] 
**bgp_redistribution** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue.md) |  | [optional] 
**dhcp_subnets** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValue.md) |  | [optional] 
**ebgp_multipath** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath.md) |  | [optional] 
**ipfix_exporters** | [**Dict[str, V1GlobalConfigPatchRequestIpfixExportersValue]**](V1GlobalConfigPatchRequestIpfixExportersValue.md) |  | [optional] 
**nat_ruleset** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset.md) |  | [optional] 
**networks** | **List[str]** |  | [optional] 
**ospfv2** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2.md) |  | [optional] 
**ospfv3** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2.md) |  | [optional] 
**overlay_filters** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters.md) |  | [optional] 
**static_routes** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue.md) |  | [optional] 
**syslog_targets** | [**Dict[str, V1GlobalConfigPatchRequestSyslogServersValue]**](V1GlobalConfigPatchRequestSyslogServersValue.md) |  | [optional] 
**traffic_ruleset** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfNatRuleset.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf import V1DevicesDeviceIdConfigPutRequestCoreCoreVrf

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrf from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_dict = v1_devices_device_id_config_put_request_core_core_vrf_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrf from a dict
v1_devices_device_id_config_put_request_core_core_vrf_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


