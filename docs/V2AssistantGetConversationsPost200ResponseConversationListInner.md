# V2AssistantGetConversationsPost200ResponseConversationListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_header** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 
**conversation_recent_timestamp** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_get_conversations_post200_response_conversation_list_inner import V2AssistantGetConversationsPost200ResponseConversationListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantGetConversationsPost200ResponseConversationListInner from a JSON string
v2_assistant_get_conversations_post200_response_conversation_list_inner_instance = V2AssistantGetConversationsPost200ResponseConversationListInner.from_json(json)
# print the JSON string representation of the object
print(V2AssistantGetConversationsPost200ResponseConversationListInner.to_json())

# convert the object into a dict
v2_assistant_get_conversations_post200_response_conversation_list_inner_dict = v2_assistant_get_conversations_post200_response_conversation_list_inner_instance.to_dict()
# create an instance of V2AssistantGetConversationsPost200ResponseConversationListInner from a dict
v2_assistant_get_conversations_post200_response_conversation_list_inner_from_dict = V2AssistantGetConversationsPost200ResponseConversationListInner.from_dict(v2_assistant_get_conversations_post200_response_conversation_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


