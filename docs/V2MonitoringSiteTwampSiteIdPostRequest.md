# V2MonitoringSiteTwampSiteIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner]**](V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_site_twamp_site_id_post_request import V2MonitoringSiteTwampSiteIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringSiteTwampSiteIdPostRequest from a JSON string
v2_monitoring_site_twamp_site_id_post_request_instance = V2MonitoringSiteTwampSiteIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringSiteTwampSiteIdPostRequest.to_json())

# convert the object into a dict
v2_monitoring_site_twamp_site_id_post_request_dict = v2_monitoring_site_twamp_site_id_post_request_instance.to_dict()
# create an instance of V2MonitoringSiteTwampSiteIdPostRequest from a dict
v2_monitoring_site_twamp_site_id_post_request_from_dict = V2MonitoringSiteTwampSiteIdPostRequest.from_dict(v2_monitoring_site_twamp_site_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


