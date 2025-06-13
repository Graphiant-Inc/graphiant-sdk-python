# V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inside** | **str** |  | [optional] 
**pairs** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZonePairsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZonePairsValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_zones_value_zone import V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone from a JSON string
v1_global_config_patch_request_traffic_policies_zones_value_zone_instance = V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_zones_value_zone_dict = v1_global_config_patch_request_traffic_policies_zones_value_zone_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone from a dict
v1_global_config_patch_request_traffic_policies_zones_value_zone_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone.from_dict(v1_global_config_patch_request_traffic_policies_zones_value_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


