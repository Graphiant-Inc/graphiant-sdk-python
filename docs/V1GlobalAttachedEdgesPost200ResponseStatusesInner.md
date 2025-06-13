# V1GlobalAttachedEdgesPost200ResponseStatusesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**internal_state** | **str** |  | [optional] 
**site_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_since** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_attached_edges_post200_response_statuses_inner import V1GlobalAttachedEdgesPost200ResponseStatusesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAttachedEdgesPost200ResponseStatusesInner from a JSON string
v1_global_attached_edges_post200_response_statuses_inner_instance = V1GlobalAttachedEdgesPost200ResponseStatusesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAttachedEdgesPost200ResponseStatusesInner.to_json())

# convert the object into a dict
v1_global_attached_edges_post200_response_statuses_inner_dict = v1_global_attached_edges_post200_response_statuses_inner_instance.to_dict()
# create an instance of V1GlobalAttachedEdgesPost200ResponseStatusesInner from a dict
v1_global_attached_edges_post200_response_statuses_inner_from_dict = V1GlobalAttachedEdgesPost200ResponseStatusesInner.from_dict(v1_global_attached_edges_post200_response_statuses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


