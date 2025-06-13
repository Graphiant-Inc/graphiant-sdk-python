# V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_servers** | [**List[V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerAddedServersInner]**](V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerAddedServersInner.md) |  | [optional] 
**app** | [**V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerApp**](V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerApp.md) |  | [optional] 
**removed_servers** | [**List[V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerAddedServersInner]**](V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInnerAddedServersInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner import V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner from a JSON string
v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner_instance = V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner.to_json())

# convert the object into a dict
v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner_dict = v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner_instance.to_dict()
# create an instance of V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner from a dict
v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner_from_dict = V2AssuranceBucketAppServersAllGet200ResponseAppServerChangesInner.from_dict(v2_assurance_bucket_app_servers_all_get200_response_app_server_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


