# V1ExtranetsB2bConsumerPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**List[V1ExtranetsB2bConsumerPostRequestPolicyInner]**](V1ExtranetsB2bConsumerPostRequestPolicyInner.md) |  | [optional] 
**provider_enterprise_id** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 
**site_information** | [**List[V1ExtranetsB2bConsumerPostRequestSiteInformationInner]**](V1ExtranetsB2bConsumerPostRequestSiteInformationInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post_request import V1ExtranetsB2bConsumerPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPostRequest from a JSON string
v1_extranets_b2b_consumer_post_request_instance = V1ExtranetsB2bConsumerPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPostRequest.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post_request_dict = v1_extranets_b2b_consumer_post_request_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPostRequest from a dict
v1_extranets_b2b_consumer_post_request_from_dict = V1ExtranetsB2bConsumerPostRequest.from_dict(v1_extranets_b2b_consumer_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


