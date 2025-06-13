# V2MonitoringSegmentRouteCountsPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**ipv4_route_count** | [**V2MonitoringBfdPost200ResponseDataInnerSamplesInner**](V2MonitoringBfdPost200ResponseDataInnerSamplesInner.md) |  | [optional] 
**ipv6_route_count** | [**V2MonitoringBfdPost200ResponseDataInnerSamplesInner**](V2MonitoringBfdPost200ResponseDataInnerSamplesInner.md) |  | [optional] 
**segment_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_segment_route_counts_post200_response_data_inner import V2MonitoringSegmentRouteCountsPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringSegmentRouteCountsPost200ResponseDataInner from a JSON string
v2_monitoring_segment_route_counts_post200_response_data_inner_instance = V2MonitoringSegmentRouteCountsPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringSegmentRouteCountsPost200ResponseDataInner.to_json())

# convert the object into a dict
v2_monitoring_segment_route_counts_post200_response_data_inner_dict = v2_monitoring_segment_route_counts_post200_response_data_inner_instance.to_dict()
# create an instance of V2MonitoringSegmentRouteCountsPost200ResponseDataInner from a dict
v2_monitoring_segment_route_counts_post200_response_data_inner_from_dict = V2MonitoringSegmentRouteCountsPost200ResponseDataInner.from_dict(v2_monitoring_segment_route_counts_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


