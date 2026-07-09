# ManaV2GuestConsumerSiteToSiteVpnConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** |  | [optional] 
**ipsec_gateway_details** | [**ManaV2IPsecGatewayDetails**](ManaV2IPsecGatewayDetails.md) |  | [optional] 
**ipsec_gateway_peers** | [**ManaV2IPsecGatewayPeersConfig**](ManaV2IPsecGatewayPeersConfig.md) |  | [optional] 
**region_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_guest_consumer_site_to_site_vpn_config import ManaV2GuestConsumerSiteToSiteVpnConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2GuestConsumerSiteToSiteVpnConfig from a JSON string
mana_v2_guest_consumer_site_to_site_vpn_config_instance = ManaV2GuestConsumerSiteToSiteVpnConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2GuestConsumerSiteToSiteVpnConfig.to_json())

# convert the object into a dict
mana_v2_guest_consumer_site_to_site_vpn_config_dict = mana_v2_guest_consumer_site_to_site_vpn_config_instance.to_dict()
# create an instance of ManaV2GuestConsumerSiteToSiteVpnConfig from a dict
mana_v2_guest_consumer_site_to_site_vpn_config_from_dict = ManaV2GuestConsumerSiteToSiteVpnConfig.from_dict(mana_v2_guest_consumer_site_to_site_vpn_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


