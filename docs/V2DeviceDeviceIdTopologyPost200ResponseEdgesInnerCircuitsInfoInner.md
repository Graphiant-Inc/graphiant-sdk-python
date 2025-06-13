# V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_carrier** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**device_hostname** | **str** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**last_resort_circuit** | **bool** |  | [optional] 
**quality** | **str** |  | [optional] 
**source_ip** | **str** |  | [optional] 
**source_public_ip** | **str** |  | [optional] 
**uptime** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner import V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner from a JSON string
v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner_dict = v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner from a dict
v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner.from_dict(v2_device_device_id_topology_post200_response_edges_inner_circuits_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


