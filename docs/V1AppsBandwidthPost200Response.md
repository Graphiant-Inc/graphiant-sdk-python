# V1AppsBandwidthPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**List[V1AppsBandwidthPost200ResponseStatsInner]**](V1AppsBandwidthPost200ResponseStatsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_bandwidth_post200_response import V1AppsBandwidthPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsBandwidthPost200Response from a JSON string
v1_apps_bandwidth_post200_response_instance = V1AppsBandwidthPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1AppsBandwidthPost200Response.to_json())

# convert the object into a dict
v1_apps_bandwidth_post200_response_dict = v1_apps_bandwidth_post200_response_instance.to_dict()
# create an instance of V1AppsBandwidthPost200Response from a dict
v1_apps_bandwidth_post200_response_from_dict = V1AppsBandwidthPost200Response.from_dict(v1_apps_bandwidth_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


