# V2NotificationlistPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_notificationlist_post_request import V2NotificationlistPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2NotificationlistPostRequest from a JSON string
v2_notificationlist_post_request_instance = V2NotificationlistPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2NotificationlistPostRequest.to_json())

# convert the object into a dict
v2_notificationlist_post_request_dict = v2_notificationlist_post_request_instance.to_dict()
# create an instance of V2NotificationlistPostRequest from a dict
v2_notificationlist_post_request_from_dict = V2NotificationlistPostRequest.from_dict(v2_notificationlist_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


