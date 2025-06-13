# V2MonitoringPolicyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**selectors** | [**List[V2MonitoringPolicyPostRequestSelectorsInner]**](V2MonitoringPolicyPostRequestSelectorsInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_policy_post_request import V2MonitoringPolicyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringPolicyPostRequest from a JSON string
v2_monitoring_policy_post_request_instance = V2MonitoringPolicyPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringPolicyPostRequest.to_json())

# convert the object into a dict
v2_monitoring_policy_post_request_dict = v2_monitoring_policy_post_request_instance.to_dict()
# create an instance of V2MonitoringPolicyPostRequest from a dict
v2_monitoring_policy_post_request_from_dict = V2MonitoringPolicyPostRequest.from_dict(v2_monitoring_policy_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


