# AlertserviceZendeskDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zendesk_api_token** | **str** | zendesk api token (deprecated, use zendesk_client_secret) | [optional] 
**zendesk_assignee_id** | **str** | zendesk assignee id (required) | 
**zendesk_base_url** | **str** | zendesk base url (required) | 
**zendesk_client_id** | **str** | zendesk oauth client id (required) | 
**zendesk_client_secret** | **str** | zendesk oauth client secret (required) | 
**zendesk_email** | **str** | zendesk email (deprecated, use zendesk_client_id) | [optional] 

## Example

```python
from graphiant_sdk.models.alertservice_zendesk_details import AlertserviceZendeskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AlertserviceZendeskDetails from a JSON string
alertservice_zendesk_details_instance = AlertserviceZendeskDetails.from_json(json)
# print the JSON string representation of the object
print(AlertserviceZendeskDetails.to_json())

# convert the object into a dict
alertservice_zendesk_details_dict = alertservice_zendesk_details_instance.to_dict()
# create an instance of AlertserviceZendeskDetails from a dict
alertservice_zendesk_details_from_dict = AlertserviceZendeskDetails.from_dict(alertservice_zendesk_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


