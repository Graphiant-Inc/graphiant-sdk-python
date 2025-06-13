# V1DeviceStatusPost200ResponseMappingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**ipaddress** | **str** |  | [optional] 
**tt_identity** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_status_post200_response_mappings_inner import V1DeviceStatusPost200ResponseMappingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceStatusPost200ResponseMappingsInner from a JSON string
v1_device_status_post200_response_mappings_inner_instance = V1DeviceStatusPost200ResponseMappingsInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceStatusPost200ResponseMappingsInner.to_json())

# convert the object into a dict
v1_device_status_post200_response_mappings_inner_dict = v1_device_status_post200_response_mappings_inner_instance.to_dict()
# create an instance of V1DeviceStatusPost200ResponseMappingsInner from a dict
v1_device_status_post200_response_mappings_inner_from_dict = V1DeviceStatusPost200ResponseMappingsInner.from_dict(v1_device_status_post200_response_mappings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


