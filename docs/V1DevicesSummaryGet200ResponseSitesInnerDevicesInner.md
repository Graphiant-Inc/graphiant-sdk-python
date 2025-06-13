# V1DevicesSummaryGet200ResponseSitesInnerDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_virtual** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**override_region** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRegion**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRegion.md) |  | [optional] 
**platform_name** | **str** |  | [optional] 
**region** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRegion**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRegion.md) |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_summary_get200_response_sites_inner_devices_inner import V1DevicesSummaryGet200ResponseSitesInnerDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesSummaryGet200ResponseSitesInnerDevicesInner from a JSON string
v1_devices_summary_get200_response_sites_inner_devices_inner_instance = V1DevicesSummaryGet200ResponseSitesInnerDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesSummaryGet200ResponseSitesInnerDevicesInner.to_json())

# convert the object into a dict
v1_devices_summary_get200_response_sites_inner_devices_inner_dict = v1_devices_summary_get200_response_sites_inner_devices_inner_instance.to_dict()
# create an instance of V1DevicesSummaryGet200ResponseSitesInnerDevicesInner from a dict
v1_devices_summary_get200_response_sites_inner_devices_inner_from_dict = V1DevicesSummaryGet200ResponseSitesInnerDevicesInner.from_dict(v1_devices_summary_get200_response_sites_inner_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


