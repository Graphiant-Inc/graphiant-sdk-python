# V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dl_incidents** | [**V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents**](V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents.md) |  | [optional] 
**overall_status** | **str** |  | [optional] 
**total_incidents** | [**V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents**](V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents.md) |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**ul_incidents** | [**V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents**](V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInnerDlIncidents.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner import V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner from a JSON string
v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner_instance = V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner.from_json(json)
# print the JSON string representation of the object
print(V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner.to_json())

# convert the object into a dict
v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner_dict = v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner_instance.to_dict()
# create an instance of V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner from a dict
v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner_from_dict = V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInnerDataInner.from_dict(v1_apps_app_summary_post200_response_app_summary_circuits_incidents_inner_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


