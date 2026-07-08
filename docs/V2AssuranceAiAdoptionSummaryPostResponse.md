# V2AssuranceAiAdoptionSummaryPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_level_kpi** | [**AssuranceTopLevelKpi**](AssuranceTopLevelKpi.md) |  | [optional] 
**what_widget** | [**AssuranceWhatWidget**](AssuranceWhatWidget.md) |  | [optional] 
**when_widget** | [**AssuranceWhenWidget**](AssuranceWhenWidget.md) |  | [optional] 
**where_widget** | [**AssuranceWhereWidget**](AssuranceWhereWidget.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_ai_adoption_summary_post_response import V2AssuranceAiAdoptionSummaryPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceAiAdoptionSummaryPostResponse from a JSON string
v2_assurance_ai_adoption_summary_post_response_instance = V2AssuranceAiAdoptionSummaryPostResponse.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceAiAdoptionSummaryPostResponse.to_json())

# convert the object into a dict
v2_assurance_ai_adoption_summary_post_response_dict = v2_assurance_ai_adoption_summary_post_response_instance.to_dict()
# create an instance of V2AssuranceAiAdoptionSummaryPostResponse from a dict
v2_assurance_ai_adoption_summary_post_response_from_dict = V2AssuranceAiAdoptionSummaryPostResponse.from_dict(v2_assurance_ai_adoption_summary_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


