# V2MonitoringSystemGenericPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[V2MonitoringBfdPost200ResponseDataInnerSamplesInner]**](V2MonitoringBfdPost200ResponseDataInnerSamplesInner.md) |  | [optional] 
**selector** | [**V1AccountMfaGet200Response**](V1AccountMfaGet200Response.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_system_generic_post200_response_data_inner import V2MonitoringSystemGenericPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringSystemGenericPost200ResponseDataInner from a JSON string
v2_monitoring_system_generic_post200_response_data_inner_instance = V2MonitoringSystemGenericPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringSystemGenericPost200ResponseDataInner.to_json())

# convert the object into a dict
v2_monitoring_system_generic_post200_response_data_inner_dict = v2_monitoring_system_generic_post200_response_data_inner_instance.to_dict()
# create an instance of V2MonitoringSystemGenericPost200ResponseDataInner from a dict
v2_monitoring_system_generic_post200_response_data_inner_from_dict = V2MonitoringSystemGenericPost200ResponseDataInner.from_dict(v2_monitoring_system_generic_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


