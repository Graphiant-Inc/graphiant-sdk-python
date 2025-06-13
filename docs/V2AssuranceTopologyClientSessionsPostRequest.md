# V2AssuranceTopologyClientSessionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**app_server_key** | **str** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**filter** | [**V2AssuranceTopologyClientSessionsPostRequestFilter**](V2AssuranceTopologyClientSessionsPostRequestFilter.md) |  | [optional] 
**flex_algo_id** | **int** |  | [optional] 
**site_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_sessions_post_request import V2AssuranceTopologyClientSessionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionsPostRequest from a JSON string
v2_assurance_topology_client_sessions_post_request_instance = V2AssuranceTopologyClientSessionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionsPostRequest.to_json())

# convert the object into a dict
v2_assurance_topology_client_sessions_post_request_dict = v2_assurance_topology_client_sessions_post_request_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionsPostRequest from a dict
v2_assurance_topology_client_sessions_post_request_from_dict = V2AssuranceTopologyClientSessionsPostRequest.from_dict(v2_assurance_topology_client_sessions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


