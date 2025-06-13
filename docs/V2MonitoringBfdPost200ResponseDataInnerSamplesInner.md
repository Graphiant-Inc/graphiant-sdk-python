# V2MonitoringBfdPost200ResponseDataInnerSamplesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_bfd_post200_response_data_inner_samples_inner import V2MonitoringBfdPost200ResponseDataInnerSamplesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringBfdPost200ResponseDataInnerSamplesInner from a JSON string
v2_monitoring_bfd_post200_response_data_inner_samples_inner_instance = V2MonitoringBfdPost200ResponseDataInnerSamplesInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringBfdPost200ResponseDataInnerSamplesInner.to_json())

# convert the object into a dict
v2_monitoring_bfd_post200_response_data_inner_samples_inner_dict = v2_monitoring_bfd_post200_response_data_inner_samples_inner_instance.to_dict()
# create an instance of V2MonitoringBfdPost200ResponseDataInnerSamplesInner from a dict
v2_monitoring_bfd_post200_response_data_inner_samples_inner_from_dict = V2MonitoringBfdPost200ResponseDataInnerSamplesInner.from_dict(v2_monitoring_bfd_post200_response_data_inner_samples_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


