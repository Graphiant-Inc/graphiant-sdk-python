# V1RegionsRegionIdGatewaysGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateways** | [**List[V1RegionsRegionIdGatewaysGetResponseGateway]**](V1RegionsRegionIdGatewaysGetResponseGateway.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_regions_region_id_gateways_get_response import V1RegionsRegionIdGatewaysGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1RegionsRegionIdGatewaysGetResponse from a JSON string
v1_regions_region_id_gateways_get_response_instance = V1RegionsRegionIdGatewaysGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1RegionsRegionIdGatewaysGetResponse.to_json())

# convert the object into a dict
v1_regions_region_id_gateways_get_response_dict = v1_regions_region_id_gateways_get_response_instance.to_dict()
# create an instance of V1RegionsRegionIdGatewaysGetResponse from a dict
v1_regions_region_id_gateways_get_response_from_dict = V1RegionsRegionIdGatewaysGetResponse.from_dict(v1_regions_region_id_gateways_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


