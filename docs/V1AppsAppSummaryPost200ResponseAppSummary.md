# V1AppsAppSummaryPost200ResponseAppSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_health** | **Dict[str, int]** |  | [optional] 
**app_incidents** | [**V1AppsAppSummaryPost200ResponseAppSummaryAppIncidents**](V1AppsAppSummaryPost200ResponseAppSummaryAppIncidents.md) |  | [optional] 
**apps_on_device_count** | **int** |  | [optional] 
**average_qoe** | **float** |  | [optional] 
**circuits_incidents** | [**List[V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInner]**](V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsInner.md) |  | [optional] 
**circuits_incidentsv2** | [**List[V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsv2Inner]**](V1AppsAppSummaryPost200ResponseAppSummaryCircuitsIncidentsv2Inner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_app_summary_post200_response_app_summary import V1AppsAppSummaryPost200ResponseAppSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsAppSummaryPost200ResponseAppSummary from a JSON string
v1_apps_app_summary_post200_response_app_summary_instance = V1AppsAppSummaryPost200ResponseAppSummary.from_json(json)
# print the JSON string representation of the object
print(V1AppsAppSummaryPost200ResponseAppSummary.to_json())

# convert the object into a dict
v1_apps_app_summary_post200_response_app_summary_dict = v1_apps_app_summary_post200_response_app_summary_instance.to_dict()
# create an instance of V1AppsAppSummaryPost200ResponseAppSummary from a dict
v1_apps_app_summary_post200_response_app_summary_from_dict = V1AppsAppSummaryPost200ResponseAppSummary.from_dict(v1_apps_app_summary_post200_response_app_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


