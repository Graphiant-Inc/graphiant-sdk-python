# V2DeviceDeviceIdTopologyPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[V2DeviceDeviceIdTopologyPost200ResponseEdgesInner]**](V2DeviceDeviceIdTopologyPost200ResponseEdgesInner.md) |  | [optional] 
**nodes** | [**List[V2DeviceDeviceIdTopologyPost200ResponseNodesInner]**](V2DeviceDeviceIdTopologyPost200ResponseNodesInner.md) |  | [optional] 
**snapshots** | [**List[V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner]**](V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response import V2DeviceDeviceIdTopologyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200Response from a JSON string
v2_device_device_id_topology_post200_response_instance = V2DeviceDeviceIdTopologyPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200Response.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_dict = v2_device_device_id_topology_post200_response_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200Response from a dict
v2_device_device_id_topology_post200_response_from_dict = V2DeviceDeviceIdTopologyPost200Response.from_dict(v2_device_device_id_topology_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


