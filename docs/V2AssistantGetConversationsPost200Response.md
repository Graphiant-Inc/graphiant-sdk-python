# V2AssistantGetConversationsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_list** | [**List[V2AssistantGetConversationsPost200ResponseConversationListInner]**](V2AssistantGetConversationsPost200ResponseConversationListInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_get_conversations_post200_response import V2AssistantGetConversationsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantGetConversationsPost200Response from a JSON string
v2_assistant_get_conversations_post200_response_instance = V2AssistantGetConversationsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssistantGetConversationsPost200Response.to_json())

# convert the object into a dict
v2_assistant_get_conversations_post200_response_dict = v2_assistant_get_conversations_post200_response_instance.to_dict()
# create an instance of V2AssistantGetConversationsPost200Response from a dict
v2_assistant_get_conversations_post200_response_from_dict = V2AssistantGetConversationsPost200Response.from_dict(v2_assistant_get_conversations_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


