# V1GlobalAppsCustomGet200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList**](V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList.md) |  | [optional] 
**app_config** | [**V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig**](V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig.md) |  | [optional] 
**app_list_reference_count** | **int** |  | [optional] 
**policy_reference_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_custom_get200_response_entries_inner import V1GlobalAppsCustomGet200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsCustomGet200ResponseEntriesInner from a JSON string
v1_global_apps_custom_get200_response_entries_inner_instance = V1GlobalAppsCustomGet200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsCustomGet200ResponseEntriesInner.to_json())

# convert the object into a dict
v1_global_apps_custom_get200_response_entries_inner_dict = v1_global_apps_custom_get200_response_entries_inner_instance.to_dict()
# create an instance of V1GlobalAppsCustomGet200ResponseEntriesInner from a dict
v1_global_apps_custom_get200_response_entries_inner_from_dict = V1GlobalAppsCustomGet200ResponseEntriesInner.from_dict(v1_global_apps_custom_get200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


