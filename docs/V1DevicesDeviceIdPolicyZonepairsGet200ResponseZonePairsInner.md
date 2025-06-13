# V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inside** | **str** |  | [optional] 
**outside** | **str** |  | [optional] 
**security_rulesets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner import V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner from a JSON string
v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner_instance = V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner.to_json())

# convert the object into a dict
v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner_dict = v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner_instance.to_dict()
# create an instance of V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner from a dict
v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner_from_dict = V1DevicesDeviceIdPolicyZonepairsGet200ResponseZonePairsInner.from_dict(v1_devices_device_id_policy_zonepairs_get200_response_zone_pairs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


