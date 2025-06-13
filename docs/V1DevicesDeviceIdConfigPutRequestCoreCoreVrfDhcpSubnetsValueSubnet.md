# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_lease_time_secs** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**domain_name_server** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerNameservers**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerNameservers.md) |  | [optional] 
**interface** | **str** |  | [optional] 
**ip_gateway** | **str** |  | [optional] 
**ip_prefix** | **str** |  | [optional] 
**ip_ranges** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerRangesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerRangesInner.md) |  | [optional] 
**ip_ranges_v2** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnetIpRangesV2**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnetIpRangesV2.md) |  | [optional] 
**max_lease_time_secs** | **int** |  | [optional] 
**min_lease_time_secs** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**static_leases** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnetStaticLeasesValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnetStaticLeasesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet_dict = v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet from a dict
v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfDhcpSubnetsValueSubnet.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_dhcp_subnets_value_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


