# V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_server_key** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**lan_segments** | **List[str]** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**server_site_name** | **str** |  | [optional] 
**session_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_summaries_post200_response_summaries_inner import V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner from a JSON string
v2_assurance_topology_client_summaries_post200_response_summaries_inner_instance = V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner.to_json())

# convert the object into a dict
v2_assurance_topology_client_summaries_post200_response_summaries_inner_dict = v2_assurance_topology_client_summaries_post200_response_summaries_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner from a dict
v2_assurance_topology_client_summaries_post200_response_summaries_inner_from_dict = V2AssuranceTopologyClientSummariesPost200ResponseSummariesInner.from_dict(v2_assurance_topology_client_summaries_post200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


