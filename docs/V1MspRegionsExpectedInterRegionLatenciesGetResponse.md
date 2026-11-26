# V1MspRegionsExpectedInterRegionLatenciesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inter_region_latency_matrix** | [**ManaV2InterRegionLatencyMatrix**](ManaV2InterRegionLatencyMatrix.md) |  | [optional] 
**source_region_missing_destinations** | [**Dict[str, V1MspRegionsExpectedInterRegionLatenciesGetResponseMissingDestinationRegions]**](V1MspRegionsExpectedInterRegionLatenciesGetResponseMissingDestinationRegions.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_msp_regions_expected_inter_region_latencies_get_response import V1MspRegionsExpectedInterRegionLatenciesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1MspRegionsExpectedInterRegionLatenciesGetResponse from a JSON string
v1_msp_regions_expected_inter_region_latencies_get_response_instance = V1MspRegionsExpectedInterRegionLatenciesGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1MspRegionsExpectedInterRegionLatenciesGetResponse.to_json())

# convert the object into a dict
v1_msp_regions_expected_inter_region_latencies_get_response_dict = v1_msp_regions_expected_inter_region_latencies_get_response_instance.to_dict()
# create an instance of V1MspRegionsExpectedInterRegionLatenciesGetResponse from a dict
v1_msp_regions_expected_inter_region_latencies_get_response_from_dict = V1MspRegionsExpectedInterRegionLatenciesGetResponse.from_dict(v1_msp_regions_expected_inter_region_latencies_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


