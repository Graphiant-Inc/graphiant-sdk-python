# V2AssuranceBucketAppServersAllGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_server_changes** | [**List[V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner]**](V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_bucket_app_servers_all_get200_response import V2AssuranceBucketAppServersAllGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceBucketAppServersAllGet200Response from a JSON string
v2_assurance_bucket_app_servers_all_get200_response_instance = V2AssuranceBucketAppServersAllGet200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceBucketAppServersAllGet200Response.to_json())

# convert the object into a dict
v2_assurance_bucket_app_servers_all_get200_response_dict = v2_assurance_bucket_app_servers_all_get200_response_instance.to_dict()
# create an instance of V2AssuranceBucketAppServersAllGet200Response from a dict
v2_assurance_bucket_app_servers_all_get200_response_from_dict = V2AssuranceBucketAppServersAllGet200Response.from_dict(v2_assurance_bucket_app_servers_all_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


