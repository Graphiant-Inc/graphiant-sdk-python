# V1ExtranetSitesUsageTopPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_b2_b** | **bool** |  | [optional] 
**is_provider** | **bool** |  | [optional] 
**service_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_sites_usage_top_post_request import V1ExtranetSitesUsageTopPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetSitesUsageTopPostRequest from a JSON string
v1_extranet_sites_usage_top_post_request_instance = V1ExtranetSitesUsageTopPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetSitesUsageTopPostRequest.to_json())

# convert the object into a dict
v1_extranet_sites_usage_top_post_request_dict = v1_extranet_sites_usage_top_post_request_instance.to_dict()
# create an instance of V1ExtranetSitesUsageTopPostRequest from a dict
v1_extranet_sites_usage_top_post_request_from_dict = V1ExtranetSitesUsageTopPostRequest.from_dict(v1_extranet_sites_usage_top_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


