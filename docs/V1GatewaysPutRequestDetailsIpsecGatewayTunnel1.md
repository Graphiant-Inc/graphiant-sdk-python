# V1GatewaysPutRequestDetailsIpsecGatewayTunnel1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inside_ipv4_cidr** | **str** |  | [optional] 
**inside_ipv6_cidr** | **str** |  | [optional] 
**local_ike_peer_identity** | **str** |  | [optional] 
**psk** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway_tunnel1 import V1GatewaysPutRequestDetailsIpsecGatewayTunnel1

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayTunnel1 from a JSON string
v1_gateways_put_request_details_ipsec_gateway_tunnel1_instance = V1GatewaysPutRequestDetailsIpsecGatewayTunnel1.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsIpsecGatewayTunnel1.to_json())

# convert the object into a dict
v1_gateways_put_request_details_ipsec_gateway_tunnel1_dict = v1_gateways_put_request_details_ipsec_gateway_tunnel1_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayTunnel1 from a dict
v1_gateways_put_request_details_ipsec_gateway_tunnel1_from_dict = V1GatewaysPutRequestDetailsIpsecGatewayTunnel1.from_dict(v1_gateways_put_request_details_ipsec_gateway_tunnel1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


