# V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_name** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_site_twamp_site_id_post_request_selectors_inner import V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner from a JSON string
v2_monitoring_site_twamp_site_id_post_request_selectors_inner_instance = V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner.to_json())

# convert the object into a dict
v2_monitoring_site_twamp_site_id_post_request_selectors_inner_dict = v2_monitoring_site_twamp_site_id_post_request_selectors_inner_instance.to_dict()
# create an instance of V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner from a dict
v2_monitoring_site_twamp_site_id_post_request_selectors_inner_from_dict = V2MonitoringSiteTwampSiteIdPostRequestSelectorsInner.from_dict(v2_monitoring_site_twamp_site_id_post_request_selectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


