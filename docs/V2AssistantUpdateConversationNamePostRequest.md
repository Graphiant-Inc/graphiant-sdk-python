# V2AssistantUpdateConversationNamePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_header** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_update_conversation_name_post_request import V2AssistantUpdateConversationNamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantUpdateConversationNamePostRequest from a JSON string
v2_assistant_update_conversation_name_post_request_instance = V2AssistantUpdateConversationNamePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssistantUpdateConversationNamePostRequest.to_json())

# convert the object into a dict
v2_assistant_update_conversation_name_post_request_dict = v2_assistant_update_conversation_name_post_request_instance.to_dict()
# create an instance of V2AssistantUpdateConversationNamePostRequest from a dict
v2_assistant_update_conversation_name_post_request_from_dict = V2AssistantUpdateConversationNamePostRequest.from_dict(v2_assistant_update_conversation_name_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


