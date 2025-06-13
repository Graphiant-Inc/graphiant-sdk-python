# V2MonitoringBfdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**selectors** | [**List[V2MonitoringBfdPostRequestSelectorsInner]**](V2MonitoringBfdPostRequestSelectorsInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_bfd_post_request import V2MonitoringBfdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringBfdPostRequest from a JSON string
v2_monitoring_bfd_post_request_instance = V2MonitoringBfdPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringBfdPostRequest.to_json())

# convert the object into a dict
v2_monitoring_bfd_post_request_dict = v2_monitoring_bfd_post_request_instance.to_dict()
# create an instance of V2MonitoringBfdPostRequest from a dict
v2_monitoring_bfd_post_request_from_dict = V2MonitoringBfdPostRequest.from_dict(v2_monitoring_bfd_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


