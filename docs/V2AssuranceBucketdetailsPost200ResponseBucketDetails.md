# V2AssuranceBucketdetailsPost200ResponseBucketDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_count_threat_high** | **int** |  | [optional] 
**app_count_threat_low** | **int** |  | [optional] 
**app_count_threat_medium** | **int** |  | [optional] 
**app_id_records** | [**List[V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord]**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.md) |  | [optional] 
**app_name_records** | [**List[V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord]**](V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord.md) |  | [optional] 
**bucket_name_to_display** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_ip_port** | **bool** |  | [optional] 
**flow_count** | **int** |  | [optional] 
**new_ip_hint** | **bool** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**trend_value_list** | [**List[V2AssuranceBucketdetailsPost200ResponseBucketDetailsTrendValueListInner]**](V2AssuranceBucketdetailsPost200ResponseBucketDetailsTrendValueListInner.md) |  | [optional] 
**unique_app_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_bucketdetails_post200_response_bucket_details import V2AssuranceBucketdetailsPost200ResponseBucketDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceBucketdetailsPost200ResponseBucketDetails from a JSON string
v2_assurance_bucketdetails_post200_response_bucket_details_instance = V2AssuranceBucketdetailsPost200ResponseBucketDetails.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceBucketdetailsPost200ResponseBucketDetails.to_json())

# convert the object into a dict
v2_assurance_bucketdetails_post200_response_bucket_details_dict = v2_assurance_bucketdetails_post200_response_bucket_details_instance.to_dict()
# create an instance of V2AssuranceBucketdetailsPost200ResponseBucketDetails from a dict
v2_assurance_bucketdetails_post200_response_bucket_details_from_dict = V2AssuranceBucketdetailsPost200ResponseBucketDetails.from_dict(v2_assurance_bucketdetails_post200_response_bucket_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


