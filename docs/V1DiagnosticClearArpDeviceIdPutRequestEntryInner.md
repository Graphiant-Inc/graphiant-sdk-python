# V1DiagnosticClearArpDeviceIdPutRequestEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**V1DiagnosticClearArpDeviceIdPutRequestEntryInnerAddress**](V1DiagnosticClearArpDeviceIdPutRequestEntryInnerAddress.md) |  | [optional] 
**all_entry** | **bool** |  | [optional] 
**interface_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_clear_arp_device_id_put_request_entry_inner import V1DiagnosticClearArpDeviceIdPutRequestEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticClearArpDeviceIdPutRequestEntryInner from a JSON string
v1_diagnostic_clear_arp_device_id_put_request_entry_inner_instance = V1DiagnosticClearArpDeviceIdPutRequestEntryInner.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticClearArpDeviceIdPutRequestEntryInner.to_json())

# convert the object into a dict
v1_diagnostic_clear_arp_device_id_put_request_entry_inner_dict = v1_diagnostic_clear_arp_device_id_put_request_entry_inner_instance.to_dict()
# create an instance of V1DiagnosticClearArpDeviceIdPutRequestEntryInner from a dict
v1_diagnostic_clear_arp_device_id_put_request_entry_inner_from_dict = V1DiagnosticClearArpDeviceIdPutRequestEntryInner.from_dict(v1_diagnostic_clear_arp_device_id_put_request_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


