# V1GatewaysPutRequestDetailsAwsAdvanceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** |  | [optional] 
**allowed_prefixes** | **List[str]** |  | [optional] 
**amazon_bgp_router_ip** | **str** |  | [optional] 
**bgp_auth_key** | **str** |  | [optional] 
**customer_bgp_router_ip** | **str** |  | [optional] 
**is_jumbo** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_aws_advance_settings import V1GatewaysPutRequestDetailsAwsAdvanceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAwsAdvanceSettings from a JSON string
v1_gateways_put_request_details_aws_advance_settings_instance = V1GatewaysPutRequestDetailsAwsAdvanceSettings.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAwsAdvanceSettings.to_json())

# convert the object into a dict
v1_gateways_put_request_details_aws_advance_settings_dict = v1_gateways_put_request_details_aws_advance_settings_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAwsAdvanceSettings from a dict
v1_gateways_put_request_details_aws_advance_settings_from_dict = V1GatewaysPutRequestDetailsAwsAdvanceSettings.from_dict(v1_gateways_put_request_details_aws_advance_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


