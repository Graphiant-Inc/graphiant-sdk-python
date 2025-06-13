# V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**vpcs** | [**List[V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInner]**](V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner import V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner from a JSON string
v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_instance = V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner.to_json())

# convert the object into a dict
v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_dict = v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner from a dict
v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_from_dict = V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner.from_dict(v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


