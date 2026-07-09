# AssuranceWhatWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bubble_categories** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**top_tools_by_active_users** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**top_tools_by_data_transferred** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_what_widget import AssuranceWhatWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceWhatWidget from a JSON string
assurance_what_widget_instance = AssuranceWhatWidget.from_json(json)
# print the JSON string representation of the object
print(AssuranceWhatWidget.to_json())

# convert the object into a dict
assurance_what_widget_dict = assurance_what_widget_instance.to_dict()
# create an instance of AssuranceWhatWidget from a dict
assurance_what_widget_from_dict = AssuranceWhatWidget.from_dict(assurance_what_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


