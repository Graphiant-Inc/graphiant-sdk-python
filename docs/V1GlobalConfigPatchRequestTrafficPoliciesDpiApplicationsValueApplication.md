# V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**destination_network** | **str** |  | [optional] 
**destination_network_list** | **str** |  | [optional] 
**destination_networks** | [**V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks.md) |  | [optional] 
**destination_port** | **int** |  | [optional] 
**destination_port_list** | **str** |  | [optional] 
**destination_ports** | [**V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationPorts**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationPorts.md) |  | [optional] 
**icmp_type** | **int** |  | [optional] 
**ip_protocol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_network** | **str** |  | [optional] 
**source_network_list** | **str** |  | [optional] 
**source_networks** | [**V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationNetworks.md) |  | [optional] 
**source_port** | **int** |  | [optional] 
**source_port_list** | **str** |  | [optional] 
**source_ports** | [**V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationPorts**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplicationDestinationPorts.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_dpi_applications_value_application import V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication from a JSON string
v1_global_config_patch_request_traffic_policies_dpi_applications_value_application_instance = V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_dpi_applications_value_application_dict = v1_global_config_patch_request_traffic_policies_dpi_applications_value_application_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication from a dict
v1_global_config_patch_request_traffic_policies_dpi_applications_value_application_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValueApplication.from_dict(v1_global_config_patch_request_traffic_policies_dpi_applications_value_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


