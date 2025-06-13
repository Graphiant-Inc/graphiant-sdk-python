# V2NotificationlistPostRequestTimeWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_size_sec** | **int** |  | [optional] 
**old_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**recent_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notificationlist_post_request_time_window import V2NotificationlistPostRequestTimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationlistPostRequestTimeWindow from a JSON string
v2_notificationlist_post_request_time_window_instance = V2NotificationlistPostRequestTimeWindow.from_json(json)
# print the JSON string representation of the object
print(V2NotificationlistPostRequestTimeWindow.to_json())

# convert the object into a dict
v2_notificationlist_post_request_time_window_dict = v2_notificationlist_post_request_time_window_instance.to_dict()
# create an instance of V2NotificationlistPostRequestTimeWindow from a dict
v2_notificationlist_post_request_time_window_from_dict = V2NotificationlistPostRequestTimeWindow.from_dict(v2_notificationlist_post_request_time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


