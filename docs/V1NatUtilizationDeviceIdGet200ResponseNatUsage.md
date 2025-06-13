# V1NatUtilizationDeviceIdGet200ResponseNatUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_count** | **int** |  | [optional] 
**current_count_extranet** | **int** |  | [optional] 
**current_count_pat** | **int** |  | [optional] 
**current_count_static** | **int** |  | [optional] 
**max_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_nat_utilization_device_id_get200_response_nat_usage import V1NatUtilizationDeviceIdGet200ResponseNatUsage

# TODO update the JSON string below
json = "{}"
# create an instance of V1NatUtilizationDeviceIdGet200ResponseNatUsage from a JSON string
v1_nat_utilization_device_id_get200_response_nat_usage_instance = V1NatUtilizationDeviceIdGet200ResponseNatUsage.from_json(json)
# print the JSON string representation of the object
print(V1NatUtilizationDeviceIdGet200ResponseNatUsage.to_json())

# convert the object into a dict
v1_nat_utilization_device_id_get200_response_nat_usage_dict = v1_nat_utilization_device_id_get200_response_nat_usage_instance.to_dict()
# create an instance of V1NatUtilizationDeviceIdGet200ResponseNatUsage from a dict
v1_nat_utilization_device_id_get200_response_nat_usage_from_dict = V1NatUtilizationDeviceIdGet200ResponseNatUsage.from_dict(v1_nat_utilization_device_id_get200_response_nat_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


