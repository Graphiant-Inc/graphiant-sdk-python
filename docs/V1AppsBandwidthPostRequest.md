# V1AppsBandwidthPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**dl_circuit_name** | **str** |  | [optional] 
**is_dia** | **bool** |  | [optional] 
**sla_class** | **str** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 
**ul_circuit_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_bandwidth_post_request import V1AppsBandwidthPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsBandwidthPostRequest from a JSON string
v1_apps_bandwidth_post_request_instance = V1AppsBandwidthPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AppsBandwidthPostRequest.to_json())

# convert the object into a dict
v1_apps_bandwidth_post_request_dict = v1_apps_bandwidth_post_request_instance.to_dict()
# create an instance of V1AppsBandwidthPostRequest from a dict
v1_apps_bandwidth_post_request_from_dict = V1AppsBandwidthPostRequest.from_dict(v1_apps_bandwidth_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


