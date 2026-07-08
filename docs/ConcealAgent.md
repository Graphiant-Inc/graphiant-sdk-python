# ConcealAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**last_checkin** | **str** |  | [optional] 
**machine** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.conceal_agent import ConcealAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ConcealAgent from a JSON string
conceal_agent_instance = ConcealAgent.from_json(json)
# print the JSON string representation of the object
print(ConcealAgent.to_json())

# convert the object into a dict
conceal_agent_dict = conceal_agent_instance.to_dict()
# create an instance of ConcealAgent from a dict
conceal_agent_from_dict = ConcealAgent.from_dict(conceal_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


