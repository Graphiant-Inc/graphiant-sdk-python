# V1AlarmsListGet200ResponseAlarmsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged_by** | **str** |  | [optional] 
**alarm_id** | **int** |  | [optional] 
**alarm_type_id** | **str** |  | [optional] 
**alarm_type_qualifier** | **str** |  | [optional] 
**alt_component** | **str** |  | [optional] 
**boot_id** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**created** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**description** | **str** |  | [optional] 
**is_cleared** | **bool** |  | [optional] 
**is_resolved** | **bool** |  | [optional] 
**last_changed** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**last_raised** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**perceived_severity** | **str** |  | [optional] 
**resolved_by** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**where** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_alarms_list_get200_response_alarms_inner import V1AlarmsListGet200ResponseAlarmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AlarmsListGet200ResponseAlarmsInner from a JSON string
v1_alarms_list_get200_response_alarms_inner_instance = V1AlarmsListGet200ResponseAlarmsInner.from_json(json)
# print the JSON string representation of the object
print(V1AlarmsListGet200ResponseAlarmsInner.to_json())

# convert the object into a dict
v1_alarms_list_get200_response_alarms_inner_dict = v1_alarms_list_get200_response_alarms_inner_instance.to_dict()
# create an instance of V1AlarmsListGet200ResponseAlarmsInner from a dict
v1_alarms_list_get200_response_alarms_inner_from_dict = V1AlarmsListGet200ResponseAlarmsInner.from_dict(v1_alarms_list_get200_response_alarms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


