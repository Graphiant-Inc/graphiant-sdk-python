# AssuranceKpiMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **float** | delta value for the metric | [optional] 
**name** | **str** | name of the metric | [optional] 
**percent** | **float** | AI adoption percent for the metric | [optional] 
**tag** | **str** | AI adoption tag for the metric | [optional] 
**value** | **float** | metric value (required) | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_kpi_metric import AssuranceKpiMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceKpiMetric from a JSON string
assurance_kpi_metric_instance = AssuranceKpiMetric.from_json(json)
# print the JSON string representation of the object
print(AssuranceKpiMetric.to_json())

# convert the object into a dict
assurance_kpi_metric_dict = assurance_kpi_metric_instance.to_dict()
# create an instance of AssuranceKpiMetric from a dict
assurance_kpi_metric_from_dict = AssuranceKpiMetric.from_dict(assurance_kpi_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


