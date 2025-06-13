# V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**disconnected_reason** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner import V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner from a JSON string
v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner_instance = V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner.to_json())

# convert the object into a dict
v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner_dict = v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner_instance.to_dict()
# create an instance of V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner from a dict
v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner_from_dict = V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner.from_dict(v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


