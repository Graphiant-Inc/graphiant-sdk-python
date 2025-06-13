# V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_core** | **float** |  | [optional] 
**allocation_gw** | **float** |  | [optional] 
**credit_core** | **float** |  | [optional] 
**credit_gw** | **float** |  | [optional] 
**region_id** | **int** |  | [optional] 
**region_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get200_response_regional_allocations_inner import V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner from a JSON string
v1_enterprise_allocation_get200_response_regional_allocations_inner_instance = V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner.to_json())

# convert the object into a dict
v1_enterprise_allocation_get200_response_regional_allocations_inner_dict = v1_enterprise_allocation_get200_response_regional_allocations_inner_instance.to_dict()
# create an instance of V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner from a dict
v1_enterprise_allocation_get200_response_regional_allocations_inner_from_dict = V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner.from_dict(v1_enterprise_allocation_get200_response_regional_allocations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


