# V1ExtranetsIdApplyPost202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1ExtranetsIdApplyPost202ResponseDevicesInner]**](V1ExtranetsIdApplyPost202ResponseDevicesInner.md) |  | [optional] 
**job_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_id_apply_post202_response import V1ExtranetsIdApplyPost202Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsIdApplyPost202Response from a JSON string
v1_extranets_id_apply_post202_response_instance = V1ExtranetsIdApplyPost202Response.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsIdApplyPost202Response.to_json())

# convert the object into a dict
v1_extranets_id_apply_post202_response_dict = v1_extranets_id_apply_post202_response_instance.to_dict()
# create an instance of V1ExtranetsIdApplyPost202Response from a dict
v1_extranets_id_apply_post202_response_from_dict = V1ExtranetsIdApplyPost202Response.from_dict(v1_extranets_id_apply_post202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


