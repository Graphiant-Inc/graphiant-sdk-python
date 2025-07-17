# V1DevicesDeviceIdControllerPeersPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**controller_device_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_controller_peers_put_request import V1DevicesDeviceIdControllerPeersPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdControllerPeersPutRequest from a JSON string
v1_devices_device_id_controller_peers_put_request_instance = V1DevicesDeviceIdControllerPeersPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdControllerPeersPutRequest.to_json())

# convert the object into a dict
v1_devices_device_id_controller_peers_put_request_dict = v1_devices_device_id_controller_peers_put_request_instance.to_dict()
# create an instance of V1DevicesDeviceIdControllerPeersPutRequest from a dict
v1_devices_device_id_controller_peers_put_request_from_dict = V1DevicesDeviceIdControllerPeersPutRequest.from_dict(v1_devices_device_id_controller_peers_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


