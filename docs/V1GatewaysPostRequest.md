# V1GatewaysPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**V1GatewaysPutRequestDetails**](V1GatewaysPutRequestDetails.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_post_request import V1GatewaysPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPostRequest from a JSON string
v1_gateways_post_request_instance = V1GatewaysPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPostRequest.to_json())

# convert the object into a dict
v1_gateways_post_request_dict = v1_gateways_post_request_instance.to_dict()
# create an instance of V1GatewaysPostRequest from a dict
v1_gateways_post_request_from_dict = V1GatewaysPostRequest.from_dict(v1_gateways_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


