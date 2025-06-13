# V1EnterprisesManagedGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**V1EnterprisesGet200ResponseEnterprisesInnerCounts**](V1EnterprisesGet200ResponseEnterprisesInnerCounts.md) |  | [optional] 
**enterprises** | [**List[V1EnterprisesGet200ResponseEnterprisesInner]**](V1EnterprisesGet200ResponseEnterprisesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_managed_get200_response import V1EnterprisesManagedGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesManagedGet200Response from a JSON string
v1_enterprises_managed_get200_response_instance = V1EnterprisesManagedGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesManagedGet200Response.to_json())

# convert the object into a dict
v1_enterprises_managed_get200_response_dict = v1_enterprises_managed_get200_response_instance.to_dict()
# create an instance of V1EnterprisesManagedGet200Response from a dict
v1_enterprises_managed_get200_response_from_dict = V1EnterprisesManagedGet200Response.from_dict(v1_enterprises_managed_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


