# ManaV2IPsecGatewayPeersConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the IPsec gateway service | [optional] 
**remote_peers** | [**List[ManaV2IPsecGatewayRemotePeer]**](ManaV2IPsecGatewayRemotePeer.md) |  | [optional] 
**routing** | [**ManaV2IpsecRoutingConfig**](ManaV2IpsecRoutingConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_i_psec_gateway_peers_config import ManaV2IPsecGatewayPeersConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2IPsecGatewayPeersConfig from a JSON string
mana_v2_i_psec_gateway_peers_config_instance = ManaV2IPsecGatewayPeersConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2IPsecGatewayPeersConfig.to_json())

# convert the object into a dict
mana_v2_i_psec_gateway_peers_config_dict = mana_v2_i_psec_gateway_peers_config_instance.to_dict()
# create an instance of ManaV2IPsecGatewayPeersConfig from a dict
mana_v2_i_psec_gateway_peers_config_from_dict = ManaV2IPsecGatewayPeersConfig.from_dict(mana_v2_i_psec_gateway_peers_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


