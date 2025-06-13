# V2RuleEnabledisablePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**rule_id_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_rule_enabledisable_post_request import V2RuleEnabledisablePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2RuleEnabledisablePostRequest from a JSON string
v2_rule_enabledisable_post_request_instance = V2RuleEnabledisablePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2RuleEnabledisablePostRequest.to_json())

# convert the object into a dict
v2_rule_enabledisable_post_request_dict = v2_rule_enabledisable_post_request_instance.to_dict()
# create an instance of V2RuleEnabledisablePostRequest from a dict
v2_rule_enabledisable_post_request_from_dict = V2RuleEnabledisablePostRequest.from_dict(v2_rule_enabledisable_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


