# V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_status** | **str** |  | [optional] 
**location** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner import V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner from a JSON string
v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner_instance = V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner_dict = v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner from a dict
v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner_from_dict = V1ExtranetsB2bConsumerDeviceStatusIdGet200ResponseSummaryInner.from_dict(v1_extranets_b2b_consumer_device_status_id_get200_response_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


