# V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**lan_segments** | **List[str]** |  | [optional] 
**session_count** | **int** |  | [optional] 
**site** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointSite**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_site_summaries_post200_response_summaries_inner import V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner from a JSON string
v2_assurance_topology_site_summaries_post200_response_summaries_inner_instance = V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner.to_json())

# convert the object into a dict
v2_assurance_topology_site_summaries_post200_response_summaries_inner_dict = v2_assurance_topology_site_summaries_post200_response_summaries_inner_instance.to_dict()
# create an instance of V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner from a dict
v2_assurance_topology_site_summaries_post200_response_summaries_inner_from_dict = V2AssuranceTopologySiteSummariesPost200ResponseSummariesInner.from_dict(v2_assurance_topology_site_summaries_post200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


