# V1DiagnosticResetIpsecSessionDeviceIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all3_rd_party** | **bool** |  | [optional] 
**all_controllers** | **bool** |  | [optional] 
**all_e2_e** | **bool** |  | [optional] 
**vrf** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_reset_ipsec_session_device_id_put_request import V1DiagnosticResetIpsecSessionDeviceIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticResetIpsecSessionDeviceIdPutRequest from a JSON string
v1_diagnostic_reset_ipsec_session_device_id_put_request_instance = V1DiagnosticResetIpsecSessionDeviceIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticResetIpsecSessionDeviceIdPutRequest.to_json())

# convert the object into a dict
v1_diagnostic_reset_ipsec_session_device_id_put_request_dict = v1_diagnostic_reset_ipsec_session_device_id_put_request_instance.to_dict()
# create an instance of V1DiagnosticResetIpsecSessionDeviceIdPutRequest from a dict
v1_diagnostic_reset_ipsec_session_device_id_put_request_from_dict = V1DiagnosticResetIpsecSessionDeviceIdPutRequest.from_dict(v1_diagnostic_reset_ipsec_session_device_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


