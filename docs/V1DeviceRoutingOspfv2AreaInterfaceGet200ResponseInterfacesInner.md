# V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bdr_ip_addr** | **str** |  | [optional] 
**bdr_router_id** | **str** |  | [optional] 
**dr_ip_addr** | **str** |  | [optional] 
**dr_router_id** | **str** |  | [optional] 
**hello_interval** | **str** |  | [optional] 
**hello_timer** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**neighbors** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 
**wait_timer** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner import V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner from a JSON string
v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner_instance = V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner_dict = v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner from a dict
v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner_from_dict = V1DeviceRoutingOspfv2AreaInterfaceGet200ResponseInterfacesInner.from_dict(v1_device_routing_ospfv2_area_interface_get200_response_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


