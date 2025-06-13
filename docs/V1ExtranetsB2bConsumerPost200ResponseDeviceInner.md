# V1ExtranetsB2bConsumerPost200ResponseDeviceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**last_updated** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**site** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post200_response_device_inner import V1ExtranetsB2bConsumerPost200ResponseDeviceInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPost200ResponseDeviceInner from a JSON string
v1_extranets_b2b_consumer_post200_response_device_inner_instance = V1ExtranetsB2bConsumerPost200ResponseDeviceInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPost200ResponseDeviceInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post200_response_device_inner_dict = v1_extranets_b2b_consumer_post200_response_device_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPost200ResponseDeviceInner from a dict
v1_extranets_b2b_consumer_post200_response_device_inner_from_dict = V1ExtranetsB2bConsumerPost200ResponseDeviceInner.from_dict(v1_extranets_b2b_consumer_post200_response_device_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


