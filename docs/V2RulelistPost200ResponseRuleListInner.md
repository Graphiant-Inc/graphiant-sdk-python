# V2RulelistPost200ResponseRuleListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm_clear** | **str** |  | [optional] 
**alarm_set** | **str** |  | [optional] 
**allow_count** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**plane** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**rule_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_rulelist_post200_response_rule_list_inner import V2RulelistPost200ResponseRuleListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2RulelistPost200ResponseRuleListInner from a JSON string
v2_rulelist_post200_response_rule_list_inner_instance = V2RulelistPost200ResponseRuleListInner.from_json(json)
# print the JSON string representation of the object
print(V2RulelistPost200ResponseRuleListInner.to_json())

# convert the object into a dict
v2_rulelist_post200_response_rule_list_inner_dict = v2_rulelist_post200_response_rule_list_inner_instance.to_dict()
# create an instance of V2RulelistPost200ResponseRuleListInner from a dict
v2_rulelist_post200_response_rule_list_inner_from_dict = V2RulelistPost200ResponseRuleListInner.from_dict(v2_rulelist_post200_response_rule_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


