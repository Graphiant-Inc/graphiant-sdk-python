# V2AssuranceCategorizeAiAppPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **List[str]** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**is_ai_app** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_categorize_ai_app_post_request import V2AssuranceCategorizeAiAppPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceCategorizeAiAppPostRequest from a JSON string
v2_assurance_categorize_ai_app_post_request_instance = V2AssuranceCategorizeAiAppPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceCategorizeAiAppPostRequest.to_json())

# convert the object into a dict
v2_assurance_categorize_ai_app_post_request_dict = v2_assurance_categorize_ai_app_post_request_instance.to_dict()
# create an instance of V2AssuranceCategorizeAiAppPostRequest from a dict
v2_assurance_categorize_ai_app_post_request_from_dict = V2AssuranceCategorizeAiAppPostRequest.from_dict(v2_assurance_categorize_ai_app_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


