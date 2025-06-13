# V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**interval_seconds** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroupRulesValue]**](V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroupRulesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group import V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup from a JSON string
v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group_instance = V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group_dict = v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup from a dict
v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group_from_dict = V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValueRuleGroup.from_dict(v1_devices_device_id_config_put_request_core_prometheus_rule_groups_value_rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


