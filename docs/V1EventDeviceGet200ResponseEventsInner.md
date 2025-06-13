# V1EventDeviceGet200ResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** |  | [optional] 
**device_id** | **int** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**event_data** | **str** |  | [optional] 
**event_id** | **int** |  | [optional] 
**event_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_event_device_get200_response_events_inner import V1EventDeviceGet200ResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventDeviceGet200ResponseEventsInner from a JSON string
v1_event_device_get200_response_events_inner_instance = V1EventDeviceGet200ResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(V1EventDeviceGet200ResponseEventsInner.to_json())

# convert the object into a dict
v1_event_device_get200_response_events_inner_dict = v1_event_device_get200_response_events_inner_instance.to_dict()
# create an instance of V1EventDeviceGet200ResponseEventsInner from a dict
v1_event_device_get200_response_events_inner_from_dict = V1EventDeviceGet200ResponseEventsInner.from_dict(v1_event_device_get200_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


