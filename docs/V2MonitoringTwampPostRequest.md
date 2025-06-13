# V2MonitoringTwampPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**selectors** | [**List[V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner]**](V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_twamp_post_request import V2MonitoringTwampPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringTwampPostRequest from a JSON string
v2_monitoring_twamp_post_request_instance = V2MonitoringTwampPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringTwampPostRequest.to_json())

# convert the object into a dict
v2_monitoring_twamp_post_request_dict = v2_monitoring_twamp_post_request_instance.to_dict()
# create an instance of V2MonitoringTwampPostRequest from a dict
v2_monitoring_twamp_post_request_from_dict = V2MonitoringTwampPostRequest.from_dict(v2_monitoring_twamp_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


