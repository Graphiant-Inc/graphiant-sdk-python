# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_bucketdetails_post200_response_bucket_details import V2AssuranceBucketdetailsPost200ResponseBucketDetails

class TestV2AssuranceBucketdetailsPost200ResponseBucketDetails(unittest.TestCase):
    """V2AssuranceBucketdetailsPost200ResponseBucketDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceBucketdetailsPost200ResponseBucketDetails:
        """Test V2AssuranceBucketdetailsPost200ResponseBucketDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceBucketdetailsPost200ResponseBucketDetails`
        """
        model = V2AssuranceBucketdetailsPost200ResponseBucketDetails()
        if include_optional:
            return V2AssuranceBucketdetailsPost200ResponseBucketDetails(
                app_count_threat_high = 1234567891011,
                app_count_threat_low = 1234567891011,
                app_count_threat_medium = 1234567891011,
                app_id_records = [
                    graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_id_record._v2_assurance_applicationdetailsbyname_post_200_response_appIdRecord(
                        affected_hosts = 1234567891011, 
                        affected_regions = 1234567891011, 
                        affected_sites = 1234567891011, 
                        affected_vrfs = 1234567891011, 
                        app_id_key = 'example string', 
                        app_name = 'example string', 
                        app_type = 'ENUM_VALUE', 
                        blocked_reason_list = [
                            'example string'
                            ], 
                        category = 'example string', 
                        classfication_field = 'example string', 
                        classification_field = 'example string', 
                        first_seen = 1234567891011, 
                        flex_algo = [
                            graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_id_record_flex_algo_inner._v2_assurance_applicationdetailsbyname_post_200_response_appIdRecord_flexAlgo_inner(
                                flex_algo_id = 1234567891011, 
                                flex_algo_name = 'example string', )
                            ], 
                        flows_analyzed = 1234567891011, 
                        last_seen = 1234567891011, 
                        new_ip_hint = True, 
                        recommendation = 'example string', 
                        region_list = [
                            'example string'
                            ], 
                        risk_status = 'ENUM_VALUE', 
                        server_ip = 'example string', 
                        server_port = 'example string', 
                        site_list = [
                            'example string'
                            ], 
                        threat_score = 1234567891011, 
                        vrf_list = [
                            'example string'
                            ], )
                    ],
                app_name_records = [
                    graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_name_record._v2_assurance_applicationdetailsbyname_post_200_response_appNameRecord(
                        affected_hosts = 1234567891011, 
                        affected_regions = 1234567891011, 
                        affected_sites = 1234567891011, 
                        affected_vrfs = 1234567891011, 
                        app_id = 1234567891011, 
                        app_id_records = [
                            graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_id_record._v2_assurance_applicationdetailsbyname_post_200_response_appIdRecord(
                                affected_hosts = 1234567891011, 
                                affected_regions = 1234567891011, 
                                affected_sites = 1234567891011, 
                                affected_vrfs = 1234567891011, 
                                app_id_key = 'example string', 
                                app_name = 'example string', 
                                app_type = 'ENUM_VALUE', 
                                blocked_reason_list = [
                                    'example string'
                                    ], 
                                category = 'example string', 
                                classfication_field = 'example string', 
                                classification_field = 'example string', 
                                first_seen = 1234567891011, 
                                flex_algo = [
                                    graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_id_record_flex_algo_inner._v2_assurance_applicationdetailsbyname_post_200_response_appIdRecord_flexAlgo_inner(
                                        flex_algo_id = 1234567891011, 
                                        flex_algo_name = 'example string', )
                                    ], 
                                flows_analyzed = 1234567891011, 
                                last_seen = 1234567891011, 
                                new_ip_hint = True, 
                                recommendation = 'example string', 
                                region_list = [
                                    'example string'
                                    ], 
                                risk_status = 'ENUM_VALUE', 
                                server_ip = 'example string', 
                                server_port = 'example string', 
                                site_list = [
                                    'example string'
                                    ], 
                                threat_score = 1234567891011, 
                                vrf_list = [
                                    'example string'
                                    ], )
                            ], 
                        app_name = 'example string', 
                        app_type = 'ENUM_VALUE', 
                        category = 'example string', 
                        da_classified = True, 
                        flex_algo = [
                            graphiant_sdk.models._v2_assurance_applicationdetailsbyname_post_200_response_app_id_record_flex_algo_inner._v2_assurance_applicationdetailsbyname_post_200_response_appIdRecord_flexAlgo_inner(
                                flex_algo_id = 1234567891011, 
                                flex_algo_name = 'example string', )
                            ], 
                        flows_analyzed = 1234567891011, 
                        recommendation = 'example string', 
                        risk_status = 'ENUM_VALUE', 
                        threat_score = 1234567891011, )
                    ],
                bucket_name_to_display = 'example string',
                description = 'example string',
                display_ip_port = True,
                flow_count = 1234567891011,
                new_ip_hint = True,
                recommendation = 'example string',
                trend_value_list = [
                    graphiant_sdk.models._v2_assurance_bucketdetails_post_200_response_bucket_details_trend_value_list_inner._v2_assurance_bucketdetails_post_200_response_bucketDetails_trendValueList_inner(
                        end_time = 1234567891011, 
                        flow_count = 1234567891011, 
                        start_time = 1234567891011, )
                    ],
                unique_app_count = 1234567891011
            )
        else:
            return V2AssuranceBucketdetailsPost200ResponseBucketDetails(
        )
        """

    def testV2AssuranceBucketdetailsPost200ResponseBucketDetails(self):
        """Test V2AssuranceBucketdetailsPost200ResponseBucketDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
