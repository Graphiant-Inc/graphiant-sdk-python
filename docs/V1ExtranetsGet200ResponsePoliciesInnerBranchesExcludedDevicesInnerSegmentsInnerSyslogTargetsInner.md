# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_host** | **str** |  | [optional] 
**destination_port** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**source_interface** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**transport** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_syslog_targets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


