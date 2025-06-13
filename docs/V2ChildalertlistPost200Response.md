# V2ChildalertlistPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_list** | [**List[V2ChildalertlistPost200ResponseAlertListInner]**](V2ChildalertlistPost200ResponseAlertListInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_childalertlist_post200_response import V2ChildalertlistPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2ChildalertlistPost200Response from a JSON string
v2_childalertlist_post200_response_instance = V2ChildalertlistPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2ChildalertlistPost200Response.to_json())

# convert the object into a dict
v2_childalertlist_post200_response_dict = v2_childalertlist_post200_response_instance.to_dict()
# create an instance of V2ChildalertlistPost200Response from a dict
v2_childalertlist_post200_response_from_dict = V2ChildalertlistPost200Response.from_dict(v2_childalertlist_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


