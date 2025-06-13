# V1GlobalAppsAppListsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_list_config** | [**V1GlobalAppsAppListsPostRequestAppListConfig**](V1GlobalAppsAppListsPostRequestAppListConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_app_lists_post_request import V1GlobalAppsAppListsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsAppListsPostRequest from a JSON string
v1_global_apps_app_lists_post_request_instance = V1GlobalAppsAppListsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsAppListsPostRequest.to_json())

# convert the object into a dict
v1_global_apps_app_lists_post_request_dict = v1_global_apps_app_lists_post_request_instance.to_dict()
# create an instance of V1GlobalAppsAppListsPostRequest from a dict
v1_global_apps_app_lists_post_request_from_dict = V1GlobalAppsAppListsPostRequest.from_dict(v1_global_apps_app_lists_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


