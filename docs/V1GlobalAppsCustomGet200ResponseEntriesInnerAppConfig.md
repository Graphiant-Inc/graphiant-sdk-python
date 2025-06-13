# V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**ip_lists** | **List[str]** |  | [optional] 
**ip_prefixes** | **List[str]** |  | [optional] 
**ip_protocol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**port_ranges** | [**List[V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange]**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_apps_custom_get200_response_entries_inner_app_config import V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig from a JSON string
v1_global_apps_custom_get200_response_entries_inner_app_config_instance = V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig.from_json(json)
# print the JSON string representation of the object
print(V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig.to_json())

# convert the object into a dict
v1_global_apps_custom_get200_response_entries_inner_app_config_dict = v1_global_apps_custom_get200_response_entries_inner_app_config_instance.to_dict()
# create an instance of V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig from a dict
v1_global_apps_custom_get200_response_entries_inner_app_config_from_dict = V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig.from_dict(v1_global_apps_custom_get200_response_entries_inner_app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


