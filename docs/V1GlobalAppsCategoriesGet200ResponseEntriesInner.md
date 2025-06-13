# V1GlobalAppsCategoriesGet200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_count** | **int** |  | [optional] 
**category** | [**V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList**](V1GlobalAppsAppListsGet200ResponseEntriesInnerAppList.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_categories_get200_response_entries_inner import V1GlobalAppsCategoriesGet200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsCategoriesGet200ResponseEntriesInner from a JSON string
v1_global_apps_categories_get200_response_entries_inner_instance = V1GlobalAppsCategoriesGet200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsCategoriesGet200ResponseEntriesInner.to_json())

# convert the object into a dict
v1_global_apps_categories_get200_response_entries_inner_dict = v1_global_apps_categories_get200_response_entries_inner_instance.to_dict()
# create an instance of V1GlobalAppsCategoriesGet200ResponseEntriesInner from a dict
v1_global_apps_categories_get200_response_entries_inner_from_dict = V1GlobalAppsCategoriesGet200ResponseEntriesInner.from_dict(v1_global_apps_categories_get200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


