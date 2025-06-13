# V1EventSystemAckPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_event_system_ack_post_request import V1EventSystemAckPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventSystemAckPostRequest from a JSON string
v1_event_system_ack_post_request_instance = V1EventSystemAckPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1EventSystemAckPostRequest.to_json())

# convert the object into a dict
v1_event_system_ack_post_request_dict = v1_event_system_ack_post_request_instance.to_dict()
# create an instance of V1EventSystemAckPostRequest from a dict
v1_event_system_ack_post_request_from_dict = V1EventSystemAckPostRequest.from_dict(v1_event_system_ack_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


