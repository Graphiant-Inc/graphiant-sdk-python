# V1SoftwareRunningDetailsGet200ResponseDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_running_details_get200_response_devices_inner import V1SoftwareRunningDetailsGet200ResponseDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareRunningDetailsGet200ResponseDevicesInner from a JSON string
v1_software_running_details_get200_response_devices_inner_instance = V1SoftwareRunningDetailsGet200ResponseDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareRunningDetailsGet200ResponseDevicesInner.to_json())

# convert the object into a dict
v1_software_running_details_get200_response_devices_inner_dict = v1_software_running_details_get200_response_devices_inner_instance.to_dict()
# create an instance of V1SoftwareRunningDetailsGet200ResponseDevicesInner from a dict
v1_software_running_details_get200_response_devices_inner_from_dict = V1SoftwareRunningDetailsGet200ResponseDevicesInner.from_dict(v1_software_running_details_get200_response_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


