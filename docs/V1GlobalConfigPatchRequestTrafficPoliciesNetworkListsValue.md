# V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_network_lists_value import V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue from a JSON string
v1_global_config_patch_request_traffic_policies_network_lists_value_instance = V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_network_lists_value_dict = v1_global_config_patch_request_traffic_policies_network_lists_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue from a dict
v1_global_config_patch_request_traffic_policies_network_lists_value_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue.from_dict(v1_global_config_patch_request_traffic_policies_network_lists_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


