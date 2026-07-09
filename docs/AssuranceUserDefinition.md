# AssuranceUserDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sent** | **float** | data sent by the user (required) | [optional] 
**managed** | **bool** | whether the user is managed (required) | [optional] 
**sessions_day** | **float** | daily sessions for the user (required) | [optional] 
**user** | **str** | user identifier (required) | [optional] 
**vrf** | **str** | VRF associated with the user (required) | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_user_definition import AssuranceUserDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceUserDefinition from a JSON string
assurance_user_definition_instance = AssuranceUserDefinition.from_json(json)
# print the JSON string representation of the object
print(AssuranceUserDefinition.to_json())

# convert the object into a dict
assurance_user_definition_dict = assurance_user_definition_instance.to_dict()
# create an instance of AssuranceUserDefinition from a dict
assurance_user_definition_from_dict = AssuranceUserDefinition.from_dict(assurance_user_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


