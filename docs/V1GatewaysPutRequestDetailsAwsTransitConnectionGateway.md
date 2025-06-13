# V1GatewaysPutRequestDetailsAwsTransitConnectionGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**transit_gateways** | [**List[V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner]**](V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_aws_transit_connection_gateway import V1GatewaysPutRequestDetailsAwsTransitConnectionGateway

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnectionGateway from a JSON string
v1_gateways_put_request_details_aws_transit_connection_gateway_instance = V1GatewaysPutRequestDetailsAwsTransitConnectionGateway.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAwsTransitConnectionGateway.to_json())

# convert the object into a dict
v1_gateways_put_request_details_aws_transit_connection_gateway_dict = v1_gateways_put_request_details_aws_transit_connection_gateway_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnectionGateway from a dict
v1_gateways_put_request_details_aws_transit_connection_gateway_from_dict = V1GatewaysPutRequestDetailsAwsTransitConnectionGateway.from_dict(v1_gateways_put_request_details_aws_transit_connection_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


