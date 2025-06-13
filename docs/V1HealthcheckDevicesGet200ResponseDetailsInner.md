# V1HealthcheckDevicesGet200ResponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_core_state** | **List[bool]** |  | [optional] 
**bgp_odp_state** | **List[bool]** |  | [optional] 
**core_tunnel_state** | **List[bool]** |  | [optional] 
**device_id** | **int** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**gnmi_state** | **bool** |  | [optional] 
**ipsec_core_status** | **str** |  | [optional] 
**ipsec_odp_status** | **str** |  | [optional] 
**odp_status** | [**V1HealthcheckDevicesGet200ResponseDetailsInnerOdpStatus**](V1HealthcheckDevicesGet200ResponseDetailsInnerOdpStatus.md) |  | [optional] 
**odp_tunnel_state** | **List[bool]** |  | [optional] 
**onboarding_status** | [**V1HealthcheckDevicesGet200ResponseDetailsInnerOnboardingStatus**](V1HealthcheckDevicesGet200ResponseDetailsInnerOnboardingStatus.md) |  | [optional] 
**t2_status** | [**V1HealthcheckDevicesGet200ResponseDetailsInnerOdpStatus**](V1HealthcheckDevicesGet200ResponseDetailsInnerOdpStatus.md) |  | [optional] 
**topo_gw_state** | **str** |  | [optional] 
**tt_tunnel_state** | **List[bool]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_healthcheck_devices_get200_response_details_inner import V1HealthcheckDevicesGet200ResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1HealthcheckDevicesGet200ResponseDetailsInner from a JSON string
v1_healthcheck_devices_get200_response_details_inner_instance = V1HealthcheckDevicesGet200ResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print(V1HealthcheckDevicesGet200ResponseDetailsInner.to_json())

# convert the object into a dict
v1_healthcheck_devices_get200_response_details_inner_dict = v1_healthcheck_devices_get200_response_details_inner_instance.to_dict()
# create an instance of V1HealthcheckDevicesGet200ResponseDetailsInner from a dict
v1_healthcheck_devices_get200_response_details_inner_from_dict = V1HealthcheckDevicesGet200ResponseDetailsInner.from_dict(v1_healthcheck_devices_get200_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


