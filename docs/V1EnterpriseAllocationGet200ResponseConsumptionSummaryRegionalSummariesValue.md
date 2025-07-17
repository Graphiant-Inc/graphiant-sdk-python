# V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueAllocation**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueAllocation.md) |  | [optional] 
**consumed_credits** | **float** |  | [optional] 
**core_conversion_factor** | **float** |  | [optional] 
**gw_conversion_factor** | **float** |  | [optional] 
**internet_consumption** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueInternetConsumption**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueInternetConsumption.md) |  | [optional] 
**usage** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueAllocation**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValueAllocation.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value import V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue from a JSON string
v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value_instance = V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue.to_json())

# convert the object into a dict
v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value_dict = v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value_instance.to_dict()
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue from a dict
v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value_from_dict = V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue.from_dict(v1_enterprise_allocation_get200_response_consumption_summary_regional_summaries_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


