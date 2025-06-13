# V2AssistantGetConversationDetailsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** |  | [optional] 
**response_list** | [**List[V2AssistantAddToConversationPost200Response]**](V2AssistantAddToConversationPost200Response.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assistant_get_conversation_details_post200_response import V2AssistantGetConversationDetailsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssistantGetConversationDetailsPost200Response from a JSON string
v2_assistant_get_conversation_details_post200_response_instance = V2AssistantGetConversationDetailsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssistantGetConversationDetailsPost200Response.to_json())

# convert the object into a dict
v2_assistant_get_conversation_details_post200_response_dict = v2_assistant_get_conversation_details_post200_response_instance.to_dict()
# create an instance of V2AssistantGetConversationDetailsPost200Response from a dict
v2_assistant_get_conversation_details_post200_response_from_dict = V2AssistantGetConversationDetailsPost200Response.from_dict(v2_assistant_get_conversation_details_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


