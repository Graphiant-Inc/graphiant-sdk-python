# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_distance** | **int** |  | [optional] 
**administrative_distance** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAdministrativeDistance**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAdministrativeDistance.md) |  | [optional] 
**description** | **str** |  | [optional] 
**destination_prefix** | **str** |  | [optional] 
**ip_version** | **int** |  | [optional] 
**next_hop** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRouteNextHop**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRouteNextHop.md) |  | [optional] 
**next_hops** | [**List[V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRouteNextHop]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRouteNextHop.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route_dict = v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute from a dict
v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValueRoute.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_static_routes_value_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


