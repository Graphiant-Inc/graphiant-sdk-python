# V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 
**stats** | [**V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValueStats**](V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValueStats.md) |  | [optional] 
**usage** | **float** |  | [optional] 
**usage_pct** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value import V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue from a JSON string
v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value_instance = V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue.from_json(json)
# print the JSON string representation of the object
print(V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue.to_json())

# convert the object into a dict
v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value_dict = v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value_instance.to_dict()
# create an instance of V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue from a dict
v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value_from_dict = V1AppsVisualizationPost200ResponseAppsVisualizationInnerCircuitMapValue.from_dict(v1_apps_visualization_post200_response_apps_visualization_inner_circuit_map_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


