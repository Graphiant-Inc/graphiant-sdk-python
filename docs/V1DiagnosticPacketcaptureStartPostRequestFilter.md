# V1DiagnosticPacketcaptureStartPostRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**V1DiagnosticPacketcaptureStartPostRequestFilterDestination**](V1DiagnosticPacketcaptureStartPostRequestFilterDestination.md) |  | [optional] 
**dscp** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**source** | [**V1DiagnosticPacketcaptureStartPostRequestFilterDestination**](V1DiagnosticPacketcaptureStartPostRequestFilterDestination.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_packetcapture_start_post_request_filter import V1DiagnosticPacketcaptureStartPostRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPacketcaptureStartPostRequestFilter from a JSON string
v1_diagnostic_packetcapture_start_post_request_filter_instance = V1DiagnosticPacketcaptureStartPostRequestFilter.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPacketcaptureStartPostRequestFilter.to_json())

# convert the object into a dict
v1_diagnostic_packetcapture_start_post_request_filter_dict = v1_diagnostic_packetcapture_start_post_request_filter_instance.to_dict()
# create an instance of V1DiagnosticPacketcaptureStartPostRequestFilter from a dict
v1_diagnostic_packetcapture_start_post_request_filter_from_dict = V1DiagnosticPacketcaptureStartPostRequestFilter.from_dict(v1_diagnostic_packetcapture_start_post_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


