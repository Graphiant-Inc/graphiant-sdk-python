# V1DiagnosticClearArpDeviceIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**List[V1DiagnosticClearArpDeviceIdPutRequestEntryInner]**](V1DiagnosticClearArpDeviceIdPutRequestEntryInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_clear_arp_device_id_put_request import V1DiagnosticClearArpDeviceIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticClearArpDeviceIdPutRequest from a JSON string
v1_diagnostic_clear_arp_device_id_put_request_instance = V1DiagnosticClearArpDeviceIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticClearArpDeviceIdPutRequest.to_json())

# convert the object into a dict
v1_diagnostic_clear_arp_device_id_put_request_dict = v1_diagnostic_clear_arp_device_id_put_request_instance.to_dict()
# create an instance of V1DiagnosticClearArpDeviceIdPutRequest from a dict
v1_diagnostic_clear_arp_device_id_put_request_from_dict = V1DiagnosticClearArpDeviceIdPutRequest.from_dict(v1_diagnostic_clear_arp_device_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


