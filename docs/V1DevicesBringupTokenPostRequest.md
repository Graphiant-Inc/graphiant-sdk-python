# V1DevicesBringupTokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**valid_till_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**validity_sec** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_bringup_token_post_request import V1DevicesBringupTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesBringupTokenPostRequest from a JSON string
v1_devices_bringup_token_post_request_instance = V1DevicesBringupTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesBringupTokenPostRequest.to_json())

# convert the object into a dict
v1_devices_bringup_token_post_request_dict = v1_devices_bringup_token_post_request_instance.to_dict()
# create an instance of V1DevicesBringupTokenPostRequest from a dict
v1_devices_bringup_token_post_request_from_dict = V1DevicesBringupTokenPostRequest.from_dict(v1_devices_bringup_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


