# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | **List[str]** |  | [optional] 
**admin_distance** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAdminDistance**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAdminDistance.md) |  | [optional] 
**areas** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValue.md) |  | [optional] 
**auto** | **bool** |  | [optional] 
**default_originate** | **str** |  | [optional] 
**manual** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**redistribution** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessRedistributionValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessRedistributionValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_dict = v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process from a dict
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2Process.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


