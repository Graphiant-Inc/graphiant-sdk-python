# V1DevicesDeviceIdConfigPutRequestCorePrometheus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_groups** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValue]**](V1DevicesDeviceIdConfigPutRequestCorePrometheusRuleGroupsValue.md) |  | [optional] 
**sink** | [**V1DevicesDeviceIdConfigPutRequestCorePrometheusSink**](V1DevicesDeviceIdConfigPutRequestCorePrometheusSink.md) |  | [optional] 
**sysdb_monitors** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCorePrometheusSysdbMonitorsValue]**](V1DevicesDeviceIdConfigPutRequestCorePrometheusSysdbMonitorsValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_prometheus import V1DevicesDeviceIdConfigPutRequestCorePrometheus

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCorePrometheus from a JSON string
v1_devices_device_id_config_put_request_core_prometheus_instance = V1DevicesDeviceIdConfigPutRequestCorePrometheus.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCorePrometheus.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_prometheus_dict = v1_devices_device_id_config_put_request_core_prometheus_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCorePrometheus from a dict
v1_devices_device_id_config_put_request_core_prometheus_from_dict = V1DevicesDeviceIdConfigPutRequestCorePrometheus.from_dict(v1_devices_device_id_config_put_request_core_prometheus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


