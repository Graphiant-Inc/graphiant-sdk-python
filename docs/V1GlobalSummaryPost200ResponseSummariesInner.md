# V1GlobalSummaryPost200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_point** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ip_version** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**num_attached_devices** | **int** |  | [optional] 
**num_attached_sites** | **int** |  | [optional] 
**num_failures** | **int** |  | [optional] 
**num_in_sync_devices** | **int** |  | [optional] 
**num_override_devices** | **int** |  | [optional] 
**num_policies** | **int** |  | [optional] 
**num_prefixes** | **int** |  | [optional] 
**num_rules** | **int** |  | [optional] 
**num_statements** | **int** |  | [optional] 
**traffic_policy_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_summary_post200_response_summaries_inner import V1GlobalSummaryPost200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalSummaryPost200ResponseSummariesInner from a JSON string
v1_global_summary_post200_response_summaries_inner_instance = V1GlobalSummaryPost200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalSummaryPost200ResponseSummariesInner.to_json())

# convert the object into a dict
v1_global_summary_post200_response_summaries_inner_dict = v1_global_summary_post200_response_summaries_inner_instance.to_dict()
# create an instance of V1GlobalSummaryPost200ResponseSummariesInner from a dict
v1_global_summary_post200_response_summaries_inner_from_dict = V1GlobalSummaryPost200ResponseSummariesInner.from_dict(v1_global_summary_post200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


