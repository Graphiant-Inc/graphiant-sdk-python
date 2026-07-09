# ManaV2IPsecGatewayRemotePeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **str** |  | [optional] 
**ike_initiator** | **bool** | When true, Graphiant initiates IKE for this peer | [optional] 
**mtu** | **int** |  | [optional] 
**name** | **str** | Optional display name or label for this peer; used when generating tunnel names | [optional] 
**remote_ike_peer_identity** | **str** | IKE identity of the remote peer | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tunnel1** | [**ManaV2IPsecGatewayTunnelDetails**](ManaV2IPsecGatewayTunnelDetails.md) |  | [optional] 
**tunnel2** | [**ManaV2IPsecGatewayTunnelDetails**](ManaV2IPsecGatewayTunnelDetails.md) |  | [optional] 
**vpn_profile** | **str** | Enterprise IPsec VPN profile name for this peer | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_i_psec_gateway_remote_peer import ManaV2IPsecGatewayRemotePeer

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2IPsecGatewayRemotePeer from a JSON string
mana_v2_i_psec_gateway_remote_peer_instance = ManaV2IPsecGatewayRemotePeer.from_json(json)
# print the JSON string representation of the object
print(ManaV2IPsecGatewayRemotePeer.to_json())

# convert the object into a dict
mana_v2_i_psec_gateway_remote_peer_dict = mana_v2_i_psec_gateway_remote_peer_instance.to_dict()
# create an instance of ManaV2IPsecGatewayRemotePeer from a dict
mana_v2_i_psec_gateway_remote_peer_from_dict = ManaV2IPsecGatewayRemotePeer.from_dict(mana_v2_i_psec_gateway_remote_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


