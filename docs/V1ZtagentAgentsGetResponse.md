# V1ZtagentAgentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[ConcealAgent]**](ConcealAgent.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_ztagent_agents_get_response import V1ZtagentAgentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ZtagentAgentsGetResponse from a JSON string
v1_ztagent_agents_get_response_instance = V1ZtagentAgentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ZtagentAgentsGetResponse.to_json())

# convert the object into a dict
v1_ztagent_agents_get_response_dict = v1_ztagent_agents_get_response_instance.to_dict()
# create an instance of V1ZtagentAgentsGetResponse from a dict
v1_ztagent_agents_get_response_from_dict = V1ZtagentAgentsGetResponse.from_dict(v1_ztagent_agents_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


