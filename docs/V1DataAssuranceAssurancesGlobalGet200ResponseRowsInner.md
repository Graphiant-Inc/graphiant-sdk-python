# V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerAppsInner]**](V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerAppsInner.md) |  | [optional] 
**assurance_id** | **int** |  | [optional] 
**assurance_name** | **str** |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**flex_algo** | **str** |  | [optional] 
**lans** | [**List[V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerLansInner]**](V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerLansInner.md) |  | [optional] 
**sites** | [**List[V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerSitesInner]**](V1DataAssuranceAssurancesGlobalGet200ResponseRowsInnerSitesInner.md) |  | [optional] 
**updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_data_assurance_assurances_global_get200_response_rows_inner import V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner from a JSON string
v1_data_assurance_assurances_global_get200_response_rows_inner_instance = V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner.from_json(json)
# print the JSON string representation of the object
print(V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner.to_json())

# convert the object into a dict
v1_data_assurance_assurances_global_get200_response_rows_inner_dict = v1_data_assurance_assurances_global_get200_response_rows_inner_instance.to_dict()
# create an instance of V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner from a dict
v1_data_assurance_assurances_global_get200_response_rows_inner_from_dict = V1DataAssuranceAssurancesGlobalGet200ResponseRowsInner.from_dict(v1_data_assurance_assurances_global_get200_response_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


