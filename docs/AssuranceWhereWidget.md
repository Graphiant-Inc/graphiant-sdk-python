# AssuranceWhereWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_sites_by_users** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 
**top_users_by_data_transferred** | [**List[AssuranceUserDefinition]**](AssuranceUserDefinition.md) |  | [optional] 
**top_vrfs_by_users** | [**List[AssuranceKpiMetric]**](AssuranceKpiMetric.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_where_widget import AssuranceWhereWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceWhereWidget from a JSON string
assurance_where_widget_instance = AssuranceWhereWidget.from_json(json)
# print the JSON string representation of the object
print(AssuranceWhereWidget.to_json())

# convert the object into a dict
assurance_where_widget_dict = assurance_where_widget_instance.to_dict()
# create an instance of AssuranceWhereWidget from a dict
assurance_where_widget_from_dict = AssuranceWhereWidget.from_dict(assurance_where_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


