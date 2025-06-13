# V2MonitoringExtranetLogDetailsPost200ResponseLogsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**server_address** | **str** |  | [optional] 
**site_name** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_extranet_log_details_post200_response_logs_inner import V2MonitoringExtranetLogDetailsPost200ResponseLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringExtranetLogDetailsPost200ResponseLogsInner from a JSON string
v2_monitoring_extranet_log_details_post200_response_logs_inner_instance = V2MonitoringExtranetLogDetailsPost200ResponseLogsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringExtranetLogDetailsPost200ResponseLogsInner.to_json())

# convert the object into a dict
v2_monitoring_extranet_log_details_post200_response_logs_inner_dict = v2_monitoring_extranet_log_details_post200_response_logs_inner_instance.to_dict()
# create an instance of V2MonitoringExtranetLogDetailsPost200ResponseLogsInner from a dict
v2_monitoring_extranet_log_details_post200_response_logs_inner_from_dict = V2MonitoringExtranetLogDetailsPost200ResponseLogsInner.from_dict(v2_monitoring_extranet_log_details_post200_response_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


