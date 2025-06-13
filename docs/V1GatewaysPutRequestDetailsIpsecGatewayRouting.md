# V1GatewaysPutRequestDetailsIpsecGatewayRouting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp**](V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgp.md) |  | [optional] 
**static** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerStatic**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerStatic.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway_routing import V1GatewaysPutRequestDetailsIpsecGatewayRouting

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRouting from a JSON string
v1_gateways_put_request_details_ipsec_gateway_routing_instance = V1GatewaysPutRequestDetailsIpsecGatewayRouting.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsIpsecGatewayRouting.to_json())

# convert the object into a dict
v1_gateways_put_request_details_ipsec_gateway_routing_dict = v1_gateways_put_request_details_ipsec_gateway_routing_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRouting from a dict
v1_gateways_put_request_details_ipsec_gateway_routing_from_dict = V1GatewaysPutRequestDetailsIpsecGatewayRouting.from_dict(v1_gateways_put_request_details_ipsec_gateway_routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


