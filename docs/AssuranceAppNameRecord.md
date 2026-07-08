# AssuranceAppNameRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_hosts** | **int** |  | [optional] 
**affected_regions** | **int** |  | [optional] 
**affected_sites** | **int** |  | [optional] 
**affected_vrfs** | **int** |  | [optional] 
**app_ai_tag** | **str** |  | [optional] 
**app_id** | **int** |  | [optional] 
**app_id_records** | [**List[AssuranceAppIdRecord]**](AssuranceAppIdRecord.md) |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**da_classified** | **bool** |  | [optional] 
**exchange_service** | [**List[AssuranceExchangeServiceIdentifier]**](AssuranceExchangeServiceIdentifier.md) |  | [optional] 
**flex_algo** | [**List[AssuranceFlexAlgoIdentifier]**](AssuranceFlexAlgoIdentifier.md) |  | [optional] 
**flows_analyzed** | **int** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**risk_status** | **str** |  | [optional] 
**threat_score** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_app_name_record import AssuranceAppNameRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceAppNameRecord from a JSON string
assurance_app_name_record_instance = AssuranceAppNameRecord.from_json(json)
# print the JSON string representation of the object
print(AssuranceAppNameRecord.to_json())

# convert the object into a dict
assurance_app_name_record_dict = assurance_app_name_record_instance.to_dict()
# create an instance of AssuranceAppNameRecord from a dict
assurance_app_name_record_from_dict = AssuranceAppNameRecord.from_dict(assurance_app_name_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


