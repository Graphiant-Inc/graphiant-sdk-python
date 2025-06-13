# V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b2b_status** | **str** |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**id** | **int** |  | [optional] 
**num_edges** | **int** |  | [optional] 
**num_segments** | **int** |  | [optional] 
**num_sites** | **int** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**publisher_name** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_summary_get200_response_summary_inner import V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner from a JSON string
v1_extranets_b2b_consumer_summary_get200_response_summary_inner_instance = V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_summary_get200_response_summary_inner_dict = v1_extranets_b2b_consumer_summary_get200_response_summary_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner from a dict
v1_extranets_b2b_consumer_summary_get200_response_summary_inner_from_dict = V1ExtranetsB2bConsumerSummaryGet200ResponseSummaryInner.from_dict(v1_extranets_b2b_consumer_summary_get200_response_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


