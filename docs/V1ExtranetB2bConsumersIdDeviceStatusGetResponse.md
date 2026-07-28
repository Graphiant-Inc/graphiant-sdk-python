# V1ExtranetB2bConsumersIdDeviceStatusGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_status** | **str** |  | [optional] 
**summary** | [**List[ManaV2B2bExtranetStatusSummary]**](ManaV2B2bExtranetStatusSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_consumers_id_device_status_get_response import V1ExtranetB2bConsumersIdDeviceStatusGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bConsumersIdDeviceStatusGetResponse from a JSON string
v1_extranet_b2b_consumers_id_device_status_get_response_instance = V1ExtranetB2bConsumersIdDeviceStatusGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bConsumersIdDeviceStatusGetResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_consumers_id_device_status_get_response_dict = v1_extranet_b2b_consumers_id_device_status_get_response_instance.to_dict()
# create an instance of V1ExtranetB2bConsumersIdDeviceStatusGetResponse from a dict
v1_extranet_b2b_consumers_id_device_status_get_response_from_dict = V1ExtranetB2bConsumersIdDeviceStatusGetResponse.from_dict(v1_extranet_b2b_consumers_id_device_status_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


