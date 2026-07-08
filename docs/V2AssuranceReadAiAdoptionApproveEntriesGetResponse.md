# V2AssuranceReadAiAdoptionApproveEntriesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_app_list** | [**List[AssuranceApprovedAppEntry]**](AssuranceApprovedAppEntry.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_read_ai_adoption_approve_entries_get_response import V2AssuranceReadAiAdoptionApproveEntriesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceReadAiAdoptionApproveEntriesGetResponse from a JSON string
v2_assurance_read_ai_adoption_approve_entries_get_response_instance = V2AssuranceReadAiAdoptionApproveEntriesGetResponse.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceReadAiAdoptionApproveEntriesGetResponse.to_json())

# convert the object into a dict
v2_assurance_read_ai_adoption_approve_entries_get_response_dict = v2_assurance_read_ai_adoption_approve_entries_get_response_instance.to_dict()
# create an instance of V2AssuranceReadAiAdoptionApproveEntriesGetResponse from a dict
v2_assurance_read_ai_adoption_approve_entries_get_response_from_dict = V2AssuranceReadAiAdoptionApproveEntriesGetResponse.from_dict(v2_assurance_read_ai_adoption_approve_entries_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


