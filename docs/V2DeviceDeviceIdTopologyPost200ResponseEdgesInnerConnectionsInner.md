# V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**circuit_carrier** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**destination_ip** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**last_established_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**quality** | **str** |  | [optional] 
**source_ip** | **str** |  | [optional] 
**source_public_ip** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_edges_inner_connections_inner import V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner from a JSON string
v2_device_device_id_topology_post200_response_edges_inner_connections_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_edges_inner_connections_inner_dict = v2_device_device_id_topology_post200_response_edges_inner_connections_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner from a dict
v2_device_device_id_topology_post200_response_edges_inner_connections_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner.from_dict(v2_device_device_id_topology_post200_response_edges_inner_connections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


