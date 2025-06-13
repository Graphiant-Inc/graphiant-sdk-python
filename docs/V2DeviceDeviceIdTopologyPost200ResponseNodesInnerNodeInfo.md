# V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_quality** | **str** |  | [optional] 
**cpu** | **float** |  | [optional] 
**data_quality** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**maintenance_mode** | **bool** |  | [optional] 
**memory** | **float** |  | [optional] 
**mgmt_ip** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**portal_quality** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**staging_mode** | **bool** |  | [optional] 
**temperature** | **float** |  | [optional] 
**uptime** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_nodes_inner_node_info import V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo from a JSON string
v2_device_device_id_topology_post200_response_nodes_inner_node_info_instance = V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_nodes_inner_node_info_dict = v2_device_device_id_topology_post200_response_nodes_inner_node_info_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo from a dict
v2_device_device_id_topology_post200_response_nodes_inner_node_info_from_dict = V2DeviceDeviceIdTopologyPost200ResponseNodesInnerNodeInfo.from_dict(v2_device_device_id_topology_post200_response_nodes_inner_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


