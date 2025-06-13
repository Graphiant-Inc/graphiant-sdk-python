# V2DeviceDeviceIdTopologyPost200ResponseNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_info** | [**List[V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner]**](V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner.md) |  | [optional] 
**connections** | [**List[V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner]**](V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**node_info** | [**V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo**](V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo.md) |  | [optional] 
**quality** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_nodes_inner import V2DeviceDeviceIdTopologyPost200ResponseNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInner from a JSON string
v2_device_device_id_topology_post200_response_nodes_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseNodesInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseNodesInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_nodes_inner_dict = v2_device_device_id_topology_post200_response_nodes_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInner from a dict
v2_device_device_id_topology_post200_response_nodes_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseNodesInner.from_dict(v2_device_device_id_topology_post200_response_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


