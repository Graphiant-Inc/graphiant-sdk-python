# V2NotificationCreatePostRequestNotificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**frequency** | **int** |  | [optional] 
**message_body** | **str** |  | [optional] 
**notification_name** | **str** |  | [optional] 
**opsgenie_list** | **List[str]** |  | [optional] 
**opsramp_list** | **List[str]** |  | [optional] 
**recipient_list** | **List[str]** |  | [optional] 
**teams_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notification_create_post_request_notification_body import V2NotificationCreatePostRequestNotificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationCreatePostRequestNotificationBody from a JSON string
v2_notification_create_post_request_notification_body_instance = V2NotificationCreatePostRequestNotificationBody.from_json(json)
# print the JSON string representation of the object
print(V2NotificationCreatePostRequestNotificationBody.to_json())

# convert the object into a dict
v2_notification_create_post_request_notification_body_dict = v2_notification_create_post_request_notification_body_instance.to_dict()
# create an instance of V2NotificationCreatePostRequestNotificationBody from a dict
v2_notification_create_post_request_notification_body_from_dict = V2NotificationCreatePostRequestNotificationBody.from_dict(v2_notification_create_post_request_notification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


