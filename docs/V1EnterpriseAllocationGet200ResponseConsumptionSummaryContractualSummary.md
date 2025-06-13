# V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummaryExpirationDate**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummaryExpirationDate.md) |  | [optional] 
**total_consumed_credits** | **float** |  | [optional] 
**total_contracted_credits** | **float** |  | [optional] 
**total_remaining_credits** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary import V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary from a JSON string
v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary_instance = V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary.to_json())

# convert the object into a dict
v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary_dict = v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary_instance.to_dict()
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary from a dict
v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary_from_dict = V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary.from_dict(v1_enterprise_allocation_get200_response_consumption_summary_contractual_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


