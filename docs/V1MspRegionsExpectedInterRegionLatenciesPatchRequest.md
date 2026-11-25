# V1MspRegionsExpectedInterRegionLatenciesPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inter_region_latency_matrix** | [**ManaV2InterRegionLatencyMatrix**](ManaV2InterRegionLatencyMatrix.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_msp_regions_expected_inter_region_latencies_patch_request import V1MspRegionsExpectedInterRegionLatenciesPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1MspRegionsExpectedInterRegionLatenciesPatchRequest from a JSON string
v1_msp_regions_expected_inter_region_latencies_patch_request_instance = V1MspRegionsExpectedInterRegionLatenciesPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1MspRegionsExpectedInterRegionLatenciesPatchRequest.to_json())

# convert the object into a dict
v1_msp_regions_expected_inter_region_latencies_patch_request_dict = v1_msp_regions_expected_inter_region_latencies_patch_request_instance.to_dict()
# create an instance of V1MspRegionsExpectedInterRegionLatenciesPatchRequest from a dict
v1_msp_regions_expected_inter_region_latencies_patch_request_from_dict = V1MspRegionsExpectedInterRegionLatenciesPatchRequest.from_dict(v1_msp_regions_expected_inter_region_latencies_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


