# V2AllowlistRuleIdGet200ResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**device_interface** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**is_wan_circuit** | **bool** |  | [optional] 
**note_text** | **str** |  | [optional] 
**peer_device_interface** | **str** |  | [optional] 
**peer_device_name** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**rule_name** | **str** |  | [optional] 
**site_name** | **str** |  | [optional] 
**vrf_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_allowlist_rule_id_get200_response_records_inner import V2AllowlistRuleIdGet200ResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AllowlistRuleIdGet200ResponseRecordsInner from a JSON string
v2_allowlist_rule_id_get200_response_records_inner_instance = V2AllowlistRuleIdGet200ResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(V2AllowlistRuleIdGet200ResponseRecordsInner.to_json())

# convert the object into a dict
v2_allowlist_rule_id_get200_response_records_inner_dict = v2_allowlist_rule_id_get200_response_records_inner_instance.to_dict()
# create an instance of V2AllowlistRuleIdGet200ResponseRecordsInner from a dict
v2_allowlist_rule_id_get200_response_records_inner_from_dict = V2AllowlistRuleIdGet200ResponseRecordsInner.from_dict(v2_allowlist_rule_id_get200_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


