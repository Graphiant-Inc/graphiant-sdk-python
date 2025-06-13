# V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** |  | [optional] 
**inbound_policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy.md) |  | [optional] 
**outbound_policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family import V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily from a JSON string
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family_instance = V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily.to_json())

# convert the object into a dict
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family_dict = v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily from a dict
v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family_from_dict = V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValueFamily.from_dict(v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


