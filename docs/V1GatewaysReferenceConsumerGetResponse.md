# V1GatewaysReferenceConsumerGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipsec_gateway_details** | [**ManaV2IPsecGatewayDetails**](ManaV2IPsecGatewayDetails.md) |  | [optional] 
**ipsec_gateway_peers** | [**ManaV2IPsecGatewayPeersConfig**](ManaV2IPsecGatewayPeersConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_reference_consumer_get_response import V1GatewaysReferenceConsumerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysReferenceConsumerGetResponse from a JSON string
v1_gateways_reference_consumer_get_response_instance = V1GatewaysReferenceConsumerGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysReferenceConsumerGetResponse.to_json())

# convert the object into a dict
v1_gateways_reference_consumer_get_response_dict = v1_gateways_reference_consumer_get_response_instance.to_dict()
# create an instance of V1GatewaysReferenceConsumerGetResponse from a dict
v1_gateways_reference_consumer_get_response_from_dict = V1GatewaysReferenceConsumerGetResponse.from_dict(v1_gateways_reference_consumer_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


