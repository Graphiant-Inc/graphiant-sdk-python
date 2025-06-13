# V1EnterpriseAllocationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumption_summary** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummary**](V1EnterpriseAllocationGet200ResponseConsumptionSummary.md) |  | [optional] 
**conversion_holders** | [**Dict[str, V1EnterpriseAllocationGet200ResponseConversionHoldersValue]**](V1EnterpriseAllocationGet200ResponseConversionHoldersValue.md) |  | [optional] 
**regional_allocations** | [**List[V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner]**](V1EnterpriseAllocationGet200ResponseRegionalAllocationsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get200_response import V1EnterpriseAllocationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGet200Response from a JSON string
v1_enterprise_allocation_get200_response_instance = V1EnterpriseAllocationGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGet200Response.to_json())

# convert the object into a dict
v1_enterprise_allocation_get200_response_dict = v1_enterprise_allocation_get200_response_instance.to_dict()
# create an instance of V1EnterpriseAllocationGet200Response from a dict
v1_enterprise_allocation_get200_response_from_dict = V1EnterpriseAllocationGet200Response.from_dict(v1_enterprise_allocation_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


