# V2MonitoringPolicyPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[V2MonitoringPolicyPost200ResponseDataInner]**](V2MonitoringPolicyPost200ResponseDataInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_policy_post200_response import V2MonitoringPolicyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringPolicyPost200Response from a JSON string
v2_monitoring_policy_post200_response_instance = V2MonitoringPolicyPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringPolicyPost200Response.to_json())

# convert the object into a dict
v2_monitoring_policy_post200_response_dict = v2_monitoring_policy_post200_response_instance.to_dict()
# create an instance of V2MonitoringPolicyPost200Response from a dict
v2_monitoring_policy_post200_response_from_dict = V2MonitoringPolicyPost200Response.from_dict(v2_monitoring_policy_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


