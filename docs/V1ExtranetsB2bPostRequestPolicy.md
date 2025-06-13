# V1ExtranetsB2bPostRequestPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_pools** | **List[str]** |  | [optional] 
**profiles** | [**List[V1ExtranetsB2bPostRequestPolicyProfilesInner]**](V1ExtranetsB2bPostRequestPolicyProfilesInner.md) |  | [optional] 
**service_lan_segment** | **int** |  | [optional] 
**service_prefixes** | **List[str]** |  | [optional] 
**sites** | [**List[V1ExtranetsB2bConsumerPostRequestSiteInformationInner]**](V1ExtranetsB2bConsumerPostRequestSiteInformationInner.md) |  | [optional] 
**sla** | [**V1ExtranetsB2bPostRequestPolicySla**](V1ExtranetsB2bPostRequestPolicySla.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_post_request_policy import V1ExtranetsB2bPostRequestPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bPostRequestPolicy from a JSON string
v1_extranets_b2b_post_request_policy_instance = V1ExtranetsB2bPostRequestPolicy.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bPostRequestPolicy.to_json())

# convert the object into a dict
v1_extranets_b2b_post_request_policy_dict = v1_extranets_b2b_post_request_policy_instance.to_dict()
# create an instance of V1ExtranetsB2bPostRequestPolicy from a dict
v1_extranets_b2b_post_request_policy_from_dict = V1ExtranetsB2bPostRequestPolicy.from_dict(v1_extranets_b2b_post_request_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


