# V1EnterpriseAllocationGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumption_summary** | [**ManaV2BandwidthConsumptionSummary**](ManaV2BandwidthConsumptionSummary.md) |  | [optional] 
**conversion_holders** | [**Dict[str, ManaV2AllocationConversionHolder]**](ManaV2AllocationConversionHolder.md) |  | [optional] 
**regional_allocations** | [**List[ManaV2RegionalAllocation]**](ManaV2RegionalAllocation.md) |  | [optional] 
**zero_trust_summary** | [**ManaV2ZeroTrustConsumptionSummary**](ManaV2ZeroTrustConsumptionSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get_response import V1EnterpriseAllocationGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGetResponse from a JSON string
v1_enterprise_allocation_get_response_instance = V1EnterpriseAllocationGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGetResponse.to_json())

# convert the object into a dict
v1_enterprise_allocation_get_response_dict = v1_enterprise_allocation_get_response_instance.to_dict()
# create an instance of V1EnterpriseAllocationGetResponse from a dict
v1_enterprise_allocation_get_response_from_dict = V1EnterpriseAllocationGetResponse.from_dict(v1_enterprise_allocation_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


