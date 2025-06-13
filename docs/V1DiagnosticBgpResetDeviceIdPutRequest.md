# V1DiagnosticBgpResetDeviceIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **bool** |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**local_interface** | **str** |  | [optional] 
**neighbor** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_bgp_reset_device_id_put_request import V1DiagnosticBgpResetDeviceIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticBgpResetDeviceIdPutRequest from a JSON string
v1_diagnostic_bgp_reset_device_id_put_request_instance = V1DiagnosticBgpResetDeviceIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticBgpResetDeviceIdPutRequest.to_json())

# convert the object into a dict
v1_diagnostic_bgp_reset_device_id_put_request_dict = v1_diagnostic_bgp_reset_device_id_put_request_instance.to_dict()
# create an instance of V1DiagnosticBgpResetDeviceIdPutRequest from a dict
v1_diagnostic_bgp_reset_device_id_put_request_from_dict = V1DiagnosticBgpResetDeviceIdPutRequest.from_dict(v1_diagnostic_bgp_reset_device_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


