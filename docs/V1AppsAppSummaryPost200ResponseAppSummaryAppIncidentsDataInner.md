# V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_count** | **int** |  | [optional] 
**app_status** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner import V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner from a JSON string
v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner_instance = V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner.from_json(json)
# print the JSON string representation of the object
print(V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner.to_json())

# convert the object into a dict
v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner_dict = v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner_instance.to_dict()
# create an instance of V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner from a dict
v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner_from_dict = V1AppsAppSummaryPost200ResponseAppSummaryAppIncidentsDataInner.from_dict(v1_apps_app_summary_post200_response_app_summary_app_incidents_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


