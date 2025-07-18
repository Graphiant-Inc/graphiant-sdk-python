# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_bwtracker_region_cloud_summary_post200_response import V1BwtrackerRegionCloudSummaryPost200Response

class TestV1BwtrackerRegionCloudSummaryPost200Response(unittest.TestCase):
    """V1BwtrackerRegionCloudSummaryPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1BwtrackerRegionCloudSummaryPost200Response:
        """Test V1BwtrackerRegionCloudSummaryPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1BwtrackerRegionCloudSummaryPost200Response`
        """
        model = V1BwtrackerRegionCloudSummaryPost200Response()
        if include_optional:
            return V1BwtrackerRegionCloudSummaryPost200Response(
                bwusage_summary = graphiant_sdk.models._v1_bwtracker_region_cloud_summary_post_200_response_bwusage_summary._v1_bwtracker_region_cloud_summary_post_200_response_bwusageSummary(
                    bwusage_top_providers = [
                        graphiant_sdk.models._v1_bwtracker_region_cloud_summary_post_200_response_bwusage_summary_bwusage_top_providers_inner._v1_bwtracker_region_cloud_summary_post_200_response_bwusageSummary_bwusageTopProviders_inner(
                            capacity_kbps = 123.45, 
                            provider_id = 12345678910, 
                            provider_name = 'example string', 
                            usage_kbps = 123.45, )
                        ], 
                    cloudusage_kbps = 123.45, 
                    percent_changed = 123.45, 
                    provider_count = 12345678910, 
                    providerusage_kbps = 12345678910, 
                    totusage_kbps = 123.45, )
            )
        else:
            return V1BwtrackerRegionCloudSummaryPost200Response(
        )
        """

    def testV1BwtrackerRegionCloudSummaryPost200Response(self):
        """Test V1BwtrackerRegionCloudSummaryPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
