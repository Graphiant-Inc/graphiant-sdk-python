# V1GlobalAppsCustomGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[V1GlobalAppsCustomGet200ResponseEntriesInner]**](V1GlobalAppsCustomGet200ResponseEntriesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_custom_get200_response import V1GlobalAppsCustomGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsCustomGet200Response from a JSON string
v1_global_apps_custom_get200_response_instance = V1GlobalAppsCustomGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsCustomGet200Response.to_json())

# convert the object into a dict
v1_global_apps_custom_get200_response_dict = v1_global_apps_custom_get200_response_instance.to_dict()
# create an instance of V1GlobalAppsCustomGet200Response from a dict
v1_global_apps_custom_get200_response_from_dict = V1GlobalAppsCustomGet200Response.from_dict(v1_global_apps_custom_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


