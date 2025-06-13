# V1ExtranetsB2bConsumerPostRequestSiteInformationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bw_allocation_site_lists** | **int** |  | [optional] 
**bw_allocation_sites** | **int** |  | [optional] 
**policer_site_lists** | [**V1ExtranetsB2bConsumerPostRequestSiteInformationInnerPolicerSiteLists**](V1ExtranetsB2bConsumerPostRequestSiteInformationInnerPolicerSiteLists.md) |  | [optional] 
**policer_sites** | [**V1ExtranetsB2bConsumerPostRequestSiteInformationInnerPolicerSiteLists**](V1ExtranetsB2bConsumerPostRequestSiteInformationInnerPolicerSiteLists.md) |  | [optional] 
**site_lists** | **List[int]** |  | [optional] 
**sites** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post_request_site_information_inner import V1ExtranetsB2bConsumerPostRequestSiteInformationInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPostRequestSiteInformationInner from a JSON string
v1_extranets_b2b_consumer_post_request_site_information_inner_instance = V1ExtranetsB2bConsumerPostRequestSiteInformationInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPostRequestSiteInformationInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post_request_site_information_inner_dict = v1_extranets_b2b_consumer_post_request_site_information_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPostRequestSiteInformationInner from a dict
v1_extranets_b2b_consumer_post_request_site_information_inner_from_dict = V1ExtranetsB2bConsumerPostRequestSiteInformationInner.from_dict(v1_extranets_b2b_consumer_post_request_site_information_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


