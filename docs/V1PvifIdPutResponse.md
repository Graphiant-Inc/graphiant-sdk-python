# V1PvifIdPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_all_sites** | **bool** | True when consumer scope is all symmetric sites (snapshotted on create and update); false when advertisement lists explicit sites or site lists | [optional] 
**advertisement** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | [optional] 
**consumer_lan_segments** | [**Dict[str, ManaV2PublicVifGatewayConsumerLanDevices]**](ManaV2PublicVifGatewayConsumerLanDevices.md) |  | [optional] 
**covering_prefixes** | **List[str]** |  | [optional] 
**gateway_bgp_neighbors** | [**Dict[str, ManaV2BgpNeighbor]**](ManaV2BgpNeighbor.md) |  | [optional] 
**id** | **int** | Producer service id | [optional] 
**lan_segment_id** | **int** | Producer LAN segment (VRF) id | [optional] 
**nat_prefix_strategy** | [**ManaV2PublicVifGatewayNatPrefixStrategy**](ManaV2PublicVifGatewayNatPrefixStrategy.md) |  | [optional] 
**region_id** | **int** | Graphiant region for gateway appliances | [optional] 
**service_name** | **str** | Service display name | [optional] 
**storage_provider** | **str** | Storage provider for gateway appliances | [optional] 

## Example

```python
from graphiant_sdk.models.v1_pvif_id_put_response import V1PvifIdPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1PvifIdPutResponse from a JSON string
v1_pvif_id_put_response_instance = V1PvifIdPutResponse.from_json(json)
# print the JSON string representation of the object
print(V1PvifIdPutResponse.to_json())

# convert the object into a dict
v1_pvif_id_put_response_dict = v1_pvif_id_put_response_instance.to_dict()
# create an instance of V1PvifIdPutResponse from a dict
v1_pvif_id_put_response_from_dict = V1PvifIdPutResponse.from_dict(v1_pvif_id_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


