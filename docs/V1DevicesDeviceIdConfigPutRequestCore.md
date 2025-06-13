# V1DevicesDeviceIdConfigPutRequestCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_instance** | [**V1DevicesDeviceIdConfigPutRequestCoreBgpInstance**](V1DevicesDeviceIdConfigPutRequestCoreBgpInstance.md) |  | [optional] 
**core_vrf** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrf**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.md) |  | [optional] 
**interfaces** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreInterfacesValue]**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValue.md) |  | [optional] 
**ipfix_exporters** | [**Dict[str, V1GlobalConfigPatchRequestIpfixExportersValue]**](V1GlobalConfigPatchRequestIpfixExportersValue.md) |  | [optional] 
**isp_vrfs** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrf]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.md) |  | [optional] 
**maintenance_mode** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**prefix_sets** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValue]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValue.md) |  | [optional] 
**prometheus** | [**V1DevicesDeviceIdConfigPutRequestCorePrometheus**](V1DevicesDeviceIdConfigPutRequestCorePrometheus.md) |  | [optional] 
**region** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**route_policies** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValue.md) |  | [optional] 
**site** | [**V1SitesPostRequestSite**](V1SitesPostRequestSite.md) |  | [optional] 
**traffic_policy** | [**V1GlobalConfigPatchRequestTrafficPolicies**](V1GlobalConfigPatchRequestTrafficPolicies.md) |  | [optional] 
**vrfs** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrf]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrf.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core import V1DevicesDeviceIdConfigPutRequestCore

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCore from a JSON string
v1_devices_device_id_config_put_request_core_instance = V1DevicesDeviceIdConfigPutRequestCore.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCore.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_dict = v1_devices_device_id_config_put_request_core_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCore from a dict
v1_devices_device_id_config_put_request_core_from_dict = V1DevicesDeviceIdConfigPutRequestCore.from_dict(v1_devices_device_id_config_put_request_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


