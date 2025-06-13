# V1EnterpriseAllocationGet200ResponseConsumptionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contractual_summary** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryContractualSummary.md) |  | [optional] 
**global_summary** | [**V1EnterpriseAllocationGet200ResponseConsumptionSummaryGlobalSummary**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryGlobalSummary.md) |  | [optional] 
**regional_summaries** | [**Dict[str, V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue]**](V1EnterpriseAllocationGet200ResponseConsumptionSummaryRegionalSummariesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_allocation_get200_response_consumption_summary import V1EnterpriseAllocationGet200ResponseConsumptionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummary from a JSON string
v1_enterprise_allocation_get200_response_consumption_summary_instance = V1EnterpriseAllocationGet200ResponseConsumptionSummary.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseAllocationGet200ResponseConsumptionSummary.to_json())

# convert the object into a dict
v1_enterprise_allocation_get200_response_consumption_summary_dict = v1_enterprise_allocation_get200_response_consumption_summary_instance.to_dict()
# create an instance of V1EnterpriseAllocationGet200ResponseConsumptionSummary from a dict
v1_enterprise_allocation_get200_response_consumption_summary_from_dict = V1EnterpriseAllocationGet200ResponseConsumptionSummary.from_dict(v1_enterprise_allocation_get200_response_consumption_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


