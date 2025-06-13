# V2AckCreateupdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id_list** | **List[str]** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_ack_createupdate_post_request import V2AckCreateupdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AckCreateupdatePostRequest from a JSON string
v2_ack_createupdate_post_request_instance = V2AckCreateupdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AckCreateupdatePostRequest.to_json())

# convert the object into a dict
v2_ack_createupdate_post_request_dict = v2_ack_createupdate_post_request_instance.to_dict()
# create an instance of V2AckCreateupdatePostRequest from a dict
v2_ack_createupdate_post_request_from_dict = V2AckCreateupdatePostRequest.from_dict(v2_ack_createupdate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


