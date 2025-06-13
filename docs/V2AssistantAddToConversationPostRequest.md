# V2AssistantAddToConversationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** |  | [optional] 
**question** | [**V2AssistantAddToConversationPostRequestQuestion**](V2AssistantAddToConversationPostRequestQuestion.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_add_to_conversation_post_request import V2AssistantAddToConversationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantAddToConversationPostRequest from a JSON string
v2_assistant_add_to_conversation_post_request_instance = V2AssistantAddToConversationPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssistantAddToConversationPostRequest.to_json())

# convert the object into a dict
v2_assistant_add_to_conversation_post_request_dict = v2_assistant_add_to_conversation_post_request_instance.to_dict()
# create an instance of V2AssistantAddToConversationPostRequest from a dict
v2_assistant_add_to_conversation_post_request_from_dict = V2AssistantAddToConversationPostRequest.from_dict(v2_assistant_add_to_conversation_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


