# V1EnterprisesGet200ResponseEnterprisesInnerCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_down_count** | **int** |  | [optional] 
**active_up_count** | **int** |  | [optional] 
**deactivated_down_count** | **int** |  | [optional] 
**down_sites_count** | **int** |  | [optional] 
**empty_sites_count** | **int** |  | [optional] 
**impaired_sites_count** | **int** |  | [optional] 
**staging_down_count** | **int** |  | [optional] 
**staging_up_count** | **int** |  | [optional] 
**total_customers** | **int** |  | [optional] 
**total_edges** | **int** |  | [optional] 
**total_msps** | **int** |  | [optional] 
**total_sites** | **int** |  | [optional] 
**up_sites_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_get200_response_enterprises_inner_counts import V1EnterprisesGet200ResponseEnterprisesInnerCounts

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesGet200ResponseEnterprisesInnerCounts from a JSON string
v1_enterprises_get200_response_enterprises_inner_counts_instance = V1EnterprisesGet200ResponseEnterprisesInnerCounts.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesGet200ResponseEnterprisesInnerCounts.to_json())

# convert the object into a dict
v1_enterprises_get200_response_enterprises_inner_counts_dict = v1_enterprises_get200_response_enterprises_inner_counts_instance.to_dict()
# create an instance of V1EnterprisesGet200ResponseEnterprisesInnerCounts from a dict
v1_enterprises_get200_response_enterprises_inner_counts_from_dict = V1EnterprisesGet200ResponseEnterprisesInnerCounts.from_dict(v1_enterprises_get200_response_enterprises_inner_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


