# ManaV2InterRegionLatencyMatrix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_region_latencies** | [**Dict[str, ManaV2DestinationRegionLatencies]**](ManaV2DestinationRegionLatencies.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_inter_region_latency_matrix import ManaV2InterRegionLatencyMatrix

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2InterRegionLatencyMatrix from a JSON string
mana_v2_inter_region_latency_matrix_instance = ManaV2InterRegionLatencyMatrix.from_json(json)
# print the JSON string representation of the object
print(ManaV2InterRegionLatencyMatrix.to_json())

# convert the object into a dict
mana_v2_inter_region_latency_matrix_dict = mana_v2_inter_region_latency_matrix_instance.to_dict()
# create an instance of ManaV2InterRegionLatencyMatrix from a dict
mana_v2_inter_region_latency_matrix_from_dict = ManaV2InterRegionLatencyMatrix.from_dict(mana_v2_inter_region_latency_matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


