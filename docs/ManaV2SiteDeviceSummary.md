# ManaV2SiteDeviceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_site_device_summary import ManaV2SiteDeviceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2SiteDeviceSummary from a JSON string
mana_v2_site_device_summary_instance = ManaV2SiteDeviceSummary.from_json(json)
# print the JSON string representation of the object
print(ManaV2SiteDeviceSummary.to_json())

# convert the object into a dict
mana_v2_site_device_summary_dict = mana_v2_site_device_summary_instance.to_dict()
# create an instance of ManaV2SiteDeviceSummary from a dict
mana_v2_site_device_summary_from_dict = ManaV2SiteDeviceSummary.from_dict(mana_v2_site_device_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


