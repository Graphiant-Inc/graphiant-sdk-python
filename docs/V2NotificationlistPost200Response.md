# V2NotificationlistPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_list** | [**List[V2NotificationlistPost200ResponseNotificationListInner]**](V2NotificationlistPost200ResponseNotificationListInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notificationlist_post200_response import V2NotificationlistPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationlistPost200Response from a JSON string
v2_notificationlist_post200_response_instance = V2NotificationlistPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2NotificationlistPost200Response.to_json())

# convert the object into a dict
v2_notificationlist_post200_response_dict = v2_notificationlist_post200_response_instance.to_dict()
# create an instance of V2NotificationlistPost200Response from a dict
v2_notificationlist_post200_response_from_dict = V2NotificationlistPost200Response.from_dict(v2_notificationlist_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


