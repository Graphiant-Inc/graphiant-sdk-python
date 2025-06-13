# V1GlobalConfigPatchRequestSyslogServersValueTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**global_id** | **int** |  | [optional] 
**host** | **str** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**severity** | **str** |  | [optional] 
**transport** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_syslog_servers_value_target import V1GlobalConfigPatchRequestSyslogServersValueTarget

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSyslogServersValueTarget from a JSON string
v1_global_config_patch_request_syslog_servers_value_target_instance = V1GlobalConfigPatchRequestSyslogServersValueTarget.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSyslogServersValueTarget.to_json())

# convert the object into a dict
v1_global_config_patch_request_syslog_servers_value_target_dict = v1_global_config_patch_request_syslog_servers_value_target_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSyslogServersValueTarget from a dict
v1_global_config_patch_request_syslog_servers_value_target_from_dict = V1GlobalConfigPatchRequestSyslogServersValueTarget.from_dict(v1_global_config_patch_request_syslog_servers_value_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


