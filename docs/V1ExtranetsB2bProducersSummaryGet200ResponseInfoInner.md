# V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**server_ip_address** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**total_customers** | **int** |  | [optional] 
**total_sites** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_producers_summary_get200_response_info_inner import V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner from a JSON string
v1_extranets_b2b_producers_summary_get200_response_info_inner_instance = V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner.to_json())

# convert the object into a dict
v1_extranets_b2b_producers_summary_get200_response_info_inner_dict = v1_extranets_b2b_producers_summary_get200_response_info_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner from a dict
v1_extranets_b2b_producers_summary_get200_response_info_inner_from_dict = V1ExtranetsB2bProducersSummaryGet200ResponseInfoInner.from_dict(v1_extranets_b2b_producers_summary_get200_response_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


