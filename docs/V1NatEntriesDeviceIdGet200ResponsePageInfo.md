# V1NatEntriesDeviceIdGet200ResponsePageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**end_cursor** | **str** |  | [optional] 
**has_next_page** | **bool** |  | [optional] 
**has_prev_page** | **bool** |  | [optional] 
**start_cursor** | **str** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_records** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_nat_entries_device_id_get200_response_page_info import V1NatEntriesDeviceIdGet200ResponsePageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1NatEntriesDeviceIdGet200ResponsePageInfo from a JSON string
v1_nat_entries_device_id_get200_response_page_info_instance = V1NatEntriesDeviceIdGet200ResponsePageInfo.from_json(json)
# print the JSON string representation of the object
print(V1NatEntriesDeviceIdGet200ResponsePageInfo.to_json())

# convert the object into a dict
v1_nat_entries_device_id_get200_response_page_info_dict = v1_nat_entries_device_id_get200_response_page_info_instance.to_dict()
# create an instance of V1NatEntriesDeviceIdGet200ResponsePageInfo from a dict
v1_nat_entries_device_id_get200_response_page_info_from_dict = V1NatEntriesDeviceIdGet200ResponsePageInfo.from_dict(v1_nat_entries_device_id_get200_response_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


