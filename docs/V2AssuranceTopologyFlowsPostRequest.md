# V2AssuranceTopologyFlowsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 
**topology_id** | **int** |  | [optional] 
**topology_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_flows_post_request import V2AssuranceTopologyFlowsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyFlowsPostRequest from a JSON string
v2_assurance_topology_flows_post_request_instance = V2AssuranceTopologyFlowsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyFlowsPostRequest.to_json())

# convert the object into a dict
v2_assurance_topology_flows_post_request_dict = v2_assurance_topology_flows_post_request_instance.to_dict()
# create an instance of V2AssuranceTopologyFlowsPostRequest from a dict
v2_assurance_topology_flows_post_request_from_dict = V2AssuranceTopologyFlowsPostRequest.from_dict(v2_assurance_topology_flows_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


