# V1ExtranetB2bConsumersCustomerIdGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_object_device_summaries** | [**Dict[str, ManaV2GlobalObjectServiceSummaries]**](ManaV2GlobalObjectServiceSummaries.md) |  | [optional] 
**id** | **int** |  | [optional] 
**ipsec_tunnel_config** | [**List[V1ExtranetB2bConsumersCustomerIdGetResponseIpsecVpnTunnelConfig]**](V1ExtranetB2bConsumersCustomerIdGetResponseIpsecVpnTunnelConfig.md) |  | [optional] 
**match_details** | [**ManaV2B2bExtranetMatchConsumerDetails**](ManaV2B2bExtranetMatchConsumerDetails.md) |  | [optional] 
**match_id** | **int** |  | [optional] 
**peer_type** | **str** |  | [optional] 
**policy** | [**ManaV2ExtranetServiceConsumerPolicy**](ManaV2ExtranetServiceConsumerPolicy.md) |  | [optional] 
**site_to_site_vpn** | [**ManaV2GuestConsumerSiteToSiteVpnConfig**](ManaV2GuestConsumerSiteToSiteVpnConfig.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_consumers_customer_id_get_response import V1ExtranetB2bConsumersCustomerIdGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bConsumersCustomerIdGetResponse from a JSON string
v1_extranet_b2b_consumers_customer_id_get_response_instance = V1ExtranetB2bConsumersCustomerIdGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bConsumersCustomerIdGetResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_consumers_customer_id_get_response_dict = v1_extranet_b2b_consumers_customer_id_get_response_instance.to_dict()
# create an instance of V1ExtranetB2bConsumersCustomerIdGetResponse from a dict
v1_extranet_b2b_consumers_customer_id_get_response_from_dict = V1ExtranetB2bConsumersCustomerIdGetResponse.from_dict(v1_extranet_b2b_consumers_customer_id_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


