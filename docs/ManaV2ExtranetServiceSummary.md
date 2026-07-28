# ManaV2ExtranetServiceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**id** | **int** |  | [optional] 
**is_publisher** | **bool** | True when this enterprise publishes the service; false when consuming a remote producer | [optional] 
**lan_segment** | **int** | Service LAN segment when is_publisher and VRF exists | [optional] 
**last_updated** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**server_prefixes** | **List[str]** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**sites** | **List[int]** |  | [optional] 
**status** | **str** |  | [optional] 
**total_customers** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_summary import ManaV2ExtranetServiceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceSummary from a JSON string
mana_v2_extranet_service_summary_instance = ManaV2ExtranetServiceSummary.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceSummary.to_json())

# convert the object into a dict
mana_v2_extranet_service_summary_dict = mana_v2_extranet_service_summary_instance.to_dict()
# create an instance of ManaV2ExtranetServiceSummary from a dict
mana_v2_extranet_service_summary_from_dict = ManaV2ExtranetServiceSummary.from_dict(mana_v2_extranet_service_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


