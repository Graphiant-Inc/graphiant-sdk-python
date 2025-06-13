# V1GlobalConfigPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_prefix_sets** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValue]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValue.md) |  | [optional] 
**ipfix_exporters** | [**Dict[str, V1GlobalConfigPatchRequestIpfixExportersValue]**](V1GlobalConfigPatchRequestIpfixExportersValue.md) |  | [optional] 
**prefix_sets** | [**Dict[str, V1GlobalConfigPatchRequestPrefixSetsValue]**](V1GlobalConfigPatchRequestPrefixSetsValue.md) |  | [optional] 
**routing_policies** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValue.md) |  | [optional] 
**snmps** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValue]**](V1GlobalConfigPatchRequestSnmpsValue.md) |  | [optional] 
**syslog_servers** | [**Dict[str, V1GlobalConfigPatchRequestSyslogServersValue]**](V1GlobalConfigPatchRequestSyslogServersValue.md) |  | [optional] 
**traffic_policies** | [**V1GlobalConfigPatchRequestTrafficPolicies**](V1GlobalConfigPatchRequestTrafficPolicies.md) |  | [optional] 
**vpn_profiles** | [**Dict[str, V1GlobalConfigPatchRequestVpnProfilesValue]**](V1GlobalConfigPatchRequestVpnProfilesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request import V1GlobalConfigPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequest from a JSON string
v1_global_config_patch_request_instance = V1GlobalConfigPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequest.to_json())

# convert the object into a dict
v1_global_config_patch_request_dict = v1_global_config_patch_request_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequest from a dict
v1_global_config_patch_request_from_dict = V1GlobalConfigPatchRequest.from_dict(v1_global_config_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


