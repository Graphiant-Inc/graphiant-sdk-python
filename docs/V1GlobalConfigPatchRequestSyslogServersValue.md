# V1GlobalConfigPatchRequestSyslogServersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**V1GlobalConfigPatchRequestSyslogServersValueTarget**](V1GlobalConfigPatchRequestSyslogServersValueTarget.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_syslog_servers_value import V1GlobalConfigPatchRequestSyslogServersValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSyslogServersValue from a JSON string
v1_global_config_patch_request_syslog_servers_value_instance = V1GlobalConfigPatchRequestSyslogServersValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSyslogServersValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_syslog_servers_value_dict = v1_global_config_patch_request_syslog_servers_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSyslogServersValue from a dict
v1_global_config_patch_request_syslog_servers_value_from_dict = V1GlobalConfigPatchRequestSyslogServersValue.from_dict(v1_global_config_patch_request_syslog_servers_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


