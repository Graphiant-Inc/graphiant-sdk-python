# V1SitesPostRequestSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_prefix_set_ops** | **Dict[str, str]** |  | [optional] 
**ipfix_exporter_ops** | **Dict[str, str]** |  | [optional] 
**ipfix_exporter_ops_v2** | [**Dict[str, V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value]**](V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.md) |  | [optional] 
**location** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation.md) |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**prefix_set_ops** | **Dict[str, str]** |  | [optional] 
**route_tag** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry.md) |  | [optional] 
**routing_policy_ops** | **Dict[str, str]** |  | [optional] 
**snmp_ops** | **Dict[str, str]** |  | [optional] 
**syslog_server_ops** | **Dict[str, str]** |  | [optional] 
**syslog_server_ops_v2** | [**Dict[str, V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value]**](V1GlobalConfigSitePostRequestIpfixExporterOpsV2Value.md) |  | [optional] 
**traffic_policy_ops** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_post_request_site import V1SitesPostRequestSite

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesPostRequestSite from a JSON string
v1_sites_post_request_site_instance = V1SitesPostRequestSite.from_json(json)
# print the JSON string representation of the object
print(V1SitesPostRequestSite.to_json())

# convert the object into a dict
v1_sites_post_request_site_dict = v1_sites_post_request_site_instance.to_dict()
# create an instance of V1SitesPostRequestSite from a dict
v1_sites_post_request_site_from_dict = V1SitesPostRequestSite.from_dict(v1_sites_post_request_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


