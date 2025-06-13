# V1GlobalConfigSitePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_prefix_set_ops** | **Dict[str, str]** |  | [optional] 
**ipfix_exporter_ops** | **Dict[str, str]** |  | [optional] 
**ipfix_exporter_ops_v2** | [**Dict[str, V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value]**](V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.md) |  | [optional] 
**prefix_set_ops** | **Dict[str, str]** |  | [optional] 
**routing_policy_ops** | **Dict[str, str]** |  | [optional] 
**site_id** | **int** |  | [optional] 
**snmp_ops** | **Dict[str, str]** |  | [optional] 
**syslog_server_ops** | **Dict[str, str]** |  | [optional] 
**syslog_server_ops_v2** | [**Dict[str, V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value]**](V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.md) |  | [optional] 
**traffic_policy_ops** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_site_post_request import V1GlobalConfigSitePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigSitePostRequest from a JSON string
v1_global_config_site_post_request_instance = V1GlobalConfigSitePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigSitePostRequest.to_json())

# convert the object into a dict
v1_global_config_site_post_request_dict = v1_global_config_site_post_request_instance.to_dict()
# create an instance of V1GlobalConfigSitePostRequest from a dict
v1_global_config_site_post_request_from_dict = V1GlobalConfigSitePostRequest.from_dict(v1_global_config_site_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


