# V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**classification_entry_id** | **str** |  | [optional] 
**ip_prefix_list** | **List[str]** |  | [optional] 
**port_list** | **List[str]** |  | [optional] 
**protocol_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner import V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner from a JSON string
v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner_instance = V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner.to_json())

# convert the object into a dict
v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner_dict = v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner_instance.to_dict()
# create an instance of V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner from a dict
v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner_from_dict = V2AssuranceGetclassifiedapplicationlistGet200ResponseClassifiedApplicationListInner.from_dict(v2_assurance_getclassifiedapplicationlist_get200_response_classified_application_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


