# V2MonitoringOspfPostRequestSelectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**router_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vrf** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_ospf_post_request_selectors_inner import V2MonitoringOspfPostRequestSelectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringOspfPostRequestSelectorsInner from a JSON string
v2_monitoring_ospf_post_request_selectors_inner_instance = V2MonitoringOspfPostRequestSelectorsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringOspfPostRequestSelectorsInner.to_json())

# convert the object into a dict
v2_monitoring_ospf_post_request_selectors_inner_dict = v2_monitoring_ospf_post_request_selectors_inner_instance.to_dict()
# create an instance of V2MonitoringOspfPostRequestSelectorsInner from a dict
v2_monitoring_ospf_post_request_selectors_inner_from_dict = V2MonitoringOspfPostRequestSelectorsInner.from_dict(v2_monitoring_ospf_post_request_selectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


