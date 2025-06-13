# V1GlobalAppsAppListsPostRequestAppListConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[V1GlobalAppsAppListsGet200ResponseEntriesInnerAppListIdentifier]**](V1GlobalAppsAppListsGet200ResponseEntriesInnerAppListIdentifier.md) |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_app_lists_post_request_app_list_config import V1GlobalAppsAppListsPostRequestAppListConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsAppListsPostRequestAppListConfig from a JSON string
v1_global_apps_app_lists_post_request_app_list_config_instance = V1GlobalAppsAppListsPostRequestAppListConfig.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsAppListsPostRequestAppListConfig.to_json())

# convert the object into a dict
v1_global_apps_app_lists_post_request_app_list_config_dict = v1_global_apps_app_lists_post_request_app_list_config_instance.to_dict()
# create an instance of V1GlobalAppsAppListsPostRequestAppListConfig from a dict
v1_global_apps_app_lists_post_request_app_list_config_from_dict = V1GlobalAppsAppListsPostRequestAppListConfig.from_dict(v1_global_apps_app_lists_post_request_app_list_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


