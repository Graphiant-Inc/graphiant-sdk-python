# V2AssuranceBucketAppServersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**flex_algo_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_bucket_app_servers_post_request import V2AssuranceBucketAppServersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceBucketAppServersPostRequest from a JSON string
v2_assurance_bucket_app_servers_post_request_instance = V2AssuranceBucketAppServersPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceBucketAppServersPostRequest.to_json())

# convert the object into a dict
v2_assurance_bucket_app_servers_post_request_dict = v2_assurance_bucket_app_servers_post_request_instance.to_dict()
# create an instance of V2AssuranceBucketAppServersPostRequest from a dict
v2_assurance_bucket_app_servers_post_request_from_dict = V2AssuranceBucketAppServersPostRequest.from_dict(v2_assurance_bucket_app_servers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


