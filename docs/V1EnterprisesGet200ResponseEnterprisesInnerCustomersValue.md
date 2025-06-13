# V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_email** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**counts** | [**V1EnterprisesGet200ResponseEnterprisesInnerCounts**](V1EnterprisesGet200ResponseEnterprisesInnerCounts.md) |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**impersonation_enabled** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_get200_response_enterprises_inner_customers_value import V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue from a JSON string
v1_enterprises_get200_response_enterprises_inner_customers_value_instance = V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue.to_json())

# convert the object into a dict
v1_enterprises_get200_response_enterprises_inner_customers_value_dict = v1_enterprises_get200_response_enterprises_inner_customers_value_instance.to_dict()
# create an instance of V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue from a dict
v1_enterprises_get200_response_enterprises_inner_customers_value_from_dict = V1EnterprisesGet200ResponseEnterprisesInnerCustomersValue.from_dict(v1_enterprises_get200_response_enterprises_inner_customers_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


