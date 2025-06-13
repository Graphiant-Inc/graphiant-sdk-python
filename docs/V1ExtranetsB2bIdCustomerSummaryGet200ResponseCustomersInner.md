# V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_email** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_id_customer_summary_get200_response_customers_inner import V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner from a JSON string
v1_extranets_b2b_id_customer_summary_get200_response_customers_inner_instance = V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner.to_json())

# convert the object into a dict
v1_extranets_b2b_id_customer_summary_get200_response_customers_inner_dict = v1_extranets_b2b_id_customer_summary_get200_response_customers_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner from a dict
v1_extranets_b2b_id_customer_summary_get200_response_customers_inner_from_dict = V1ExtranetsB2bIdCustomerSummaryGet200ResponseCustomersInner.from_dict(v1_extranets_b2b_id_customer_summary_get200_response_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


