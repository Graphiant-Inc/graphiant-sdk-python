# V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flows_analyzed** | **int** |  | [optional] 
**gap_score** | **int** |  | [optional] 
**prev_gap_score** | **int** |  | [optional] 
**risk_bin** | **int** |  | [optional] 
**threat_count** | **int** |  | [optional] 
**unique_apps_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_enterprisesummary_post200_response_enterprise_summary import V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary from a JSON string
v2_assurance_enterprisesummary_post200_response_enterprise_summary_instance = V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary.to_json())

# convert the object into a dict
v2_assurance_enterprisesummary_post200_response_enterprise_summary_dict = v2_assurance_enterprisesummary_post200_response_enterprise_summary_instance.to_dict()
# create an instance of V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary from a dict
v2_assurance_enterprisesummary_post200_response_enterprise_summary_from_dict = V2AssuranceEnterprisesummaryPost200ResponseEnterpriseSummary.from_dict(v2_assurance_enterprisesummary_post200_response_enterprise_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


