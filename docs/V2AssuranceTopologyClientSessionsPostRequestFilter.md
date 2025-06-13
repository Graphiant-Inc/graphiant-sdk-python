# V2AssuranceTopologyClientSessionsPostRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_site_ids** | **List[int]** |  | [optional] 
**region_ids** | **List[int]** |  | [optional] 
**server_site_ids** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_sessions_post_request_filter import V2AssuranceTopologyClientSessionsPostRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionsPostRequestFilter from a JSON string
v2_assurance_topology_client_sessions_post_request_filter_instance = V2AssuranceTopologyClientSessionsPostRequestFilter.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionsPostRequestFilter.to_json())

# convert the object into a dict
v2_assurance_topology_client_sessions_post_request_filter_dict = v2_assurance_topology_client_sessions_post_request_filter_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionsPostRequestFilter from a dict
v2_assurance_topology_client_sessions_post_request_filter_from_dict = V2AssuranceTopologyClientSessionsPostRequestFilter.from_dict(v2_assurance_topology_client_sessions_post_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


