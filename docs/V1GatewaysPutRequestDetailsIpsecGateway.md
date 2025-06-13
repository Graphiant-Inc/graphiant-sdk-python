# V1GatewaysPutRequestDetailsIpsecGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **str** |  | [optional] 
**ike_initiator** | **bool** |  | [optional] 
**mtu** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**remote_ike_peer_identity** | **str** |  | [optional] 
**routing** | [**V1GatewaysPutRequestDetailsIpsecGatewayRouting**](V1GatewaysPutRequestDetailsIpsecGatewayRouting.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tunnel1** | [**V1GatewaysPutRequestDetailsIpsecGatewayTunnel1**](V1GatewaysPutRequestDetailsIpsecGatewayTunnel1.md) |  | [optional] 
**tunnel2** | [**V1GatewaysPutRequestDetailsIpsecGatewayTunnel1**](V1GatewaysPutRequestDetailsIpsecGatewayTunnel1.md) |  | [optional] 
**vpn_profile** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway import V1GatewaysPutRequestDetailsIpsecGateway

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsIpsecGateway from a JSON string
v1_gateways_put_request_details_ipsec_gateway_instance = V1GatewaysPutRequestDetailsIpsecGateway.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsIpsecGateway.to_json())

# convert the object into a dict
v1_gateways_put_request_details_ipsec_gateway_dict = v1_gateways_put_request_details_ipsec_gateway_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsIpsecGateway from a dict
v1_gateways_put_request_details_ipsec_gateway_from_dict = V1GatewaysPutRequestDetailsIpsecGateway.from_dict(v1_gateways_put_request_details_ipsec_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


