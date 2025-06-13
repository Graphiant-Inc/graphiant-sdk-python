# V1GlobalLanSegmentsVrfIdDevicesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[V1GlobalLanSegmentsVrfIdDevicesGet200ResponseEntriesInner]**](V1GlobalLanSegmentsVrfIdDevicesGet200ResponseEntriesInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_lan_segments_vrf_id_devices_get200_response import V1GlobalLanSegmentsVrfIdDevicesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalLanSegmentsVrfIdDevicesGet200Response from a JSON string
v1_global_lan_segments_vrf_id_devices_get200_response_instance = V1GlobalLanSegmentsVrfIdDevicesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1GlobalLanSegmentsVrfIdDevicesGet200Response.to_json())

# convert the object into a dict
v1_global_lan_segments_vrf_id_devices_get200_response_dict = v1_global_lan_segments_vrf_id_devices_get200_response_instance.to_dict()
# create an instance of V1GlobalLanSegmentsVrfIdDevicesGet200Response from a dict
v1_global_lan_segments_vrf_id_devices_get200_response_from_dict = V1GlobalLanSegmentsVrfIdDevicesGet200Response.from_dict(v1_global_lan_segments_vrf_id_devices_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


