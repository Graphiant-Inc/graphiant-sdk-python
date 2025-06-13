# V2MonitoringBgpPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**selectors** | [**List[V2MonitoringBgpPostRequestSelectorsInner]**](V2MonitoringBgpPostRequestSelectorsInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_bgp_post_request import V2MonitoringBgpPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringBgpPostRequest from a JSON string
v2_monitoring_bgp_post_request_instance = V2MonitoringBgpPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringBgpPostRequest.to_json())

# convert the object into a dict
v2_monitoring_bgp_post_request_dict = v2_monitoring_bgp_post_request_instance.to_dict()
# create an instance of V2MonitoringBgpPostRequest from a dict
v2_monitoring_bgp_post_request_from_dict = V2MonitoringBgpPostRequest.from_dict(v2_monitoring_bgp_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


