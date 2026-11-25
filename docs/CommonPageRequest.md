# CommonPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** |  | [optional] 
**last** | **int** |  | [optional] 
**token** | **str** |  | [optional] 
**after** | **str** |  | [optional] 
**first** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.common_page_request import CommonPageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPageRequest from a JSON string
common_page_request_instance = CommonPageRequest.from_json(json)
# print the JSON string representation of the object
print(CommonPageRequest.to_json())

# convert the object into a dict
common_page_request_dict = common_page_request_instance.to_dict()
# create an instance of CommonPageRequest from a dict
common_page_request_from_dict = CommonPageRequest.from_dict(common_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


