# V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface.md) |  | [optional] 
**operation** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_site_post_request_ipfix_exporter_ops_v2_value import V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value from a JSON string
v1_global_config_site_post_request_ipfix_exporter_ops_v2_value_instance = V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.to_json())

# convert the object into a dict
v1_global_config_site_post_request_ipfix_exporter_ops_v2_value_dict = v1_global_config_site_post_request_ipfix_exporter_ops_v2_value_instance.to_dict()
# create an instance of V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value from a dict
v1_global_config_site_post_request_ipfix_exporter_ops_v2_value_from_dict = V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.from_dict(v1_global_config_site_post_request_ipfix_exporter_ops_v2_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


