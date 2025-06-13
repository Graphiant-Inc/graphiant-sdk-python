# V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_hosts** | **int** |  | [optional] 
**affected_regions** | **int** |  | [optional] 
**affected_sites** | **int** |  | [optional] 
**affected_vrfs** | **int** |  | [optional] 
**app_id** | **int** |  | [optional] 
**app_id_records** | [**List[V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord]**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.md) |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**da_classified** | **bool** |  | [optional] 
**flex_algo** | [**List[V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner]**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner.md) |  | [optional] 
**flows_analyzed** | **int** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**risk_status** | **str** |  | [optional] 
**threat_score** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_applicationdetailsbyname_post200_response_app_name_record import V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord from a JSON string
v2_assurance_applicationdetailsbyname_post200_response_app_name_record_instance = V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord.to_json())

# convert the object into a dict
v2_assurance_applicationdetailsbyname_post200_response_app_name_record_dict = v2_assurance_applicationdetailsbyname_post200_response_app_name_record_instance.to_dict()
# create an instance of V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord from a dict
v2_assurance_applicationdetailsbyname_post200_response_app_name_record_from_dict = V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord.from_dict(v2_assurance_applicationdetailsbyname_post200_response_app_name_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


