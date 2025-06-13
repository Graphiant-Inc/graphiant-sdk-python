# V1GatewaysPutRequestDetailsAwsTransitConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**V1GatewaysPutRequestDetailsAwsTransitConnectionCredentials**](V1GatewaysPutRequestDetailsAwsTransitConnectionCredentials.md) |  | [optional] 
**customer_asn** | **int** |  | [optional] 
**gateway** | [**V1GatewaysPutRequestDetailsAwsTransitConnectionGateway**](V1GatewaysPutRequestDetailsAwsTransitConnectionGateway.md) |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_aws_transit_connection import V1GatewaysPutRequestDetailsAwsTransitConnection

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnection from a JSON string
v1_gateways_put_request_details_aws_transit_connection_instance = V1GatewaysPutRequestDetailsAwsTransitConnection.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAwsTransitConnection.to_json())

# convert the object into a dict
v1_gateways_put_request_details_aws_transit_connection_dict = v1_gateways_put_request_details_aws_transit_connection_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAwsTransitConnection from a dict
v1_gateways_put_request_details_aws_transit_connection_from_dict = V1GatewaysPutRequestDetailsAwsTransitConnection.from_dict(v1_gateways_put_request_details_aws_transit_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


