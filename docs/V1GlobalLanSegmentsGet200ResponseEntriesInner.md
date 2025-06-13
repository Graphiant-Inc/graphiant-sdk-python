# V1GlobalLanSegmentsGet200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_interfaces** | **int** |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**description** | **str** |  | [optional] 
**edge_references** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site_list_references** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_lan_segments_get200_response_entries_inner import V1GlobalLanSegmentsGet200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalLanSegmentsGet200ResponseEntriesInner from a JSON string
v1_global_lan_segments_get200_response_entries_inner_instance = V1GlobalLanSegmentsGet200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalLanSegmentsGet200ResponseEntriesInner.to_json())

# convert the object into a dict
v1_global_lan_segments_get200_response_entries_inner_dict = v1_global_lan_segments_get200_response_entries_inner_instance.to_dict()
# create an instance of V1GlobalLanSegmentsGet200ResponseEntriesInner from a dict
v1_global_lan_segments_get200_response_entries_inner_from_dict = V1GlobalLanSegmentsGet200ResponseEntriesInner.from_dict(v1_global_lan_segments_get200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


