# V1ExtranetsB2bConsumerIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **int** |  | [optional] 
**policy** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInner.md) |  | [optional] 
**service_name** | **str** |  | [optional] 
**site_information** | [**List[V1ExtranetsB2bConsumerPostRequestSiteInformationInner]**](V1ExtranetsB2bConsumerPostRequestSiteInformationInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_id_get200_response import V1ExtranetsB2bConsumerIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerIdGet200Response from a JSON string
v1_extranets_b2b_consumer_id_get200_response_instance = V1ExtranetsB2bConsumerIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerIdGet200Response.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_id_get200_response_dict = v1_extranets_b2b_consumer_id_get200_response_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerIdGet200Response from a dict
v1_extranets_b2b_consumer_id_get200_response_from_dict = V1ExtranetsB2bConsumerIdGet200Response.from_dict(v1_extranets_b2b_consumer_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


