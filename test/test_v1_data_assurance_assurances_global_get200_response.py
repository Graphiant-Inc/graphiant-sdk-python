# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_data_assurance_assurances_global_get200_response import V1DataAssuranceAssurancesGlobalGet200Response

class TestV1DataAssuranceAssurancesGlobalGet200Response(unittest.TestCase):
    """V1DataAssuranceAssurancesGlobalGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DataAssuranceAssurancesGlobalGet200Response:
        """Test V1DataAssuranceAssurancesGlobalGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DataAssuranceAssurancesGlobalGet200Response`
        """
        model = V1DataAssuranceAssurancesGlobalGet200Response()
        if include_optional:
            return V1DataAssuranceAssurancesGlobalGet200Response(
                rows = [
                    graphiant_sdk.models._v1_data_assurance_assurances_global_get_200_response_rows_inner._v1_data_assurance_assurances_global_get_200_response_rows_inner(
                        apps = [
                            graphiant_sdk.models._v1_data_assurance_assurances_global_get_200_response_rows_inner_apps_inner._v1_data_assurance_assurances_global_get_200_response_rows_inner_apps_inner(
                                app_name = 'example string', )
                            ], 
                        assurance_id = 1234567891011, 
                        assurance_name = 'example string', 
                        created_at = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), 
                        flex_algo = 'example string', 
                        lans = [
                            graphiant_sdk.models._v1_data_assurance_assurances_global_get_200_response_rows_inner_lans_inner._v1_data_assurance_assurances_global_get_200_response_rows_inner_lans_inner(
                                lan_name = 'example string', )
                            ], 
                        sites = [
                            graphiant_sdk.models._v1_data_assurance_assurances_global_get_200_response_rows_inner_sites_inner._v1_data_assurance_assurances_global_get_200_response_rows_inner_sites_inner(
                                site_name = 'example string', )
                            ], 
                        updated_at = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), )
                    ]
            )
        else:
            return V1DataAssuranceAssurancesGlobalGet200Response(
        )
        """

    def testV1DataAssuranceAssurancesGlobalGet200Response(self):
        """Test V1DataAssuranceAssurancesGlobalGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
