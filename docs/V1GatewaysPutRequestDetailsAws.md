# V1GatewaysPutRequestDetailsAws


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**advance_settings** | [**V1GatewaysPutRequestDetailsAwsAdvanceSettings**](V1GatewaysPutRequestDetailsAwsAdvanceSettings.md) |  | [optional] 
**transit_connection** | [**V1GatewaysPutRequestDetailsAwsTransitConnection**](V1GatewaysPutRequestDetailsAwsTransitConnection.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_aws import V1GatewaysPutRequestDetailsAws

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAws from a JSON string
v1_gateways_put_request_details_aws_instance = V1GatewaysPutRequestDetailsAws.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAws.to_json())

# convert the object into a dict
v1_gateways_put_request_details_aws_dict = v1_gateways_put_request_details_aws_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAws from a dict
v1_gateways_put_request_details_aws_from_dict = V1GatewaysPutRequestDetailsAws.from_dict(v1_gateways_put_request_details_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


