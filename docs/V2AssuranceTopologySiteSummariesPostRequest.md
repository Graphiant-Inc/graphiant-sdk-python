# V2AssuranceTopologySiteSummariesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**app_server_key** | **str** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**filter** | [**V2AssuranceTopologyClientSessionsPostRequestFilter**](V2AssuranceTopologyClientSessionsPostRequestFilter.md) |  | [optional] 
**flex_algo_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_site_summaries_post_request import V2AssuranceTopologySiteSummariesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologySiteSummariesPostRequest from a JSON string
v2_assurance_topology_site_summaries_post_request_instance = V2AssuranceTopologySiteSummariesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologySiteSummariesPostRequest.to_json())

# convert the object into a dict
v2_assurance_topology_site_summaries_post_request_dict = v2_assurance_topology_site_summaries_post_request_instance.to_dict()
# create an instance of V2AssuranceTopologySiteSummariesPostRequest from a dict
v2_assurance_topology_site_summaries_post_request_from_dict = V2AssuranceTopologySiteSummariesPostRequest.from_dict(v2_assurance_topology_site_summaries_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


