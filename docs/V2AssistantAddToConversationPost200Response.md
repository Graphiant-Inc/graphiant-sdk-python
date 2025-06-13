# V2AssistantAddToConversationPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** |  | [optional] 
**dataframe_dictionary** | [**List[V2AssistantAddToConversationPost200ResponseDataframeDictionaryInner]**](V2AssistantAddToConversationPost200ResponseDataframeDictionaryInner.md) |  | [optional] 
**original_question** | [**V2AssistantAddToConversationPostRequestQuestion**](V2AssistantAddToConversationPostRequestQuestion.md) |  | [optional] 
**response_id** | **str** |  | [optional] 
**response_language** | **str** |  | [optional] 
**response_text** | **str** |  | [optional] 
**response_timestamp** | **int** |  | [optional] 
**response_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_add_to_conversation_post200_response import V2AssistantAddToConversationPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantAddToConversationPost200Response from a JSON string
v2_assistant_add_to_conversation_post200_response_instance = V2AssistantAddToConversationPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssistantAddToConversationPost200Response.to_json())

# convert the object into a dict
v2_assistant_add_to_conversation_post200_response_dict = v2_assistant_add_to_conversation_post200_response_instance.to_dict()
# create an instance of V2AssistantAddToConversationPost200Response from a dict
v2_assistant_add_to_conversation_post200_response_from_dict = V2AssistantAddToConversationPost200Response.from_dict(v2_assistant_add_to_conversation_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


