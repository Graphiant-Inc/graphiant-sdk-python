# V1GlobalConfigPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_prefix_sets** | **Dict[str, int]** |  | [optional] 
**ipfix_exporters** | **Dict[str, int]** |  | [optional] 
**prefix_sets** | **Dict[str, int]** |  | [optional] 
**routing_policies** | **Dict[str, int]** |  | [optional] 
**snmps** | **Dict[str, int]** |  | [optional] 
**status** | **str** |  | [optional] 
**syslog_servers** | **Dict[str, int]** |  | [optional] 
**traffic_policies** | **Dict[str, int]** |  | [optional] 
**vpn_profiles** | **Dict[str, int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch200_response import V1GlobalConfigPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatch200Response from a JSON string
v1_global_config_patch200_response_instance = V1GlobalConfigPatch200Response.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatch200Response.to_json())

# convert the object into a dict
v1_global_config_patch200_response_dict = v1_global_config_patch200_response_instance.to_dict()
# create an instance of V1GlobalConfigPatch200Response from a dict
v1_global_config_patch200_response_from_dict = V1GlobalConfigPatch200Response.from_dict(v1_global_config_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


