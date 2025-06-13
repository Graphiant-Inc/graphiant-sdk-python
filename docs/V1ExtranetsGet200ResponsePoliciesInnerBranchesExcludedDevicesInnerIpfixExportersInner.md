# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **str** |  | [optional] 
**destination_port** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**monitored_segments** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**sample_mode** | **str** |  | [optional] 
**sample_rate** | **int** |  | [optional] 
**source_address** | **str** |  | [optional] 
**source_interface** | **str** |  | [optional] 
**source_segment** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipfix_exporters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


