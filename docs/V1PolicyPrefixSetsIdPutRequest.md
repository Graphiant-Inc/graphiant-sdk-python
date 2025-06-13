# V1PolicyPrefixSetsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.md) |  | [optional] 
**name** | **str** |  | [optional] 
**prefix_set_entries** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValue]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_prefix_sets_id_put_request import V1PolicyPrefixSetsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyPrefixSetsIdPutRequest from a JSON string
v1_policy_prefix_sets_id_put_request_instance = V1PolicyPrefixSetsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1PolicyPrefixSetsIdPutRequest.to_json())

# convert the object into a dict
v1_policy_prefix_sets_id_put_request_dict = v1_policy_prefix_sets_id_put_request_instance.to_dict()
# create an instance of V1PolicyPrefixSetsIdPutRequest from a dict
v1_policy_prefix_sets_id_put_request_from_dict = V1PolicyPrefixSetsIdPutRequest.from_dict(v1_policy_prefix_sets_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


