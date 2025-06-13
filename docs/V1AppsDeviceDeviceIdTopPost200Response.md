# V1AppsDeviceDeviceIdTopPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps_utilization** | [**List[V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner]**](V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_device_device_id_top_post200_response import V1AppsDeviceDeviceIdTopPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsDeviceDeviceIdTopPost200Response from a JSON string
v1_apps_device_device_id_top_post200_response_instance = V1AppsDeviceDeviceIdTopPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1AppsDeviceDeviceIdTopPost200Response.to_json())

# convert the object into a dict
v1_apps_device_device_id_top_post200_response_dict = v1_apps_device_device_id_top_post200_response_instance.to_dict()
# create an instance of V1AppsDeviceDeviceIdTopPost200Response from a dict
v1_apps_device_device_id_top_post200_response_from_dict = V1AppsDeviceDeviceIdTopPost200Response.from_dict(v1_apps_device_device_id_top_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


