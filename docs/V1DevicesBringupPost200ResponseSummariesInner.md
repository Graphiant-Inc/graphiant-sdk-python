# V1DevicesBringupPost200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**discovered_location** | **str** |  | [optional] 
**first_appeared_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**ip_detected** | **str** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_bringup_post200_response_summaries_inner import V1DevicesBringupPost200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesBringupPost200ResponseSummariesInner from a JSON string
v1_devices_bringup_post200_response_summaries_inner_instance = V1DevicesBringupPost200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesBringupPost200ResponseSummariesInner.to_json())

# convert the object into a dict
v1_devices_bringup_post200_response_summaries_inner_dict = v1_devices_bringup_post200_response_summaries_inner_instance.to_dict()
# create an instance of V1DevicesBringupPost200ResponseSummariesInner from a dict
v1_devices_bringup_post200_response_summaries_inner_from_dict = V1DevicesBringupPost200ResponseSummariesInner.from_dict(v1_devices_bringup_post200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


