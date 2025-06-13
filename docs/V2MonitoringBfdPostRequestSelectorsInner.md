# V2MonitoringBfdPostRequestSelectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**if_index** | **int** |  | [optional] 
**peer_address** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_bfd_post_request_selectors_inner import V2MonitoringBfdPostRequestSelectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringBfdPostRequestSelectorsInner from a JSON string
v2_monitoring_bfd_post_request_selectors_inner_instance = V2MonitoringBfdPostRequestSelectorsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringBfdPostRequestSelectorsInner.to_json())

# convert the object into a dict
v2_monitoring_bfd_post_request_selectors_inner_dict = v2_monitoring_bfd_post_request_selectors_inner_instance.to_dict()
# create an instance of V2MonitoringBfdPostRequestSelectorsInner from a dict
v2_monitoring_bfd_post_request_selectors_inner_from_dict = V2MonitoringBfdPostRequestSelectorsInner.from_dict(v2_monitoring_bfd_post_request_selectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


