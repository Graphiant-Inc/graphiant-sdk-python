# AssuranceClassifiedApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**classification_entry_id** | **str** |  | [optional] 
**ip_prefix_list** | **List[str]** |  | [optional] 
**port_list** | **List[str]** |  | [optional] 
**protocol_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_classified_application import AssuranceClassifiedApplication

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceClassifiedApplication from a JSON string
assurance_classified_application_instance = AssuranceClassifiedApplication.from_json(json)
# print the JSON string representation of the object
print(AssuranceClassifiedApplication.to_json())

# convert the object into a dict
assurance_classified_application_dict = assurance_classified_application_instance.to_dict()
# create an instance of AssuranceClassifiedApplication from a dict
assurance_classified_application_from_dict = AssuranceClassifiedApplication.from_dict(assurance_classified_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


