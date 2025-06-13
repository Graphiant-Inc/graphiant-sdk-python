# V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_downlink_utilization** | **float** |  | [optional] 
**average_uplink_utilization** | **float** |  | [optional] 
**circuit_carrier** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**current_downlink_utilization** | **float** |  | [optional] 
**current_uplink_utilization** | **float** |  | [optional] 
**device_id** | **int** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**jitter** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**latency** | **int** |  | [optional] 
**loss** | **float** |  | [optional] 
**qoe** | **float** |  | [optional] 
**quality** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner import V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner from a JSON string
v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner_dict = v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner from a dict
v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseNodesInnerCircuitInfoInner.from_dict(v2_device_device_id_topology_post200_response_nodes_inner_circuit_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


