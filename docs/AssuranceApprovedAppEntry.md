# AssuranceApprovedAppEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_users** | **int** | number of active users (required) | [optional] 
**category** | **str** | approved AI tool category (required) | [optional] 
**data_sent_kbps** | **float** | data sent in kbps (required) | [optional] 
**id** | **str** | approved app entry identifier (required) | [optional] 
**tool** | **str** | approved AI tool name (required) | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_approved_app_entry import AssuranceApprovedAppEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceApprovedAppEntry from a JSON string
assurance_approved_app_entry_instance = AssuranceApprovedAppEntry.from_json(json)
# print the JSON string representation of the object
print(AssuranceApprovedAppEntry.to_json())

# convert the object into a dict
assurance_approved_app_entry_dict = assurance_approved_app_entry_instance.to_dict()
# create an instance of AssuranceApprovedAppEntry from a dict
assurance_approved_app_entry_from_dict = AssuranceApprovedAppEntry.from_dict(assurance_approved_app_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


