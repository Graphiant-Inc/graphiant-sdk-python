# V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**vrf_routes** | [**List[V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInnerVrfRoutesInner]**](V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInnerVrfRoutesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_lan_segments_post200_response_device_segments_inner import V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner from a JSON string
v2_device_device_id_lan_segments_post200_response_device_segments_inner_instance = V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner.to_json())

# convert the object into a dict
v2_device_device_id_lan_segments_post200_response_device_segments_inner_dict = v2_device_device_id_lan_segments_post200_response_device_segments_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner from a dict
v2_device_device_id_lan_segments_post200_response_device_segments_inner_from_dict = V2DeviceDeviceIdLanSegmentsPost200ResponseDeviceSegmentsInner.from_dict(v2_device_device_id_lan_segments_post200_response_device_segments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


