# V1GlobalAppsAppListsGet200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_count** | **int** |  | [optional] 
**app_list** | [**V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList**](V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList.md) |  | [optional] 
**policy_reference_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_app_lists_get200_response_entries_inner import V1GlobalAppsAppListsGet200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsAppListsGet200ResponseEntriesInner from a JSON string
v1_global_apps_app_lists_get200_response_entries_inner_instance = V1GlobalAppsAppListsGet200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsAppListsGet200ResponseEntriesInner.to_json())

# convert the object into a dict
v1_global_apps_app_lists_get200_response_entries_inner_dict = v1_global_apps_app_lists_get200_response_entries_inner_instance.to_dict()
# create an instance of V1GlobalAppsAppListsGet200ResponseEntriesInner from a dict
v1_global_apps_app_lists_get200_response_entries_inner_from_dict = V1GlobalAppsAppListsGet200ResponseEntriesInner.from_dict(v1_global_apps_app_lists_get200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


