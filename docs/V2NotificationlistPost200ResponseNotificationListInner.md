# V2NotificationlistPost200ResponseNotificationListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | **str** |  | [optional] 
**mute_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**notification_body** | [**V2NotificationCreatePostRequestNotificationBody**](V2NotificationCreatePostRequestNotificationBody.md) |  | [optional] 
**notification_id** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**times_triggered** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notificationlist_post200_response_notification_list_inner import V2NotificationlistPost200ResponseNotificationListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationlistPost200ResponseNotificationListInner from a JSON string
v2_notificationlist_post200_response_notification_list_inner_instance = V2NotificationlistPost200ResponseNotificationListInner.from_json(json)
# print the JSON string representation of the object
print(V2NotificationlistPost200ResponseNotificationListInner.to_json())

# convert the object into a dict
v2_notificationlist_post200_response_notification_list_inner_dict = v2_notificationlist_post200_response_notification_list_inner_instance.to_dict()
# create an instance of V2NotificationlistPost200ResponseNotificationListInner from a dict
v2_notificationlist_post200_response_notification_list_inner_from_dict = V2NotificationlistPost200ResponseNotificationListInner.from_dict(v2_notificationlist_post200_response_notification_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


