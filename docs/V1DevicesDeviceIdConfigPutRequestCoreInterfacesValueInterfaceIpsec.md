# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_replay_window_size** | **int** |  | [optional] 
**dh_group** | **str** |  | [optional] 
**dpd_interval** | **int** |  | [optional] 
**encryption_alg** | **str** |  | [optional] 
**esn** | **bool** |  | [optional] 
**ike_integrity** | **str** |  | [optional] 
**initiator** | **bool** |  | [optional] 
**ipsec_encryption_alg** | **str** |  | [optional] 
**ipsec_integrity** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**local_address** | **str** |  | [optional] 
**local_circuit** | **str** |  | [optional] 
**local_ike_peer_identity** | **str** |  | [optional] 
**perfect_forward_secrecy** | **str** |  | [optional] 
**preshared_key** | **str** |  | [optional] 
**reauth_interval** | **int** |  | [optional] 
**rekey_interval** | **int** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remote_ike_peer_identity** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


