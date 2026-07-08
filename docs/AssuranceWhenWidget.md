# AssuranceWhenWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**hour_of_day** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**monthly_active_users** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**monthly_bandwidth_transferred** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_when_widget import AssuranceWhenWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceWhenWidget from a JSON string
assurance_when_widget_instance = AssuranceWhenWidget.from_json(json)
# print the JSON string representation of the object
print(AssuranceWhenWidget.to_json())

# convert the object into a dict
assurance_when_widget_dict = assurance_when_widget_instance.to_dict()
# create an instance of AssuranceWhenWidget from a dict
assurance_when_widget_from_dict = AssuranceWhenWidget.from_dict(assurance_when_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


