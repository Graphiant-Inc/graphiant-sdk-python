# V2ChildalertlistPost200ResponseAlertListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged_list** | **List[str]** |  | [optional] 
**acknowledgement_reason** | **str** |  | [optional] 
**alert_body** | **str** |  | [optional] 
**alert_id** | **str** |  | [optional] 
**allow_listed** | **bool** |  | [optional] 
**children_alert_list** | [**V2ChildalertlistPost200ResponseAlertListInnerChildrenAlertList**](V2ChildalertlistPost200ResponseAlertListInnerChildrenAlertList.md) |  | [optional] 
**descendant_present** | **bool** |  | [optional] 
**device_id** | **str** |  | [optional] 
**end_time** | **int** |  | [optional] 
**enterprise_id** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**mute_listed** | **bool** |  | [optional] 
**notification_created** | **bool** |  | [optional] 
**occurrences** | **int** |  | [optional] 
**peer_device_id** | **str** |  | [optional] 
**peer_interface_name** | **str** |  | [optional] 
**peer_name** | **str** |  | [optional] 
**plane** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**troubleshooting_disabled_reason** | **str** |  | [optional] 
**troubleshooting_enabled** | **bool** |  | [optional] 
**tunnel_interface_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_childalertlist_post200_response_alert_list_inner import V2ChildalertlistPost200ResponseAlertListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2ChildalertlistPost200ResponseAlertListInner from a JSON string
v2_childalertlist_post200_response_alert_list_inner_instance = V2ChildalertlistPost200ResponseAlertListInner.from_json(json)
# print the JSON string representation of the object
print(V2ChildalertlistPost200ResponseAlertListInner.to_json())

# convert the object into a dict
v2_childalertlist_post200_response_alert_list_inner_dict = v2_childalertlist_post200_response_alert_list_inner_instance.to_dict()
# create an instance of V2ChildalertlistPost200ResponseAlertListInner from a dict
v2_childalertlist_post200_response_alert_list_inner_from_dict = V2ChildalertlistPost200ResponseAlertListInner.from_dict(v2_childalertlist_post200_response_alert_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


