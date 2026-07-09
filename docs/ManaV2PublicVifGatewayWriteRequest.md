# ManaV2PublicVifGatewayWriteRequest


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
from graphiant_sdk.models.mana_v2_public_vif_gateway_write_request import ManaV2PublicVifGatewayWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifGatewayWriteRequest from a JSON string
mana_v2_public_vif_gateway_write_request_instance = ManaV2PublicVifGatewayWriteRequest.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifGatewayWriteRequest.to_json())

# convert the object into a dict
mana_v2_public_vif_gateway_write_request_dict = mana_v2_public_vif_gateway_write_request_instance.to_dict()
# create an instance of ManaV2PublicVifGatewayWriteRequest from a dict
mana_v2_public_vif_gateway_write_request_from_dict = ManaV2PublicVifGatewayWriteRequest.from_dict(mana_v2_public_vif_gateway_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


