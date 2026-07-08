# AssuranceApprovedAppEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | app name to approve (required) | 
**domain** | **str** | app name to approve | [optional] 
**id** | **str** | approved app entry identifier | [optional] 
**tag_requested** | **str** | resulting tag, approved or shadow (required) | 

## Example

```python
from graphiant_sdk.models.assurance_approved_app_entry_request import AssuranceApprovedAppEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceApprovedAppEntryRequest from a JSON string
assurance_approved_app_entry_request_instance = AssuranceApprovedAppEntryRequest.from_json(json)
# print the JSON string representation of the object
print(AssuranceApprovedAppEntryRequest.to_json())

# convert the object into a dict
assurance_approved_app_entry_request_dict = assurance_approved_app_entry_request_instance.to_dict()
# create an instance of AssuranceApprovedAppEntryRequest from a dict
assurance_approved_app_entry_request_from_dict = AssuranceApprovedAppEntryRequest.from_dict(assurance_approved_app_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


