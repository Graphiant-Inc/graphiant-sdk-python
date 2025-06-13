# V1AppsVisualizationPost200ResponseAppsVisualizationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**app_name** | **str** |  | [optional] 
**circuit_availability** | **Dict[str, int]** |  | [optional] 
**circuit_map** | [**Dict[str, V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue]**](V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue.md) |  | [optional] 
**current_status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_visualization_post200_response_apps_visualization_inner import V1AppsVisualizationPost200ResponseAppsVisualizationInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsVisualizationPost200ResponseAppsVisualizationInner from a JSON string
v1_apps_visualization_post200_response_apps_visualization_inner_instance = V1AppsVisualizationPost200ResponseAppsVisualizationInner.from_json(json)
# print the JSON string representation of the object
print(V1AppsVisualizationPost200ResponseAppsVisualizationInner.to_json())

# convert the object into a dict
v1_apps_visualization_post200_response_apps_visualization_inner_dict = v1_apps_visualization_post200_response_apps_visualization_inner_instance.to_dict()
# create an instance of V1AppsVisualizationPost200ResponseAppsVisualizationInner from a dict
v1_apps_visualization_post200_response_apps_visualization_inner_from_dict = V1AppsVisualizationPost200ResponseAppsVisualizationInner.from_dict(v1_apps_visualization_post200_response_apps_visualization_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


