# V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**site_id** | **int** |  | [optional] 
**tag** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner import V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner from a JSON string
v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner_instance = V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner.to_json())

# convert the object into a dict
v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner_dict = v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner_instance.to_dict()
# create an instance of V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner from a dict
v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner_from_dict = V1PolicyRouteTagSetsTagDetailGet200ResponseDevicesInner.from_dict(v1_policy_route_tag_sets_tag_detail_get200_response_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


