# V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_hosts** | **int** |  | [optional] 
**affected_regions** | **int** |  | [optional] 
**affected_sites** | **int** |  | [optional] 
**affected_vrfs** | **int** |  | [optional] 
**app_id_key** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**blocked_reason_list** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 
**classfication_field** | **str** |  | [optional] 
**classification_field** | **str** |  | [optional] 
**first_seen** | **int** |  | [optional] 
**flex_algo** | [**List[V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner]**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner.md) |  | [optional] 
**flows_analyzed** | **int** |  | [optional] 
**last_seen** | **int** |  | [optional] 
**new_ip_hint** | **bool** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**region_list** | **List[str]** |  | [optional] 
**risk_status** | **str** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **str** |  | [optional] 
**site_list** | **List[str]** |  | [optional] 
**threat_score** | **int** |  | [optional] 
**vrf_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_applicationdetailsbyname_post200_response_app_id_record import V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord from a JSON string
v2_assurance_applicationdetailsbyname_post200_response_app_id_record_instance = V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.to_json())

# convert the object into a dict
v2_assurance_applicationdetailsbyname_post200_response_app_id_record_dict = v2_assurance_applicationdetailsbyname_post200_response_app_id_record_instance.to_dict()
# create an instance of V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord from a dict
v2_assurance_applicationdetailsbyname_post200_response_app_id_record_from_dict = V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.from_dict(v2_assurance_applicationdetailsbyname_post200_response_app_id_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


