# V1NatEntriesDeviceIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_entries** | [**List[V1NatEntriesDeviceIdGet200ResponseNatEntriesInner]**](V1NatEntriesDeviceIdGet200ResponseNatEntriesInner.md) |  | [optional] 
**page_info** | [**V1NatEntriesDeviceIdGet200ResponsePageInfo**](V1NatEntriesDeviceIdGet200ResponsePageInfo.md) |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_nat_entries_device_id_get200_response import V1NatEntriesDeviceIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1NatEntriesDeviceIdGet200Response from a JSON string
v1_nat_entries_device_id_get200_response_instance = V1NatEntriesDeviceIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1NatEntriesDeviceIdGet200Response.to_json())

# convert the object into a dict
v1_nat_entries_device_id_get200_response_dict = v1_nat_entries_device_id_get200_response_instance.to_dict()
# create an instance of V1NatEntriesDeviceIdGet200Response from a dict
v1_nat_entries_device_id_get200_response_from_dict = V1NatEntriesDeviceIdGet200Response.from_dict(v1_nat_entries_device_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


