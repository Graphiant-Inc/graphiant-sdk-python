# V1PolicyApplicationsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[V1PolicyApplicationsGet200ResponseApplicationsInner]**](V1PolicyApplicationsGet200ResponseApplicationsInner.md) |  | [optional] 
**page_info** | [**V1NatEntriesDeviceIdGet200ResponsePageInfo**](V1NatEntriesDeviceIdGet200ResponsePageInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_applications_get200_response import V1PolicyApplicationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyApplicationsGet200Response from a JSON string
v1_policy_applications_get200_response_instance = V1PolicyApplicationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1PolicyApplicationsGet200Response.to_json())

# convert the object into a dict
v1_policy_applications_get200_response_dict = v1_policy_applications_get200_response_instance.to_dict()
# create an instance of V1PolicyApplicationsGet200Response from a dict
v1_policy_applications_get200_response_from_dict = V1PolicyApplicationsGet200Response.from_dict(v1_policy_applications_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


