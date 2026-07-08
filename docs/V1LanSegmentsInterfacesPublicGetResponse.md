# V1LanSegmentsInterfacesPublicGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_segment_ids** | [**Dict[str, ManaV2LanSegmentPublicInterfacesLists]**](ManaV2LanSegmentPublicInterfacesLists.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_lan_segments_interfaces_public_get_response import V1LanSegmentsInterfacesPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1LanSegmentsInterfacesPublicGetResponse from a JSON string
v1_lan_segments_interfaces_public_get_response_instance = V1LanSegmentsInterfacesPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1LanSegmentsInterfacesPublicGetResponse.to_json())

# convert the object into a dict
v1_lan_segments_interfaces_public_get_response_dict = v1_lan_segments_interfaces_public_get_response_instance.to_dict()
# create an instance of V1LanSegmentsInterfacesPublicGetResponse from a dict
v1_lan_segments_interfaces_public_get_response_from_dict = V1LanSegmentsInterfacesPublicGetResponse.from_dict(v1_lan_segments_interfaces_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


