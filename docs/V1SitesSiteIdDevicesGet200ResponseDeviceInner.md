# V1SitesSiteIdDevicesGet200ResponseDeviceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**maintenance_mode** | **bool** |  | [optional] 
**management_ip** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**software_version** | **str** |  | [optional] 
**staging_mode** | **bool** |  | [optional] 
**uptime** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**vrrp_interface** | **str** |  | [optional] 
**vrrp_state** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_site_id_devices_get200_response_device_inner import V1SitesSiteIdDevicesGet200ResponseDeviceInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesSiteIdDevicesGet200ResponseDeviceInner from a JSON string
v1_sites_site_id_devices_get200_response_device_inner_instance = V1SitesSiteIdDevicesGet200ResponseDeviceInner.from_json(json)
# print the JSON string representation of the object
print(V1SitesSiteIdDevicesGet200ResponseDeviceInner.to_json())

# convert the object into a dict
v1_sites_site_id_devices_get200_response_device_inner_dict = v1_sites_site_id_devices_get200_response_device_inner_instance.to_dict()
# create an instance of V1SitesSiteIdDevicesGet200ResponseDeviceInner from a dict
v1_sites_site_id_devices_get200_response_device_inner_from_dict = V1SitesSiteIdDevicesGet200ResponseDeviceInner.from_dict(v1_sites_site_id_devices_get200_response_device_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


