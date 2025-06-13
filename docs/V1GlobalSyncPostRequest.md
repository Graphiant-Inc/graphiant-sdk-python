# V1GlobalSyncPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **List[int]** |  | [optional] 
**ipfix_exported_id** | **int** |  | [optional] 
**prefix_set_id** | **int** |  | [optional] 
**routing_policy_id** | **int** |  | [optional] 
**snmp_id** | **int** |  | [optional] 
**syslog_server_id** | **int** |  | [optional] 
**traffic_policy_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_sync_post_request import V1GlobalSyncPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalSyncPostRequest from a JSON string
v1_global_sync_post_request_instance = V1GlobalSyncPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalSyncPostRequest.to_json())

# convert the object into a dict
v1_global_sync_post_request_dict = v1_global_sync_post_request_instance.to_dict()
# create an instance of V1GlobalSyncPostRequest from a dict
v1_global_sync_post_request_from_dict = V1GlobalSyncPostRequest.from_dict(v1_global_sync_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


