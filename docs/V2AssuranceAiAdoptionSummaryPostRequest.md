# V2AssuranceAiAdoptionSummaryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | [**AssuranceTimeWindow**](AssuranceTimeWindow.md) |  | 
**user_list_size** | **int** | list size of user list in where widget (required) | 

## Example

```python
from graphiant_sdk.models.v2_assurance_ai_adoption_summary_post_request import V2AssuranceAiAdoptionSummaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceAiAdoptionSummaryPostRequest from a JSON string
v2_assurance_ai_adoption_summary_post_request_instance = V2AssuranceAiAdoptionSummaryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceAiAdoptionSummaryPostRequest.to_json())

# convert the object into a dict
v2_assurance_ai_adoption_summary_post_request_dict = v2_assurance_ai_adoption_summary_post_request_instance.to_dict()
# create an instance of V2AssuranceAiAdoptionSummaryPostRequest from a dict
v2_assurance_ai_adoption_summary_post_request_from_dict = V2AssuranceAiAdoptionSummaryPostRequest.from_dict(v2_assurance_ai_adoption_summary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


