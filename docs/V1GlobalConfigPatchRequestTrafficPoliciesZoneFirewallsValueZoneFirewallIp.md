# V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_land_attacks** | **bool** |  | [optional] 
**session_limit** | [**V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIpSessionLimit**](V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIpSessionLimit.md) |  | [optional] 
**urpf** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip import V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp from a JSON string
v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip_instance = V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip_dict = v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp from a dict
v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValueZoneFirewallIp.from_dict(v1_global_config_patch_request_traffic_policies_zone_firewalls_value_zone_firewall_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


