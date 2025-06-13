# V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 
**auto_ipv4** | **bool** |  | [optional] 
**auto_ipv6** | **bool** |  | [optional] 
**interface** | **str** |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint import V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint from a JSON string
v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_instance = V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint.to_json())

# convert the object into a dict
v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_dict = v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint from a dict
v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_from_dict = V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpoint.from_dict(v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


