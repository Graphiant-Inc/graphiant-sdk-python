# V1FlowsTopologyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_selector** | [**V1FlowsTopologyPostRequestAppSelector**](V1FlowsTopologyPostRequestAppSelector.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post_request import V1FlowsTopologyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPostRequest from a JSON string
v1_flows_topology_post_request_instance = V1FlowsTopologyPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPostRequest.to_json())

# convert the object into a dict
v1_flows_topology_post_request_dict = v1_flows_topology_post_request_instance.to_dict()
# create an instance of V1FlowsTopologyPostRequest from a dict
v1_flows_topology_post_request_from_dict = V1FlowsTopologyPostRequest.from_dict(v1_flows_topology_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


