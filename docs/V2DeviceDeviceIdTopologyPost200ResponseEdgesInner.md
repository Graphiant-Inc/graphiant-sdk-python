# V2DeviceDeviceIdTopologyPost200ResponseEdgesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a** | **int** |  | [optional] 
**b** | **int** |  | [optional] 
**circuits_info** | [**List[V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner]**](V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerCircuitsInfoInner.md) |  | [optional] 
**connections** | [**List[V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner]**](V2DeviceDeviceIdTopologyPost200ResponseEdgesInnerConnectionsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**quality** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_edges_inner import V2DeviceDeviceIdTopologyPost200ResponseEdgesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInner from a JSON string
v2_device_device_id_topology_post200_response_edges_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseEdgesInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseEdgesInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_edges_inner_dict = v2_device_device_id_topology_post200_response_edges_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseEdgesInner from a dict
v2_device_device_id_topology_post200_response_edges_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseEdgesInner.from_dict(v2_device_device_id_topology_post200_response_edges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


