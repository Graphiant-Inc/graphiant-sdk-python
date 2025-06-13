# V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | [**Dict[str, V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValue]**](V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValue.md) |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**keepalive_timer** | **int** |  | [optional] 
**md5_password** | [**V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpMd5Password**](V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpMd5Password.md) |  | [optional] 
**peer_asn** | **int** |  | [optional] 
**send_community** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway_routing_bgp import V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp from a JSON string
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_instance = V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp.to_json())

# convert the object into a dict
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_dict = v1_gateways_put_request_details_ipsec_gateway_routing_bgp_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp from a dict
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_from_dict = V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp.from_dict(v1_gateways_put_request_details_ipsec_gateway_routing_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


