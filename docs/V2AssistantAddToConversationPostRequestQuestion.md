# V2AssistantAddToConversationPostRequestQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** |  | [optional] 
**question_language** | **str** |  | [optional] 
**question_text** | **str** |  | [optional] 
**question_timestamp** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_add_to_conversation_post_request_question import V2AssistantAddToConversationPostRequestQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantAddToConversationPostRequestQuestion from a JSON string
v2_assistant_add_to_conversation_post_request_question_instance = V2AssistantAddToConversationPostRequestQuestion.from_json(json)
# print the JSON string representation of the object
print(V2AssistantAddToConversationPostRequestQuestion.to_json())

# convert the object into a dict
v2_assistant_add_to_conversation_post_request_question_dict = v2_assistant_add_to_conversation_post_request_question_instance.to_dict()
# create an instance of V2AssistantAddToConversationPostRequestQuestion from a dict
v2_assistant_add_to_conversation_post_request_question_from_dict = V2AssistantAddToConversationPostRequestQuestion.from_dict(v2_assistant_add_to_conversation_post_request_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


