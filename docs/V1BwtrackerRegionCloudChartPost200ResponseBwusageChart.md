# V1BwtrackerRegionCloudChartPost200ResponseBwusageChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwusage_chart** | [**List[V1BwtrackerRegionCloudChartPost200ResponseBwusageChartBwusageChartInner]**](V1BwtrackerRegionCloudChartPost200ResponseBwusageChartBwusageChartInner.md) |  | [optional] 
**percentile_usage_kbps** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart import V1BwtrackerRegionCloudChartPost200ResponseBwusageChart

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerRegionCloudChartPost200ResponseBwusageChart from a JSON string
v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart_instance = V1BwtrackerRegionCloudChartPost200ResponseBwusageChart.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerRegionCloudChartPost200ResponseBwusageChart.to_json())

# convert the object into a dict
v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart_dict = v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart_instance.to_dict()
# create an instance of V1BwtrackerRegionCloudChartPost200ResponseBwusageChart from a dict
v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart_from_dict = V1BwtrackerRegionCloudChartPost200ResponseBwusageChart.from_dict(v1_bwtracker_region_cloud_chart_post200_response_bwusage_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


