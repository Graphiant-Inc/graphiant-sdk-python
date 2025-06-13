# V1PolicyApplicationsGet200ResponseApplicationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_applications_get200_response_applications_inner import V1PolicyApplicationsGet200ResponseApplicationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyApplicationsGet200ResponseApplicationsInner from a JSON string
v1_policy_applications_get200_response_applications_inner_instance = V1PolicyApplicationsGet200ResponseApplicationsInner.from_json(json)
# print the JSON string representation of the object
print(V1PolicyApplicationsGet200ResponseApplicationsInner.to_json())

# convert the object into a dict
v1_policy_applications_get200_response_applications_inner_dict = v1_policy_applications_get200_response_applications_inner_instance.to_dict()
# create an instance of V1PolicyApplicationsGet200ResponseApplicationsInner from a dict
v1_policy_applications_get200_response_applications_inner_from_dict = V1PolicyApplicationsGet200ResponseApplicationsInner.from_dict(v1_policy_applications_get200_response_applications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


