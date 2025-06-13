# V2NotificationUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_body** | [**V2NotificationCreatePostRequestNotificationBody**](V2NotificationCreatePostRequestNotificationBody.md) |  | [optional] 
**notification_id_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notification_update_post_request import V2NotificationUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationUpdatePostRequest from a JSON string
v2_notification_update_post_request_instance = V2NotificationUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2NotificationUpdatePostRequest.to_json())

# convert the object into a dict
v2_notification_update_post_request_dict = v2_notification_update_post_request_instance.to_dict()
# create an instance of V2NotificationUpdatePostRequest from a dict
v2_notification_update_post_request_from_dict = V2NotificationUpdatePostRequest.from_dict(v2_notification_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


