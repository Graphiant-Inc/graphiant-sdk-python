# V1GlobalAppsCustomPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config** | [**V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig**](V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_custom_post_request import V1GlobalAppsCustomPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsCustomPostRequest from a JSON string
v1_global_apps_custom_post_request_instance = V1GlobalAppsCustomPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsCustomPostRequest.to_json())

# convert the object into a dict
v1_global_apps_custom_post_request_dict = v1_global_apps_custom_post_request_instance.to_dict()
# create an instance of V1GlobalAppsCustomPostRequest from a dict
v1_global_apps_custom_post_request_from_dict = V1GlobalAppsCustomPostRequest.from_dict(v1_global_apps_custom_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


