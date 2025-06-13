# V1GlobalAttachedEdgesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipfix_exported_ids** | **List[int]** |  | [optional] 
**prefix_set_ids** | **List[int]** |  | [optional] 
**routing_policy_ids** | **List[int]** |  | [optional] 
**snmp_ids** | **List[int]** |  | [optional] 
**syslog_server_ids** | **List[int]** |  | [optional] 
**traffic_policy_ids** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_attached_edges_post_request import V1GlobalAttachedEdgesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAttachedEdgesPostRequest from a JSON string
v1_global_attached_edges_post_request_instance = V1GlobalAttachedEdgesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAttachedEdgesPostRequest.to_json())

# convert the object into a dict
v1_global_attached_edges_post_request_dict = v1_global_attached_edges_post_request_instance.to_dict()
# create an instance of V1GlobalAttachedEdgesPostRequest from a dict
v1_global_attached_edges_post_request_from_dict = V1GlobalAttachedEdgesPostRequest.from_dict(v1_global_attached_edges_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


