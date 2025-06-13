# V1TroubleshootingEnterprisePostRequestDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_expiry** | **bool** |  | [optional] 
**core_connectivity** | **bool** |  | [optional] 
**core_transitions** | **bool** |  | [optional] 
**cpu** | **bool** |  | [optional] 
**crashes** | **bool** |  | [optional] 
**credit_expiry** | **bool** |  | [optional] 
**disk** | **bool** |  | [optional] 
**fan_speed** | **bool** |  | [optional] 
**license_expiry** | **bool** |  | [optional] 
**memory** | **bool** |  | [optional] 
**odp_connectivity** | **bool** |  | [optional] 
**odp_transitions** | **bool** |  | [optional] 
**sla_performance** | **bool** |  | [optional] 
**t2_connectivity** | **bool** |  | [optional] 
**t2_transitions** | **bool** |  | [optional] 
**temperature** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_enterprise_post_request_dimensions import V1TroubleshootingEnterprisePostRequestDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingEnterprisePostRequestDimensions from a JSON string
v1_troubleshooting_enterprise_post_request_dimensions_instance = V1TroubleshootingEnterprisePostRequestDimensions.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingEnterprisePostRequestDimensions.to_json())

# convert the object into a dict
v1_troubleshooting_enterprise_post_request_dimensions_dict = v1_troubleshooting_enterprise_post_request_dimensions_instance.to_dict()
# create an instance of V1TroubleshootingEnterprisePostRequestDimensions from a dict
v1_troubleshooting_enterprise_post_request_dimensions_from_dict = V1TroubleshootingEnterprisePostRequestDimensions.from_dict(v1_troubleshooting_enterprise_post_request_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


