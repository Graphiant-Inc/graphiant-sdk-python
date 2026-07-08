# V1PvifPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisement** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | [optional] 
**consumer_lan_segments** | [**Dict[str, ManaV2PublicVifGatewayConsumerLanDevices]**](ManaV2PublicVifGatewayConsumerLanDevices.md) |  | 
**covering_prefixes** | **List[str]** |  | [optional] 
**gateway_bgp_neighbors** | [**Dict[str, ManaV2BgpNeighborConfig]**](ManaV2BgpNeighborConfig.md) |  | 
**lan_segment_id** | **int** | Producer LAN segment (VRF) on gateway appliances (required) | 
**nat_prefix_strategy** | [**ManaV2PublicVifGatewayNatPrefixStrategy**](ManaV2PublicVifGatewayNatPrefixStrategy.md) |  | 
**region_id** | **int** | Graphiant region for gateway appliances (required) | 
**service_name** | **str** | Service display name (required) | 
**storage_provider** | **str** | Storage provider; each gateway appliance must match region and provider (required) | 

## Example

```python
from graphiant_sdk.models.v1_pvif_post_request import V1PvifPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PvifPostRequest from a JSON string
v1_pvif_post_request_instance = V1PvifPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1PvifPostRequest.to_json())

# convert the object into a dict
v1_pvif_post_request_dict = v1_pvif_post_request_instance.to_dict()
# create an instance of V1PvifPostRequest from a dict
v1_pvif_post_request_from_dict = V1PvifPostRequest.from_dict(v1_pvif_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


