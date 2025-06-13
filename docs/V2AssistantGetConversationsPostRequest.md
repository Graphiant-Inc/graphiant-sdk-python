# V2AssistantGetConversationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_get_conversations_post_request import V2AssistantGetConversationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantGetConversationsPostRequest from a JSON string
v2_assistant_get_conversations_post_request_instance = V2AssistantGetConversationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssistantGetConversationsPostRequest.to_json())

# convert the object into a dict
v2_assistant_get_conversations_post_request_dict = v2_assistant_get_conversations_post_request_instance.to_dict()
# create an instance of V2AssistantGetConversationsPostRequest from a dict
v2_assistant_get_conversations_post_request_from_dict = V2AssistantGetConversationsPostRequest.from_dict(v2_assistant_get_conversations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


