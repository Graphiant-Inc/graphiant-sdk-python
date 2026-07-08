# AssuranceTopLevelKpi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_transferred_kbps_metric** | [**AssuranceKpiMetric**](AssuranceKpiMetric.md) |  | [optional] 
**shadow_ai_tools_metric** | [**AssuranceKpiMetric**](AssuranceKpiMetric.md) |  | [optional] 
**tools_metric** | [**AssuranceKpiMetric**](AssuranceKpiMetric.md) |  | [optional] 
**users_metric** | [**AssuranceKpiMetric**](AssuranceKpiMetric.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_top_level_kpi import AssuranceTopLevelKpi

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceTopLevelKpi from a JSON string
assurance_top_level_kpi_instance = AssuranceTopLevelKpi.from_json(json)
# print the JSON string representation of the object
print(AssuranceTopLevelKpi.to_json())

# convert the object into a dict
assurance_top_level_kpi_dict = assurance_top_level_kpi_instance.to_dict()
# create an instance of AssuranceTopLevelKpi from a dict
assurance_top_level_kpi_from_dict = AssuranceTopLevelKpi.from_dict(assurance_top_level_kpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


