# V2MonitoringBgpPostRequestSelectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_address** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vrf** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_bgp_post_request_selectors_inner import V2MonitoringBgpPostRequestSelectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringBgpPostRequestSelectorsInner from a JSON string
v2_monitoring_bgp_post_request_selectors_inner_instance = V2MonitoringBgpPostRequestSelectorsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringBgpPostRequestSelectorsInner.to_json())

# convert the object into a dict
v2_monitoring_bgp_post_request_selectors_inner_dict = v2_monitoring_bgp_post_request_selectors_inner_instance.to_dict()
# create an instance of V2MonitoringBgpPostRequestSelectorsInner from a dict
v2_monitoring_bgp_post_request_selectors_inner_from_dict = V2MonitoringBgpPostRequestSelectorsInner.from_dict(v2_monitoring_bgp_post_request_selectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


